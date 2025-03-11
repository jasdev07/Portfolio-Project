<template>
    <div class="form-control w-full">
      <div class="label">
        <span class="label-text text-black text-2xl">{{ label }}</span>
      </div>
      <select :value="modelValue" @input="$emit('update:modelValue', $event.target.value)" class="select select-bordered border-black text-black bg-yellow-100 w-full">
        <option value="" disabled>{{ placeholder }}</option>
        <option value="independent_model">Independent Model</option>
        <option value="deep_neural_network">Deep Neural Network</option>
        <!-- You can add more options here if needed -->
      </select>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      label: {
        type: String,
        required: true,
      },
      modelValue: {
        type: String,
        default: '',
      },
      placeholder: {
        type: String,
        default: 'Select Model Framework',
      },
    },
    emits: ['update:modelValue'],
  };
  </script>
  