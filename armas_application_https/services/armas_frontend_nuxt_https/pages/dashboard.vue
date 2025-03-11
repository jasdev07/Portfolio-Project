<template>
	<div>
		<Navbar :links="[{ name: 'Dashboard', href: '/dashboard' }, { name: 'Home', href: '/' }, { name: 'About Us', href: '/about' }]" />
			<div :style="{ paddingLeft: '5%', paddingRight: '5%' }" class="box-animation dashboard-container">
				<transition name="fade-slide">

				<div class="mt-2">
					<label class="block mb-2 text-4xl font-bold text-black space-x-4">Dashboard</label>
				</div>
				</transition>

				<div class="container mx-auto p-4">

					<div class="flex-1 bg-zinc-800 focus:ring-4 focus:outline-none focus:ring-yellow-100 dark:focus:ring-yellow-500 shadow-lg shadow-yellow-500/50 dark:shadow-lg dark:shadow-yellow-800/80 font-medium rounded-lg text-sm px-5 py-2.5 text-center mr-2 mb-2">
							<SubLabel label="Please Input the Motorcycle Details" />
						</div>

						<div class="grid grid-cols-1 lg:grid-cols-2 gap-4 p-4">
						
							<!-- Left Column for Input Details and Uploads -->
							<div class="flex-1 text-black bg-yellow-500  focus:ring-4 focus:outline-none focus:ring-yellow-100 dark:focus:ring-yellow-500 shadow-lg shadow-yellow-500/50 dark:shadow-lg dark:shadow-yellow-800/80 font-medium rounded-lg text-sm px-5 py-2.5 text-center mr-2 mb-2">

								<!-- <CenteredLabel label="Please Input the Details" /> -->
								<div class="mt-5">
									<CenteredLabel label="Tabular Details" />
								</div>


								<div class="mt-5">
									<!-- Input Brand Name  -->
									<FormSelect
											id="brand_model"
											label="Brand"
											:options="brandOptions"
											v-model="SelectedBrand"
											placeholder="Select a brand"
										/>
										<FormSelect
											id="motor_model"
											label="Model Type"
											:options="availableModels"
											v-model="SelectedModel"
											placeholder="Select a model"
										/>
									</div>

									<div>
										
										<!-- Input Brand Name  -->
										<DateInput id="BrandNewDate"
											label="Brand New Date"
											v-model="BrandNewDate"
											placeholder="Select date start" />
										<DateInput id="repossessedDate"
											label="Repossessed Date"
											v-model="RepossessedDate"
											placeholder="Select date start" />
									</div>

								<div class="mt-3">
							</div>
						
						</div>

							<!-- Right Column for Previews and Predicted Class -->
							<div class="flex-1 text-black bg-yellow-500  focus:ring-4 focus:outline-none focus:ring-yellow-100 dark:focus:ring-yellow-500 shadow-lg shadow-yellow-500/50 dark:shadow-lg dark:shadow-yellow-800/80 font-medium rounded-lg text-sm px-5 py-2.5 text-center mr-2 mb-2">
								<div class="mt-5">
									<CenteredLabel label="Upload Images" />
								</div>
								<div class="grid grid-cols-1 lg:grid-cols-2 gap-4">
									<div>
										<LabelComponent id="Left-Image-Preview" label="Left Image Preview" />
										<PreviewImage ref="leftImageUpload" @image-uploaded="LeftHandleImageUpload" />
									</div>
									<div>
										<LabelComponent id="Front-Image-Preview" label="Front Image Preview" />
										<PreviewImage ref="frontImageUpload" @image-uploaded="FrontHandleImageUpload" />
									</div>
									
								</div>
								<div class="grid grid-cols-1 lg:grid-cols-2 gap-4 mt-4">
									
									<div>
										<LabelComponent id="Right-Image-Preview" label="Right Image Preview" />
										<PreviewImage ref="rightImageUpload" @image-uploaded="RightHandleImageUpload" />
									</div>
									<div>
										<LabelComponent id="Rear-Image-Preview" label="Rear Image Preview" />
										<PreviewImage ref="rearImageUpload" @image-uploaded="RearHandleImageUpload" />
									</div>
								</div>

								<div class="mt-10">
									<CenteredLabel label="Upload Audio" />
								</div>
									<!-- Audio upload section -->
									<AudioUploadComponent
										ref="audioUpload"
										@audio-selected="handleAudioFile"
										@audio-recorded="handleAudioFile"
									/>
								
							</div>			
					</div>
					<div class="grid grid-cols-1 lg:grid-cols-2 gap-4 p-4">
						<div>
							<div class="flex-1 bg-zinc-800  focus:ring-4 focus:outline-none focus:ring-yellow-100 dark:focus:ring-yellow-500 shadow-lg shadow-yellow-500/50 dark:shadow-lg dark:shadow-yellow-800/80 font-medium rounded-lg text-sm px-5 py-2.5 text-center mr-2 mb-2 ">
								<SubLabel label="Please Input Model Framework" />	
							</div>
							<div class="flex-grow p-4">
								<div class="flex-1 bg-yellow-500  focus:ring-4 focus:outline-none focus:ring-yellow-100 dark:focus:ring-yellow-500 shadow-lg shadow-yellow-500/50 dark:shadow-lg dark:shadow-yellow-800/80 font-medium rounded-lg text-sm px-5 py-2.5 text-center mr-2 mb-2 ">
									<ModelFrameworkSelect
											label="Model Framework"
											v-model="SelectedModelFramework"
											placeholder="Select Model Framework"
										/>
								</div>
							</div>
						</div>
						<div>
							<div class="flex-1 bg-zinc-800  focus:ring-4 focus:outline-none focus:ring-yellow-100 dark:focus:ring-yellow-500 shadow-lg shadow-yellow-500/50 dark:shadow-lg dark:shadow-yellow-800/80 font-medium rounded-lg text-sm px-5 py-2.5 text-center mr-2 mb-2 floating">
								<SubLabel label="Please Click the Calculate Button to show the class prediction" />
							</div>
							<div class="flex-grow p-4">
								<div class="flex-1 text-black bg-yellow-500  focus:ring-4 focus:outline-none focus:ring-yellow-100 dark:focus:ring-yellow-500 shadow-lg shadow-yellow-500/50 dark:shadow-lg dark:shadow-yellow-800/80 font-medium rounded-lg text-sm px-5 py-2.5 text-center mr-2 mb-2 floating">
									<div class="p-4">
										<div class="grid grid-cols-1 lg:grid-cols-2 gap-4">

										<!-- Calculate Button -->
										<FlexibleButton
											buttonText="Calculate"
											buttonClass="calculate-btn-class bg-yellow-500 text-black-500 hover:bg-black hover:text-yellow-500"
											:loading="calculating"
											@click="calculate"
											/>

											<!-- Clear Button -->
											<FlexibleButton 
												buttonText="Clear" 
												buttonClass="clear-btn-class bg-yellow-500 text-black-500 hover:bg-blackhover:text-yellow-500" 
												@click.native="clearInputs" />
										</div>

										<div class="grid grid-cols-1 md:grid-cols-2 items-center gap-2 mt-4">
											<transition name="fade-slide">
												<div v-if="ensemblePrediction" class="text-3xl md:text-6xl font-bold text-black">
													<h5 class="text-2xl md:text-4xl font-bold text-black">Predicted Class: {{ ensemblePrediction }}</h5> 
												</div>
											</transition>

											<div class="relative flex flex-col items-center">
												<transition name="fade-slide">

												<button
													@mouseenter="showPopover = true"
													@mouseleave="showPopover = false"
													v-if="showProbabilitiesButton"
													class="p-2 bg-black text-white font-semibold rounded-lg text-lg md:text-xl">
													Probabilities Details
												</button>
											</transition>

												<!-- Popover -->
												<div v-if="showPopover" 
													class="absolute mt-12 bg-white rounded-lg shadow-lg border"												
													@mouseenter="showPopover = true"
													@mouseleave="showPopover = false">
													<h5 class="text-md md:text-lg font-bold">Probabilities</h5>
													<div>
														<!-- Include your ProbabilitiesChart.vue component -->
														<ProbabilitiesChart :probabilities="probabilities" />
													</div>
												</div>

											</div>                                     
										</div>	
									</div>	
									
								</div>
							</div>
						</div>
					</div>
					
				</div>
				
			<Toast ref="toastComponent" :message="toastMessage" :type="toastType" />
		</div>

		<footer class="footer footer-center p-10 bg-stone-800 text-white">
			<div>
				<aside>
					<div class="flex items-center">
						<NuxtLink to="/" class="flex items-center mt-7">
							<img src="@/assets/images/armas.png" alt="Logo" class="h-8 mr-2">
							<span class="text-xl text-white">Unistar Armas</span>
						</NuxtLink>
					</div>
			
					<p>Copyright © 2024 - All right reserved</p>
				</aside> 
			</div>
		</footer>
	</div>
</template>

<script>
import FormSelect from '~/components/FormSelect.vue';
import brandModels from '~/assets/data/brandModels.json';
import DateInput from '~/components/DateInput.vue';
import ModelFrameworkSelect from '~/components/ModelFrameworkSelect.vue';
import CenteredLabel from '@/components/CenteredLabel.vue';
import SubLabel from '@/components/SubLabel.vue';
import AudioUploadComponent from '@/components/AudioUploadComponent.vue';
import FlexibleButton from '@/components/FlexibleButton.vue';
import Toast from '@/components/Toast.vue'; 
import PreviewImage from '@/components/PreviewImage.vue'; 
import LabelComponent from '@/components/Label.vue';
import ProbabilityChart from '@/components/ProbabilitiesChart.vue';
import axios from 'axios';
import { useRuntimeConfig } from '#app';



export default {
	components: {
		FormSelect,
		DateInput,
		ModelFrameworkSelect,
		CenteredLabel,
		SubLabel,
		AudioUploadComponent,
		Toast,
		LabelComponent,
		ProbabilityChart,
	},

	data() {
		return {
			SelectedBrand: '',
			SelectedModel: '',
			availableModels: [],
			BrandNewDate: '',
			RepossessedDate: '',
			SelectedModelFramework: '',
			recordedAudioName: null,
			toastMessage: '',
			toastType: '',
			ensemblePrediction: null,
			calculating: false,
			recordedAudioFile: null,
			probabilities: {},
			showPopover: false,
			showProbabilitiesButton: false,
		};
	},

	computed: {
		brandOptions() {
			return Object.keys(brandModels);
		},
	},

	watch: {
		SelectedBrand(newVal, oldVal) {
			if (newVal !== oldVal) {
				this.availableModels = brandModels[newVal] || [];
				this.SelectedModel = '';
			}
		},
	},

	setup() {
		const config = useRuntimeConfig();
		const apiURL = config.public.backendApiUrl; 

		return { apiURL };
		},

		
	methods: {

		togglePopover() {
        this.showPopover = !this.showPopover;
    },

		handleAudioFile(file) {
        // Logic to handle the selected audio file
        // You can access the selected file via the 'file' parameter
        // For example, you can update a data property to store the selected audio file
        this.recordedAudioFile = file;
    },
		handleRecordingStopped() {
			// Logic to handle the recording stopped event
			// This could involve stopping the recording and processing the recorded audio
			this.recordedAudioFile = file;
		},
		LeftHandleImageUpload(imageData) {
        this.leftImageData = imageData;
		},

		RightHandleImageUpload(imageData) {
			this.rightImageData = imageData;
		},

		FrontHandleImageUpload(imageData) {
			this.frontImageData = imageData;
		},

		RearHandleImageUpload(imageData) {
			this.rearImageData = imageData;
		},

		validateDates() {
			if (new Date(this.RepossessedDate) <= new Date(this.BrandNewDate)) {
				this.toastMessage = 'Repossessed Date must be greater than Brand New Date.';
				this.toastType = 'error';
				this.$refs.toastComponent.showToast();
			} else {
				// Valid dates logic
			}
		},

		checkRequiredFields() {
			if (!this.SelectedBrand || !this.SelectedModel || !this.BrandNewDate || !this.RepossessedDate || !this.SelectedModelFramework) {
				// Set the message and type for the toast
				this.toastMessage = 'Please fill in all required fields and correct format.';
				this.toastType = 'error';
				// Show the toast
				this.$refs.toastComponent.showToast();
				return false; // Indicate that a required field is missing
			}
			else if (!this.RightHandleImageUpload || !this.LeftHandleImageUpload || !this.FrontHandleImageUpload || !this.RearHandleImageUpload ) {
				// Set the message and type for the toast
				this.toastMessage = 'Please upload all required images';
				this.toastType = 'error';
				// Show the toast
				this.$refs.toastComponent.showToast();
				return false; // Indicate that a required field is missing
				
			}
			else if (!this.recordedAudioFile) {
				// Set the message and type for the toast
				this.toastMessage = 'Please upload all required Audio or Record file';
				this.toastType = 'error';
				// Show the toast
				this.$refs.toastComponent.showToast();
				return false; // Indicate that a required field is missing
				
			}
			return true; // All required fields are filled
		},

		async calculate() {
			this.calculating = true;
			this.checkRequiredFields();
			this.validateDates();

			const {
				SelectedModel, 
				SelectedModelFramework, 
				SelectedBrand, 
				BrandNewDate, 
				RepossessedDate,
			} = this;

			try {
				const formData = new FormData();
				
				formData.append("Brand", SelectedBrand);
				formData.append("ModelType", SelectedModel);
				formData.append("ModelFrameworks", SelectedModelFramework); 
				formData.append("BrandNewDate", new Date(BrandNewDate).toISOString());
				formData.append("RepossessedDate", new Date(RepossessedDate).toISOString());
				// Append files, assuming `this.leftImageData` and others are actual File objects
				if (this.leftImageData) formData.append('LeftImageFile', this.leftImageData);
				if (this.rightImageData) formData.append('RightImageFile', this.rightImageData);
				if (this.frontImageData) formData.append('FrontImageFile', this.frontImageData);
				if (this.rearImageData) formData.append('RearImageFile', this.rearImageData);
				if (this.recordedAudioFile) {
						formData.append('AudioFile', this.recordedAudioFile);
					}

				const response = await axios.post(`${this.apiURL}/calculate`, formData, {
				headers: {
					'Content-Type': 'multipart/form-data'
				}
				});
				console.log(response.data);
				this.ensemblePrediction = response.data.ensemble_prediction;
				this.probabilities = response.data.probabilities;
				this.calculating = false; 
				this.showProbabilitiesButton = true; 

			} catch (error) {
				console.error('Error sending data:', error);
			}finally {
				this.calculating = false; 
			}
			},

			clearInputs() {
				// Reset form fields
				this.calculating = false; 
				this.SelectedBrand = '';
				this.SelectedModel = '';
				this.BrandNewDate = '';
				this.RepossessedDate = '';
				this.SelectedModelFramework = '';
				this.ensemblePrediction = null;

				// Reset file data
				this.leftImageData = null;
				this.rightImageData = null;
				this.frontImageData = null;
				this.rearImageData = null;
				this.recordedAudioFile = null;
				this.probabilities = null;
				this.showProbabilitiesButton = false; 

				// Clear visual feedback like toasts
				this.toastMessage = '';
				this.toastType = '';

				// Clear any files that have been uploaded by triggering the clear method on child components
				// Use $nextTick to ensure the DOM updates before attempting to clear child components
				this.$nextTick(() => {
				if (this.$refs.leftImageUpload) this.$refs.leftImageUpload.clear();
				if (this.$refs.rightImageUpload) this.$refs.rightImageUpload.clear();
				if (this.$refs.frontImageUpload) this.$refs.frontImageUpload.clear();
				if (this.$refs.rearImageUpload) this.$refs.rearImageUpload.clear();
				if (this.$refs.audioUpload) this.$refs.audioUpload.clear();
				});

				// Assuming your Toast component has a method to hide the toast, hide it
				if (this.$refs.toastComponent) {
				this.$refs.toastComponent.hideToast();
				}
			},

			
	},
};
</script>

