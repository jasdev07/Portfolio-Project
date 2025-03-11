# src/main.py

import os
import logging
from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api.endpoint.load_model_route import router as load_model_router
from .api.endpoint.calculate_route import router as calculate_router
from .api.endpoint.list_models import router as list_models_router
from .api.endpoint.general_routes import router as general_router
from .api.endpoint.batch_route import router as batch_router
from .core.openapi import custom_openapi
from .loading.listing import get_model_list
from .loading.loader import load_model_info, load_e1_model


# Define start-up and shut-down procedures
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Start-up actions
    # Load environment variables
    load_dotenv()
    MODELS_DIRPATH = os.environ['MODELS_DIRPATH']

    # List models in the model directory
    model_infos = get_model_list(MODELS_DIRPATH)
    app.state.model_infos = model_infos

    # Get latest models
    e1_model_info = load_model_info(
        model_infos.loc[model_infos.TYPE == 'E1']
                   .sort_values('DEPLOY_DATE', ascending=False)
                   .iloc[0].MODEL_DIRPATH)
    e2_model_info = load_model_info(
        model_infos.loc[model_infos.TYPE == 'E2']
                   .sort_values('DEPLOY_DATE', ascending=False)
                   .iloc[0].MODEL_DIRPATH)
    app.state.e1_model_info = e1_model_info
    app.state.e2_model_info = e2_model_info

    # Update e1 model for faster inference
    e1_model = {}
    image_model, audio_model, tabular_model = load_e1_model(e1_model_info)
    e1_model['image_model'] = image_model
    e1_model['audio_model'] = audio_model
    e1_model['tabular_model'] = tabular_model

    app.state.models = e1_model

    yield

    # Clean up actions
    e1_model.clear()


app = FastAPI(lifespan=lifespan)



# Configure CORS
allowed_origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(calculate_router)
app.include_router(batch_router)
app.include_router(list_models_router)
app.include_router(load_model_router)
app.include_router(general_router)


# Modify the OpenAPI schema
@app.get("/openapi.json", include_in_schema=False)
async def get_open_api_endpoint():
    return custom_openapi(app)

# Adjust FastAPI app's openapi method to use custom_openapi
app.openapi = lambda: custom_openapi(app)
