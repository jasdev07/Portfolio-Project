<template>
	<transition name="fade">
	  <div v-if="!loadingComplete" class="preloader">
		<div class="preloader-inner">
		  <div class="preloader__status">
			<img src="@/assets/images/armas.png" alt="Loading..." class="small-image">
			<div class="preloader__status-text">{{ loaded }} %</div>
			<div class="preloader__status-loader">
			  <div class="preloader__status-bar" :style="loadStyle"></div>
			</div>
		  </div>
		</div>
	  </div>
	  <div v-else class="bg-gray-200">
		<NuxtPage />
	  </div>
	</transition>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  
  const loaded = ref(0);
  const loadStyle = ref({ width: '0%' });
  const loadingComplete = ref(false);
  
  const startLoading = () => {
	const loading = setInterval(() => {
	  if (loaded.value < 100) {
		loaded.value++;
		loadStyle.value.width = `${loaded.value}%`;
	  } else {
		clearInterval(loading);
		loadingComplete.value = true;
	  }
	}, 20);
  };
  
  onMounted(() => {
	startLoading();
  });
  </script>
  
  <style>
  /* Preloader styles */
  .preloader {
	position: fixed;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	background: rgba(0, 0, 0, 0.6);
	z-index: 1050;
	display: flex;
	justify-content: center;
	align-items: center;
  }
  
  .preloader-inner {
	text-align: center;
  }
  
  .small-image {
	width: 100px;
	height: 100px;
  }
  
  .preloader__status-text {
	margin-top: 20px;
	font-size: 20px;
	font-weight: bold;
  }
  
  .preloader__status-loader {
	position: relative;
	width: 100%;
	height: 5px;
	background-color: #f3f3f3;
	margin-top: 20px;
  }
  
  .preloader__status-bar {
	position: absolute;
	height: 100%;
	background-color: #3498db;
	width: 0%;
  }
  
  /* Transition for the fade effect */
  .fade-enter-active, .fade-leave-active {
	transition: opacity 2s;
  }
  .fade-enter, .fade-leave-to {
	opacity: 0;
  }
  </style>
  