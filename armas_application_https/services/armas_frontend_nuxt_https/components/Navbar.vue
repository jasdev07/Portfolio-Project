<template>
		<div v-if="shouldShowNavbar" class="navbar bg-stone-800 w-full">
			<div class="container mx-auto px-4 lg:px-8 flex justify-between items-center">
				<!-- Logo on the left -->
				<div class="flex items-center">
					<NuxtLink to="/" class="flex items-center">
						<img src="@/assets/images/armas.png" alt="Logo" class="h-8 mr-2">
						<span class="text-xl text-white">Unistar Armas</span>
					</NuxtLink>
				</div>
				
				<!-- Hamburger Icon for mobile -->
				<button class="lg:hidden p-2" @click="toggleMobileMenu">
						<!-- Here you can add an icon or just use text like 'Menu' -->
						<svg class="h-6 w-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
						<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7" />
						</svg>
				</button>
	
				<!-- Links for large screens -->
				<div class="hidden lg:flex items-center space-x-4">
					<NuxtLink to="/" class="btn btn-ghost text-white">Homepage</NuxtLink>
					<NuxtLink to="/dashboard" class="btn btn-ghost text-white">Dashboard</NuxtLink>
					<NuxtLink to="/about" class="btn btn-ghost text-white">About Us</NuxtLink>
					<!-- <details class="dropdown dropdown-end ml-2">
						<summary class="btn btn-ghost text-white">LOG IN</summary>
						<ul class="menu dropdown-content p-2 shadow bg-stone-800 rounded-box w-52">
							<li><NuxtLink to="/login">Sign In</NuxtLink></li>
							<li><NuxtLink to="/signup">Sign Up</NuxtLink></li>
						</ul>
					</details> -->
				</div>
			</div>

			<!-- Mobile menu content -->
				<div 
						v-show="isMobileMenuOpen" 
						class="lg:hidden"
						:class="{ 'translate-x-0': isMobileMenuOpen, '-translate-x-full': !isMobileMenuOpen }"
						@click.self="isMobileMenuOpen = false"
				>
						<ul class="p-2 transition transform duration-300 ease-in-out">
						<!-- Navigation links -->
								<li><NuxtLink to="/">Homepage</NuxtLink></li>
								<li><NuxtLink to="/dashboard">Dashboard</NuxtLink></li>
								<li><NuxtLink to="/about">About Us</NuxtLink></li>
						</ul>
				</div>
		</div>
	</template>
	
	<script>
	import { ref, computed, defineComponent } from 'vue';
	import { useRoute } from 'vue-router';
	
	export default defineComponent({
		setup() {
			const route = useRoute();
			const shouldShowNavbar = computed(() => route.path !== '/armas');
			const isMobileMenuOpen = ref(false);
	
			function toggleMobileMenu() {
				isMobileMenuOpen.value = !isMobileMenuOpen.value;
			}
	
			return { shouldShowNavbar, isMobileMenuOpen, toggleMobileMenu };
		},
	});
	</script>
	
	<style>
	/* Additional styles for the transition */
	.navbar ul {
		transition: transform 0.3s ease-in-out;
	}
	
	/* Position the mobile menu off-screen initially */
	.navbar ul.translate-x-full {
		transform: translateX(-100%);
	}
	
	/* Reset the position when the menu is open */
	.navbar ul.translate-x-0 {
		transform: translateX(0);
	}
	</style>
	