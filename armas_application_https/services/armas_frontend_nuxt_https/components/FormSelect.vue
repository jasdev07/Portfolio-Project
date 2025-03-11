<template>
		<div class="form-control w-full max-w-l">
			<label :for="id" class="label">
				<span class="label-text text-black text-2xl">{{ label }}</span>
			</label>
			<select :id="id" :value="modelValue" @change="handleChange" class="select select-bordered border-black text-black bg-yellow-100 w-full">
				<option value="" disabled>{{ placeholder }}</option>
				<option v-for="option in options" :key="option" :value="option">{{ option }}</option>
			</select>
		</div>
	</template>
	
	<script>
	export default {
		props: {
			id: String,
			label: String,
			options: Array,
			modelValue: [String, Number], // Use modelValue for v-model compatibility
			placeholder: String,
		},
		emits: ['update:modelValue'],
		methods: {
			handleChange(event) {
				// Emit the 'update:modelValue' event to update the parent's value
				this.$emit('update:modelValue', event.target.value);
			},
		},
	};
	</script>
	