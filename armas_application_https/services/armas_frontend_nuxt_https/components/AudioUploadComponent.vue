<template>
	<div class="relative mb-6">
		<div class="flex items-center space-x-2">
			<input
			v-if="!recordedAudioName"
			@change="handleAudioChange"
			aria-describedby="file_input_help"
			id="file_input_audio"
			type="file"
			accept="audio/*"
			class="block w-full text-sm text-black bg-yellow-100 border border-black rounded-lg cursor-pointer focus:outline-none dark:text-black dark:border-black dark:placeholder-black"
			/>
			<div v-else class="block w-full text-sm text-black bg-yellow-300 border border-black rounded-lg cursor-default focus:outline-none">
			{{ recordedAudioName }}
			</div>
			<button @click="toggleRecording" class="bg-black text-white rounded-full flex items-center justify-center shadow hover:bg-red-500 hover:text-black focus:outline-none w-12 h-12">
			{{ isRecording ? 'Stop' : 'Rec' }}
			</button>
			<span v-if="isRecording" class="text-red-500">
			Recording: {{ recordingTime }}s
			</span>
		</div>
		<span class="label-text text-xl text-black">Choose Valid Audio File (m4a, mp3, wav, flac, mpeg, x-m4a, x-wav)</span>

		<transition name="fade-slide">
			
			<div v-if="audioUrl" class="mt-2 ">
				<span class="label-text text-2xl text-black">Audio File Preview</span>
				<audio :src="audioUrl" controls class="w-full"></audio>
			</div>
		</transition>
	<!-- Toast component for showing messages -->
	<Toast ref="toast" :message="toastMessage" :type="toastType" />
	</div>
</template>


<script>
import Toast from './Toast.vue';


export default {
	components: {
	// ... other components
	Toast
},
	
	data() {
	return {
		mediaRecorder: null,
		audioChunks: [],
		isRecording: false,
		recordingTime: 0,
		audioUrl: null,
		recordedAudioName: '',
		toastMessage: '',
		toastType: 'info',
		showToast: false,

		};
	},

	mounted() {
		this.resetForm();
	},


	methods: {

	triggerToast(message, type = 'info') {
	this.toastMessage = message;
	this.toastType = type;
	this.$refs.toast.showToast();
	},

	toggleRecording() {
		// Implementation as provided in the previous response
		console.log('Toggling recording');
				if (this.isRecording) {
				this.stopRecording();
			} else {
				this.startRecording();
			}
	},
	async startRecording() {
		console.log('Starting recording');
		if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
			this.triggerToast('Recording not supported or not allowed on this browser. Please ensure the site has permission to access your microphone.', 'error');
			return;
		}

		try {
			const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
			this.mediaRecorder = new MediaRecorder(stream);
			this.mediaRecorder.ondataavailable = e => this.audioChunks.push(e.data);
			this.mediaRecorder.onstop = this.handleAudioRecordingStop.bind(this);

			this.mediaRecorder.start();
			this.isRecording = true; // Ensure this is set after you are sure recording has started
			console.log('Recording started');
		} catch (error) {
			if (error.name === 'NotAllowedError') {
			this.triggerToast('Microphone access was denied. Please allow access to your microphone and try again.', 'error');
			} else if (error.name === 'NotFoundError') {
			this.triggerToast('No microphone devices found. Please connect a microphone and try again.', 'error');
			} else {
			this.triggerToast('An error occurred: ' + error.message, 'error');
			}
			console.error('Error accessing microphone:', error);
			return;
		}

		this.recordingTime = 0; // Reset the timer to 0
		this.recordingTimer = setInterval(() => {
			this.recordingTime++; // Increment the recording time by 1 every second
		}, 1000); // Set the interval to 1000 milliseconds (1 second)
		},

	stopRecording() {
		// Implementation as provided in the previous response
		console.log('Stopping recording');
			if (this.mediaRecorder) {
				this.mediaRecorder.stop(); // Stop the media recorder
				this.isRecording = false;  // Update the recording state
				// Stop all tracks on the stream to release the microphone
				this.mediaRecorder.stream.getTracks().forEach(track => track.stop());
				// Clear the recording timer if you have one set up
				clearInterval(this.recordingTimer);
				this.recordingTimer = null; // Clear the interval reference
				console.log('Recording stopped');
			}
	},
	handleAudioRecordingStop() {
		console.log('Recording stopped');
		const audioBlob = new Blob(this.audioChunks, { type: 'audio/mpeg' });
		
		// Set the audio URL for previewing the recorded audio
		this.audioUrl = URL.createObjectURL(audioBlob);
		// Emit the audioBlob here
		this.$emit('audio-recorded', audioBlob);
		const audioForDurationCheck = new Audio(this.audioUrl);

		audioForDurationCheck.onloadedmetadata = () => {
			// Check if the audio duration is less than 10 seconds
			if (audioForDurationCheck.duration < 10) {
				this.showToast = true;
				this.triggerToast('The recorded audio must have a minimum length of 10 seconds.', 'error');
				this.audioChunks = []; // Reset the audio chunks
				this.audioUrl = null; // Clear the audio URL
				this.recordingTime = 0;
				return; // Exit the function if the condition is not met
			}

			// Proceed if the duration is 10 seconds or more
			this.recordedAudioName = "recorded_audio.mp3"; // Set a name for your recorded file for display
			this.audioChunks = [];
			this.recordingTime = 0;
		};
		},

	// Checks if the selected audio file format is valid
		isValidAudioFormat(fileType) {
			const validAudioFormats = [
				'audio/m4a', 'audio/mp3', 'audio/wav', 
				'audio/flac', 'audio/mpeg', 'audio/x-m4a' ,'audio/x-wav','audio/aac',
			];
			return validAudioFormats.includes(fileType.toLowerCase());
		},

		handleAudioChange(event) {
			// Get the file from the file input event
			const file = event.target.files[0];

			// If no file was selected, clear the previous audio URL and name
			if (!file) {
				this.audioUrl = null;
				this.recordedAudioName = '';
				return;
			}
			console.log("Uploaded file type:", file.type); // Debug MIME type			// Check if the selected file is a valid audio format
			if (this.isValidAudioFormat(file.type)) {
				// Set the audio URL for previewing the selected file
				this.audioUrl = URL.createObjectURL(file);

				// Save the name of the file for display purposes
				this.recordedAudioName = file.name;

				// Emit an event if you want the parent component to be aware of the selected file
				this.$emit('audio-selected', file);
			} else {
				this.triggerToast('Please select a valid audio file (mp3, wav, flac, mpeg, m4a, aac).', 'error');
				this.showToast = true;

				// Clear the file input
				this.$refs.fileInput.value = '';
			}
		},
		clear() {
			// Stop recording if it's happening
			if (this.isRecording) {
			this.stopRecording();
			}

			// Clear the chunks of audio data
			this.audioChunks = [];

			// Reset the recording time counter
			this.recordingTime = 0;

			// Clear the audio URL if there's one
			if (this.audioUrl) {
			URL.revokeObjectURL(this.audioUrl); // Clean up the object URL to avoid memory leaks
			this.audioUrl = null;
			}

			// Reset the name of the recorded audio file for display
			this.recordedAudioName = '';

			// Reset the input field for file upload if it's been used
			if (this.$refs.fileInputAudio) {
			this.$refs.fileInputAudio.value = '';
			}

			// Clear any displayed toasts related to the audio component
			this.toastMessage = '';
			this.toastType = 'info';
			this.showToast = false;
		},

		resetForm() {
			this.recordedAudioName = '';
			this.audioUrl = null;
			// Ensure this.$refs.fileInputAudio points to your file input element
			if (this.$refs.fileInputAudio) {
				this.$refs.fileInputAudio.value = '';
			}
			// Add any other resets for your form here
			},

	},
};
</script>
