<template>
	<div class="carousel max-w-full lg:max-w-md p-4 space-x-4 bg-yellow-500 rounded-box w-full" style="min-height: 200px;">
	  <!-- Carousel wrapper -->
	  <div class="carousel-center relative w-full overflow-hidden rounded-box">
		<!-- Transition wrapper for sliding effect -->
		<transition-group name="slide" tag="div" class="flex" @before-enter="beforeEnter" @enter="enter" @leave="leave">
		  <!-- Slides -->
		  <div class="carousel-item flex-none w-full" v-for="(image, index) in images" :key="image" v-show="index === currentIndex">
			<img :src="image" class="w-full object-contain rounded-box" style="max-height: 80vh;"/>
		  </div>
		</transition-group>
	  </div>
	  <!-- Carousel controls -->
	  <div v-if="showControls" class="carousel-controls absolute flex justify-between items-center w-full left-0 right-0 top-1/2 transform -translate-y-1/2 px-4 lg:px-10">
		<a href="#" class="btn btn-circle btn-sm" @click.prevent="prevImage">❮</a>
		<a href="#" class="btn btn-circle btn-sm" @click.prevent="nextImage">❯</a>
	  </div>
	</div>
  </template>
  
  
  <script>
  import sitevisit from '@/assets/images/sitevisit.jpeg';
  import sitevisit2 from '@/assets/images/sitevisit2.jpg';
  import sitevisit3 from '@/assets/images/sitevisit3.jpg';
  import sitevisit4 from '@/assets/images/sitevisit4.jpg';
  import sitevisit5 from '@/assets/images/sitevisit5.jpg';
  import sitevisit7 from '@/assets/images/sitevisit7.jpeg';
  
  export default {
	data() {
	  return {
		images: [
		  sitevisit,
		  sitevisit2,
		  sitevisit3,
		  sitevisit4,
		  sitevisit5,
		  sitevisit7,
		],
		currentIndex: 0,
		slideInterval: null,
		showControls: false,
	  };
	},
	mounted() {
	  this.startAutoSlide();
	},
	beforeDestroy() {
	  this.stopAutoSlide();
	},
	methods: {
	  startAutoSlide() {
		this.slideInterval = setInterval(() => {
		  this.nextImage();
		}, 3000);
	  },
	  stopAutoSlide() {
		clearInterval(this.slideInterval);
	  },
	  nextImage() {
		this.currentIndex = (this.currentIndex + 1) % this.images.length;
	  },
	  prevImage() {
		this.currentIndex = (this.currentIndex - 1 + this.images.length) % this.images.length;
	  },
	  beforeEnter(el) {
		el.style.transform = "translateX(100%)";
	  },
	  enter(el, done) {
		el.offsetHeight; // trigger reflow
		el.style.transition = "transform 0.5s ease";
		el.style.transform = "translateX(0)";
		done();
	  },
	  leave(el, done) {
		el.style.transform = "translateX(-100%)";
		done();
	  },
	},
  };
  </script>
  
  <style>
  /* Adjustments for responsive image display */
  .carousel-item img {
	object-fit: contain; /* Ensure the whole image is visible */
	width: 100%; /* Full width of the container */
	max-height: 100vh; /* Max height to ensure it fits in the viewport */
	border-radius: inherit; /* Match the border radius of the carousel */
  }
  
  /* Carousel slide transitions */
  .slide-enter-active, .slide-leave-active {
	transition: transform 0.5s ease;
  }
  .slide-enter, .slide-leave-to {
	transform: translateX(100%);
  }
  </style>
  