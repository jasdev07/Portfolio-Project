import os
import io
import pickle
import shutil
import logging
import librosa
from time import time
from datetime import datetime
from typing_extensions import Annotated

import yaml
import numpy as np
from PIL import Image
import tensorflow as tf
from fastapi import Request
from fastapi import HTTPException, File, UploadFile, Form, APIRouter

from src.utils.audio_utils import convert_audio_to_wav
from src.prediction.prediction_e2 import predict_class
from src.preprocessing.preprocessing_pipeline_e2 import create_torch_records
from src.prediction.prediction_e1 import get_image_prediction, get_ensemble_predictions_proba
from src.preprocessing.preprocessing_pipeline_e1 import prepare_sample_from_images, preprocess_tabular, preprocess_audio


# Initialize router
router = APIRouter()

# Set up logging
logger = logging.getLogger(__name__)


# Convert Numpy to Python
def convert_numpy_to_python(data):
    """Converts numpy data types in a nested dictionary to native Python types."""
    if isinstance(data, dict):
        return {key: convert_numpy_to_python(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [convert_numpy_to_python(item) for item in data]
    elif isinstance(data, np.ndarray):
        return data.tolist()
    elif isinstance(data, (np.int_, np.intc, np.intp, np.int8, np.int16, np.int32, np.int64,
                           np.uint8, np.uint16, np.uint32, np.uint64)):
        return int(data)
    elif isinstance(data, (np.float_, np.float16, np.float32, np.float64)):
        return round(float(data),2)
    return data

# This code is upon for calucating button
@router.post("/calculate")
async def calculate_button(
		request: Request,
		Brand: Annotated[str, Form(
			..., 
			description="Brand of the motorcycle.\n\n"
						"    Example: 'Yamaha'"
		)],
		ModelType: Annotated[str, Form(
			..., 
			description="Model Type of the motorcycle.\n\n"
						"    Example: 'YZF-R1'"
		)],
		ModelFrameworks: Annotated[str, Form(
			..., 
			description="Framework of the motorcycle.\n\n"
						"    Example: 'independent_model'"
		)],
		BrandNewDate: Annotated[str, Form(
			..., 
			description="The manufacturing date of the motorcycle.\n\n"
						"    Example: '2023-06-15T00:00:00.000Z'"
		)],
		RepossessedDate: Annotated[str, Form(
			..., 
			description="The date when the motorcycle was repossessed.\n\n"
						"    Example: '2024-01-10T00:00:00.000Z'"
		)],
		LeftImageFile: Annotated[UploadFile, File(
			..., 
			description="Upload the left side image of the motorcycle.\n\n"
						"    Note: The image should clearly show the left side."
		)],
		RightImageFile: Annotated[UploadFile, File(
			..., 
			description="Upload the right side image of the motorcycle.\n\n"
						"    Note: The image should clearly show the right side."
		)],
		FrontImageFile: Annotated[UploadFile, File(
			..., 
			description="Upload the front image of the motorcycle.\n\n"
						"    Note: The image should clearly show the front view."
		)],
		RearImageFile: Annotated[UploadFile, File(
			..., 
			description="Upload the rear image of the motorcycle.\n\n"
						"    Note: The image should clearly show the rear view."
		)],
		AudioFile: Annotated[UploadFile, File(
			..., 
			description="Upload an audio file containing the sound of the motorcycle's engine.\n\n"
						"    Note: The audio should be clear and without background noise."
		)]

	):
	"""
	Receives motorcycle details and multimedia files, processes them using various
	machine learning models, and returns an ensemble prediction of the motorcycle's
	status.

	Parameters:
	- Brand (str): Brand of the motorcycle.
	- ModelType (str): Model Type of the motorcycle.
	- ModelFrameworks (str): Framework of the motorcycle model.
	- BrandNewDate (str): ISO 8601 formatted date indicating when the motorcycle was brand new.
	- RepossessedDate (str): ISO 8601 formatted date indicating when the motorcycle was repossessed.
	- LeftImageFile (UploadFile): The uploaded image file of the motorcycle's left side.
	- RightImageFile (UploadFile): The uploaded image file of the motorcycle's right side.
	- FrontImageFile (UploadFile): The uploaded image file of the motorcycle's front.
	- RearImageFile (UploadFile): The uploaded image file of the motorcycle's rear.
	- AudioFile (UploadFile): The uploaded audio file containing the sound of the motorcycle.

	Returns:
	- dict: A dictionary containing the key 'ensemble_prediction' mapped to the ensemble prediction result.
	
	Raises:
	- HTTPException: An error response with status code 400 when input validation fails.
	"""
	try:
		# Record start time
		start_time = time()

		# Temporary file paths
		temp_audio_m4a = 'temp_audio.m4a'
		temp_audio_wav = 'temp_audio.wav'

		# Parsing dates from string to datetime
		brand_new_date = datetime.strptime(BrandNewDate, "%Y-%m-%dT%H:%M:%S.%fZ")
		repossessed_date = datetime.strptime(RepossessedDate, "%Y-%m-%dT%H:%M:%S.%fZ")

		# Read image bytes
		left_image_bytes = await LeftImageFile.read()
		front_image_bytes = await FrontImageFile.read()
		right_image_bytes = await RightImageFile.read()
		rear_image_bytes = await RearImageFile.read()


		# Open images from the uploaded files
		left_image = Image.open(io.BytesIO(left_image_bytes))
		front_image = Image.open(io.BytesIO(front_image_bytes))
		right_image = Image.open(io.BytesIO(right_image_bytes))
		rear_image = Image.open(io.BytesIO(rear_image_bytes))


		# image library processing
		cur_images = {
			'front': front_image,
			'rear': rear_image,
			'right': right_image,
			'left': left_image
		}
		
		########## Audio model processing ###########
		# Save the uploaded audio file temporarily and process
		with open(temp_audio_m4a, 'wb') as temp_file:
			shutil.copyfileobj(AudioFile.file, temp_file)

		# Attempt to process the audio file with librosa
		try:
			audio_ts, sr = librosa.load(temp_audio_m4a, sr=None, duration=9, mono=True)
		except Exception as librosa_error:
			# If librosa fails, convert the file to WAV and retry
			print(f"Librosa failed to load the audio file: {librosa_error}, converting to WAV.")
			# This matches the function definition now
			convert_audio_to_wav(temp_audio_m4a, temp_audio_wav)  
			audio_ts, sr = librosa.load(temp_audio_wav, sr=None, duration=9, mono=True)
			# Clean up the converted WAV file after processing
			os.remove(temp_audio_wav)

		if ModelFrameworks == 'independent_model':
			# Get model info
			e1_info = request.app.state.e1_model_info
			# Get models
			models = request.app.state.models
			image_model = models['image_model']
			tabular_model = models['tabular_model']
			audio_model = models['audio_model']

			######## Imagee model processing ##########

			cur_sample = prepare_sample_from_images(cur_images)
			# image_prediction = get_prediction(cur_sample, image_model)
			_, image_preds_proba = get_image_prediction(cur_sample,image_model)

			######### Tabular model processing #########
			tabular_cols_filepath = os.path.join(
       			e1_info['MODEL_DIRPATH'], e1_info['TABULAR_COLS_FILEPATH'])
			tabular_sample = preprocess_tabular(brand_new_date, repossessed_date, ModelType, tabular_cols_filepath)
			# tabular_prediction = classes[tabular_model.predict(tabular_sample).iloc[0]]
			tabular_preds_proba = tabular_model.predict_proba(tabular_sample).iloc[0].to_numpy()

			# Preprocess the audio data for the model
			audio_sample = preprocess_audio(audio_ts, sr)

			# Predict using the audio model and get the first result
			# audio_class = audio_model.predict(audio_sample).iloc[0]
			audio_preds_proba = audio_model.predict_proba(audio_sample).iloc[0].to_numpy()

			# Convert the prediction to a more interpretable form using the 'classes' dictionary
			# audio_prediction = classes[audio_class]

			########## Ensemble ###########
			# ensemble_prediction = get_ensemble_predictions(ALPHA, BETA, image_prediction, audio_prediction, tabular_prediction)
			# ensemble_prediction_converted = convert_numpy_to_python(ensemble_prediction)
			alpha = e1_info['ALPHA']
			beta = e1_info['BETA']
			ensemble_prediction = get_ensemble_predictions_proba(
       			image_preds_proba, audio_preds_proba, tabular_preds_proba,
          		alpha, beta)

			# print("Ensemble Prediction", ensemble_prediction)
			print("Ensemble Prediction", ensemble_prediction['prediction'])
			print("Probabilities per Class", ensemble_prediction['probabilities'])

			# Return the prediction result
			# return {"ensemble_prediction": ensemble_prediction}
			return {
				"ensemble_prediction": ensemble_prediction['prediction'],
				"probabilities": ensemble_prediction['probabilities'],
				"model_number": e1_info['MODEL_NUMBER'],
				"runtime": time() - start_time
			}
		
		elif ModelFrameworks == 'deep_neural_network':
			# Get E2 model info
			e2_info = request.app.state.e2_model_info
			e2_model_dirpath = e2_info['MODEL_DIRPATH']
			print('ModelFrameworks is deep_neural_network')

			# Open the file in binary read mode
			tabular_col_pkl_filepath = os.path.join(
       			e2_model_dirpath, e2_info['TABULAR_COLS_PKL'])
			with open(tabular_col_pkl_filepath, 'rb') as file:
				tab_columns = pickle.load(file)


			# Prepare data for ensemble framework 2
			data_input = create_torch_records(cur_images,
											  audio_ts, sr,
											  tab_columns,
											  brand_new_date,
											  repossessed_date,
											  ModelType)

			model_filepath = os.path.join(
       			e2_model_dirpath, e2_info['E2_MODEL_FILEPATH'])
			ensemble_prediction = predict_class(model_filepath, data_input)

			# Convert numpy data types to Python types for JSON serialization
			ensemble_prediction_converted = convert_numpy_to_python(ensemble_prediction)
			

		
			# Here, ensemble_prediction already includes 'prediction' and 'probabilities'
			print("Ensemble Prediction", ensemble_prediction['prediction'])
			print("Probabilities per Class", ensemble_prediction_converted['probabilities'])			
			# Return the prediction result
			return {
				"ensemble_prediction": ensemble_prediction_converted['prediction'],
				"probabilities": ensemble_prediction_converted['probabilities'],
				"model_number": e2_info['MODEL_NUMBER'],
				"runtime": time() - start_time
			}

	except ValueError as e:
		logger.error(f"Validation error: {str(e)} - Brand New Date: {BrandNewDate}, Repossessed Date: {RepossessedDate}")
		raise HTTPException(status_code=400, detail=str(e))
	finally:
		# Clean up the temporary M4A file
		if os.path.exists(temp_audio_m4a):
			os.remove(temp_audio_m4a)
