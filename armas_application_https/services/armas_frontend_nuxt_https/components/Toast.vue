<template>
	<transition name="fade">
		<div v-if="visible" class="fixed top-5 right-5 z-50">
			<div :class="['alert', toastClass, typeClass]">
				<div class="alert-content">
					<img v-if="type === 'error'" src="@/assets/icon/warning.png" alt="Warning" class="icon" />
					<span>{{ message }}</span>
				</div>
				<button @click="hideToast" class="close-btn ml-2">✕</button>
			</div>
		</div>
	</transition>
</template>

<script>
export default {
	props: {
		message: String,
		type: {
			type: String,
			default: 'info' // 'info', 'error', etc.
		},
	},
	data() {
		return {
			visible: false,
			toastTimeout: null,
		};
	},
	computed: {
		toastClass() {
			let baseClass = 'px-6 py-4 border-l-4 rounded shadow-lg flex items-center';
			switch (this.type) {
				case 'info':
					return `${baseClass} bg-blue-100 text-blue-800 border-blue-500`; // Example for 'info' type
				case 'error':
					return `${baseClass} bg-red-100 text-red-800 border-red-500`; // Example for 'error' type
				case 'success':
					return `${baseClass} bg-green-100 text-green-800 border-green-500`; // Example for 'success' type
				default:
					return `${baseClass} bg-white text-black`; // Default or 'info' class
			}
		},
		typeClass() {
			switch (this.type) {
			case 'info':
				return 'info-class'; // Replace with your actual class
			case 'error':
				return 'error-class'; // Replace with your actual class
			// Add other cases for different types if needed
			default:
				return '';
			}
		},
	},
	methods: {
		showToast() {
			this.visible = true;
			this.clearToastTimeout();
			this.toastTimeout = setTimeout(() => {
				this.visible = false;
			}, 3000); // Hide after 3 seconds
		},
		hideToast() {
			this.visible = false;
			this.clearToastTimeout();
		},
		clearToastTimeout() {
			if (this.toastTimeout) {
				clearTimeout(this.toastTimeout);
				this.toastTimeout = null;
			}
		}
	},
};
</script>

<style scoped>
/* Your fade transition and other styles */
.fade-enter-active, .fade-leave-active {
	transition: opacity 0.5s;
}
.fade-enter-from, .fade-leave-to {
	opacity: 0;
}

.close-btn {
	background-color: transparent; /* or any color you want */
	border: none;
	padding: 0.5rem;
	cursor: pointer;
	font-size: 1.25rem; /* Adjust size as needed */
	color: #000; /* Adjust close button color as needed */
}
</style>
