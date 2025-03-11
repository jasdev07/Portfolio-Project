<template>
	<div class="max-w-sm mx-auto bg-white rounded-lg shadow-md overflow-hidden">
	  <div class="px-3.5 py-3.5">
		<div
		  class="p-3.5 bg-gray-100 border-dashed border-2 border-gray-400 rounded-lg text-center cursor-pointer"
		  @click="triggerFileInput"
		>
		<input
			type="file"
			class="hidden"
			ref="fileInput"
			@change="previewImage"
			accept="image/*"
			
			/>
		  <!-- Image preview section -->
		  <div v-if="imageUrl" class="image-preview">
			<img :src="imageUrl" alt="Preview" class="rounded-lg mx-auto" />
		  </div>
		  <!-- Default text when no image is selected -->
		  <div v-else>
			<h5 class="text-xl font-bold text-black">Upload picture</h5>
			<p class="font-normal text-sm text-Black md:px-6">Choose a valid image file (jpeg, png, svg, gif).</p>
		  </div>
		</div>
	  </div>
	</div>
  </template>
  
  <script>
	import Toast from './Toast.vue';

	export default {
		components: {
			Toast,
			},
		data() {
			return {
				imageUrl: null, 
				toastMessage: '',
				showToast: false,
			};
		},

		methods: {
			triggerFileInput() {
				this.$refs.fileInput.click(); // Programmatically trigger the file input
			},

			isValidImageFormat(fileType) {
				const validImageFormats = ['image/jpeg', 'image/png', 'image/svg+xml', 'image/gif'];
				return validImageFormats.includes(fileType.toLowerCase());
				},
			hideToast() {
				this.showToast = false;
				},
				previewImage(event) {
					const file = event.target.files[0];
					if (file) {
						if (!this.isValidImageFormat(file.type)) {
							console.error("Please select a valid image file (jpeg, png, svg, gif).");
							alert("Invalid file type"); // Temporary alert for debugging
							this.toastMessage = 'Please select a valid image file (jpeg, png, svg, gif).';
							this.showToast = true;
							this.$refs.fileInput.value = '';
						} else {
							// File is valid, proceed with preview
							const reader = new FileReader();
							reader.onload = (e) => {
								this.imageUrl = e.target.result; // Set the loaded image data URL to imageUrl
								this.$emit('image-uploaded', file); // Emit the image data to the parent component
							};
							reader.readAsDataURL(file);
						}
					}
				},

				clear() {
					this.imageUrl = null; // Assuming imageUrl is the data property holding the preview
					if (this.$refs.fileInput) {
					this.$refs.fileInput.value = ''; // Clear the actual file input
					}
					// Emit an event or perform other cleanup if necessary
				},
		
		},
	};
  </script>
  
  <style>
  /* Add styles if needed */
  .image-preview img {
	max-width: 100%;
	max-height: 100px; /* Adjust the height as needed */
  }
  </style>
  