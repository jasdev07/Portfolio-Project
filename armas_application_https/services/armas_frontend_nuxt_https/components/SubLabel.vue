<template>
    <div class="flex justify-center">
      <label class="block text-3xl font-bold text-white">{{ label }}</label>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      label: {
        type: String,
        required: true,
      },
    },
  };
  </script>
  