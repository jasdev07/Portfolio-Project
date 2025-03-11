
  

	<template>
		<button
			:class="[
				'flex items-center justify-center rounded-full py-2 px-12 text-2xl shadow-2xl',
				'border-2 border-black',
				loading ? 'bg-black text-yellow-500 hover:bg-yellow-500 hover:text-black' : 'bg-yellow-500 text-black hover:bg-black hover:text-yellow-500',
				buttonClass
			]"			
			@click="handleClick"
			:disabled="loading">
			<div v-if="loading" role="status">
				<span class="visually-hidden loading loading-spinner loading-md bg-black"></span>

			</div>
			<span v-else>
				{{ buttonText }}
			</span>
		</button>
	</template>
	
	
  <script>
  export default {
    props: {
      buttonText: {
        type: String,
        required: true,
      },
      buttonClass: {
        type: String,
        default: 'default-button-class',
      },
      to: {
        type: String,
        default: null,
      },
      emitEvent: {
        type: String,
        default: null,
      },
      clearData: {
        type: Boolean,
        default: false,
      },
			loading: { // New prop to control the display of the preloader
      type: Boolean,
      default: false,
    },
      // Other props for backend data etc.
    },
    methods: {
      handleClick() {
        if (this.to) {
          // Logic for routing
          this.$router.push(this.to);
					this.$emit('click');

        }
      },
    },
  };
  </script>



  