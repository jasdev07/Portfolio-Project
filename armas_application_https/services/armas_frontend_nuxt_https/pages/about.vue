<template>
		<div>
			<Navbar :links="[{ name: 'Dashboard', href: '/dashboard' }, { name: 'Home', href: '/' }, { name: 'About Us', href: '/about' }]" />
			<div class="mt-7 video-container" style="position: relative; padding-left: 2.5%; padding-right: 2.5%; overflow: hidden; border-radius: 20px;">
					<div style="position: absolute; top: 0; left: 2.5%; right: 2.5%; width: 95%; height: 100%; background: rgba(0, 0, 0, 0.5); border-radius: 20px;"></div>
					<video autoplay muted loop class="video-background" style="width: 100%; height: auto; z-index: -1; border-radius: 20px;">
							<source src="@/assets/video/banner_video.mp4" type="video/mp4">
							Your browser does not support the video tag.
					</video>
					<div class="overlay-content" style="position: absolute; top: 0; left: 2.5%; right: 2.5%; display: flex; flex-direction: column; align-items: center; justify-content: center; z-index: 1; width: 95%; height: 100%;">
						<div class="absolute inset-0 flex flex-col items-center justify-center p-5">
							<h1 class="text-yellow-400 text-4xl sm:text-5xl md:text-6xl font-extrabold text-center">About Us</h1>
							<p class="text-yellow-400 text-lg sm:text-xl md:text-2xl font-extrabold text-center">
								Develop an <span class="font-extrabold">Automated Repossessed Motorcycle Assessment System (ARMAS)</span> using state-of-the-art methodologies and frameworks in the fields of <span class="font-extrabold">Artificial Intelligence</span> and <span class="font-extrabold">Machine Learning</span> by leveraging on Unistar’s dataset.
							</p>
						</div>
					</div>
			</div>

			<div :style="{ paddingLeft: '5%', paddingRight: '5%' }" class="mt-20">
				<div class="mt-20 flex ">
						<div class="flex flex-col lg:flex-row mb-4">
							<div class="lg:w-1/2 lg:mr-2 flex-grow">
							<p class="mb-1 text-base lg:text-2xl text-black px-4 lg:px-10 dark:text-black">
								<span class="font-bold">Unistar ARMAS</span> is a project granted under the Department of Science and Technology's (DOST) Collaborative Research and Development to Leverage Philippine Economy (CRADLE) Programme. It is a partnership between the Analytics, Computing and Complex Systems Laboratory of the Asian Institute of Management (ACCeSs@AIM) and Unistar Credit and Finance Corp, a local credit and financing institution for the motorcycle market. The project proposes to develop an AI-based decision support tool for streamlining asset recovery operations of Unistar. ARMAS is envisioned to be integrated with Unistar's daily business process as its main tool for motorcycle segmentation and automated evaluation, minimizing the costs for manual labor and other sources of manmade error through accurate data-driven predictions.
							</p>
							<!-- Carousel only visible on mobile -->
							<div class="lg:hidden">
								<Carousel />
							</div>
							</div>
							<!-- Carousel only visible on larger screens -->
							<div class="hidden lg:block lg:w-1/2">
							<Carousel />
							</div>
						</div>
					</div>
				<div>

					<div>
						<div class="target" v-motion :initial="{opacity: 0, y:100}" :visible="{ opacity:1, y:0 }" :delay="200" style="display: flex; justify-content: center; align-items: center;">
							<h2 class="mb-8 lg:mb-16 text-3xl font-extrabold tracking-tight leading-tight text-center text-[#333333]-900 dark:text-[#333333] md:text-4xl">Project Overview</h2>
						</div>
						<div class="target" v-motion :initial="{opacity: 0, y:100}" :visible="{ opacity:1, y:0 }" :delay="200" style="display: flex; justify-content: center; align-items: center;">
							<video class="border border-gray-700 rounded-lg dark:border-gray-700 video-fade-in" controls style="max-width: 100%; height: auto;">
								<source src="@/assets/video/ARMAS_video.mp4" type="video/mp4">
								Your browser does not support the video tag.
							</video>
						</div>
					</div>
				


					<div class="mt-20">
						<div class="mt-7 video-container" style="position: relative; padding-left: 5%; padding-right: 5%; overflow: hidden; border-radius: 20px;">
						<div class="target" v-motion :initial="{opacity: 0, y:100}" :visible="{ opacity:1, y:0 }">
							<div class="mt-30 flex justify-center items-center relative">
								<h1 class="mb-2 text-4xl font-extrabold tracking-tight leading-none text-[#333333] md:text-5xl lg:text-6xl dark:text-[#333333]">Our Team</h1>
							</div>
							<div>
								<div class="mt-5 relative">
									<img src="@/assets/images/contributor1.png" alt="UNISTAR-ARMAS Logo"/>
								</div>
							</div>
						</div>
						</div>
					</div>
				</div>
			</div>
			
			<div class="mt-10">
				<section :style="{ background: 'linear-gradient(to bottom, #FFC000, #333333)' }">
					<div class="py-8 lg:py-16 mx-auto max-w-screen-xl px-4">
						<h2 class="mb-8 lg:mb-16 text-3xl font-extrabold tracking-tight leading-tight text-center text-[#333333]-900 dark:text-[#333333] md:text-4xl">Collaborators</h2>
						<div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-3 gap-5 sm:gap-9">
							<div class="flex-grow floating-effect">
								<img src="@/assets/images/unistar.png" alt="UNISTAR-ARMAS Logo" class="h-25 w-65 mx-auto" />
							</div>
							<div class="flex-grow floating-effect">
								<img src="@/assets/images/dost.png" alt="UNISTAR-ARMAS Logo" class="h-33 w-20 mx-auto" />
							</div>
							<div class="flex-grow floating-effect">
								<img src="@/assets/images/access.png" alt="UNISTAR-ARMAS Logo" class="h-35 w-90 mx-auto" />
							</div>
						</div>
					</div>
				</section>
			</div>
			<footer class="bg-[#333333] dark:bg-[#333333]-900">
				<div class="w-full max-w-screen-xl mx-auto p-4 md:py-8">
					<div class="sm:flex sm:items-center sm:justify-between">
					<a class="flex items-center mb-4 sm:mb-0">
						<img src="@/assets/images/armas.png" class="h-8 mr-3" alt="Flowbite Logo" />
						<span class="self-center text-2xl font-semibold whitespace-nowrap dark:text-white">Unistar Armas</span>
					</a>
					<ul class="flex flex-wrap items-center mb-6 text-sm font-medium text-gray-500 sm:mb-0 dark:text-gray-400">
						<li>
						<a href="#" class="mr-4 hover:underline md:mr-6 ">About</a>
						</li>
						<li>
						<a href="#" class="mr-4 hover:underline md:mr-6">Privacy Policy</a>
						</li>
						<li>
						<a href="#" class="mr-4 hover:underline md:mr-6 ">Licensing</a>
						</li>
						<li>
						<a href="#" class="hover:underline">Contact</a>
						</li>
					</ul>
					</div>
					<hr class="my-6 border-gray-200 sm:mx-auto dark:border-gray-700 lg:my-8" />
					<span class="block text-sm text-gray-500 sm:text-center dark:text-gray-400">© 2023 <a href="" class="hover:underline">Unistar ARMAS</a>. All Rights Reserved.</span>
				</div>
			</footer>	

					
		</div>
	</template>
	
	<script>
		import Carousel from '@/components/Carousel.vue';

		export default {
		components: {
			Carousel,
		},
		};
	</script>