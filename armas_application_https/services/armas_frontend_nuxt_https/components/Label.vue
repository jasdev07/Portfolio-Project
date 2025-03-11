<template>
    <label :for="id" class="label">
        <span class="label-text text-black text-2xl flex items-center justify-center">{{ label }}</span>
    </label>
  </template>
  
  <script>
  export default {
    props: {
      id: {
        type: String,
        required: true
      },
      label: {
        type: String,
        required: true
      }
    }
  };
  </script>
  