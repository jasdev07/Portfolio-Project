	<template>
		<div class="form-control w-full max-w-l">
			<div class="label">
				<span class="label-text text-black text-2xl">{{ label }}</span>
			</div>
			<div class="relative">
				<div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
					<img src="@/assets/icon/calendar.png" alt="Icon" class="w-5 h-5" />      
				</div>
				<!-- Replace v-model with :value and @input -->
				<input :id="id" 
							type="date" 
							:value="modelValue" 
							@input="$emit('update:modelValue', $event.target.value)" 
							class="input bg-yellow-100 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring focus:ring-blue-500 block w-full pl-10 p-2.5 dark:bg-yellow-100 dark:border-gray-600 dark:placeholder-gray-400 dark:text-black" 
							:placeholder="placeholder" />
			</div>
		</div>
	</template>

	<script>

	export default {
		props: {
			id: String,
			label: String,
			iconSrc: String,
			modelValue: String, // Received the current value
			placeholder: String,
		},
		emits: ['update:modelValue'], // Emits an event to update the modelValue
	};
	</script>
