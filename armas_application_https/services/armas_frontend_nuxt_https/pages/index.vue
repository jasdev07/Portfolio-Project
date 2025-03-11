<template>
	<transition name="fade-slide">
			<div class="px-10%">
				<div :style="{ padding: '0 10%', background: 'linear-gradient(to right, #282524 50%, #e5e9ec 50%)' }">
					<div class="flex flex-row lg:flex-row justify-between mb-10">
							<h1 class="mt-5 header-text fadeInLeft text-4xl font-extrabold tracking-tight leading-none text-white md:text-5xl lg:text-6xl">
								Unistar Armas
							</h1>
							<div class=" mt-4 flex flex-col items-center md:flex-row md:justify-between md:items-end">
								<div class="flex flex-row justify-center space-x-4">
									<!-- Unistar Logo -->
									<img src="@/assets/images/unistar.png" alt="UNISTAR-ARMAS Logo" class="h-14 md:h-14 md:mt-0" />
									<!-- DOST Logo -->
									<img src="@/assets/images/dost.png" alt="DOST Logo" class=" h-14 md:h-14 md:mt-0" />
								</div>
								<!-- ACCESS Logo -->
								<img src="@/assets/images/access.png" alt="ACCESS Logo" class="mt-4 ml-4 md:ml-4 h-10 md:h-14 md:mt-0" />
							</div>
					</div>
					<transition name="fade-slide">
						<div class="card w-auto h-99 bg-stone-800 ">
							<figure><img src="@/assets/images/banner7.png" alt="car!"/></figure>
							<div class="card-body">
								<div :style="{ paddingLeft: '5%', paddingRight: '5%' }">
									<div class="flex flex-col sm:flex-row space-y-4 sm:space-y-0 sm:space-x-4 justify-start">
									
										<FlexibleButton buttonText="Get Started" buttonClass="navigate-class" actionType="route" to="/dashboard" />
										<FlexibleButton buttonText="Learn More" buttonClass="navigate-class" actionType="route" to="/about" />

									</div>
								</div>
							</div>
						</div>
					</transition>
				</div>

				<footer class="footer footer-center p-10 bg-stone-800 text-white">
					<aside>
						<img src="@/assets/images/armas.png" alt="Logo" class="mt-5 h-8 mr-2">
						<span class="text-xl text-white">Unistar Armas</span>
				
						<nav class="mt-5 grid grid-flow-col gap-8">
							<NuxtLink to="/about" class="flex items-center justify-self-start">
								<a class="link link-hover">About us</a>
							</NuxtLink>
							<NuxtLink to="/about" class="flex items-center justify-self-start">
								<a class="link link-hover">Contact</a>
							</NuxtLink>
						</nav>
						<p>Copyright © 2024 - All right reserved</p>
					</aside> 
					<nav>
						<div class="grid grid-flow-col gap-4">
							<a><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" class="fill-current"><path d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z"></path></svg></a>
							<a><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" class="fill-current"><path d="M19.615 3.184c-3.604-.246-11.631-.245-15.23 0-3.897.266-4.356 2.62-4.385 8.816.029 6.185.484 8.549 4.385 8.816 3.6.245 11.626.246 15.23 0 3.897-.266 4.356-2.62 4.385-8.816-.029-6.185-.484-8.549-4.385-8.816zm-10.615 12.816v-8l8 3.993-8 4.007z"></path></svg></a>
							<a><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" class="fill-current"><path d="M9 8h-3v4h3v12h5v-12h3.642l.358-4h-4v-1.667c0-.955.192-1.333 1.115-1.333h2.885v-5h-3.808c-3.596 0-5.192 1.583-5.192 4.615v3.385z"></path></svg></a>
						</div>
					</nav>
				</footer>
				</div>
			</transition>

</template>