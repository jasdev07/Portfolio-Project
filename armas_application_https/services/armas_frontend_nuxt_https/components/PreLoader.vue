<!-- Preloader.vue -->
<template>
	<div v-if="visible" class="preloader-container">
	  <span class="loading loading-spinner loading-md"></span>
	</div>
  </template>
  
  <script>
  export default {
	name: 'Preloader',
	props: {
	  visible: {
		type: Boolean,
		required: true,
	  },
	},
  };
  </script>
  
  <style scoped>
  .preloader-container {
	display: flex;
	justify-content: center;
	align-items: center;
	/* Add more styles to position the preloader as needed */
  }
  .loading-spinner {
	/* Style your spinner */
  }
  </style>
  