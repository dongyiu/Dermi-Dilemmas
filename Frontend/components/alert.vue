<template>
    <div v-if="show" :class="alertClasses">
      {{ message }}
    </div>
  </template>
  
  <script>
  export default {
    props: {
      show: Boolean,
      message: String,
      type: String // Add a type prop to specify the alert type (e.g., 'info' or 'alert')
    },
    computed: {
      alertClasses() {
        // Define CSS classes based on the type prop
        return {
          'fixed top-0 left-1/2 transform -translate-x-1/2 mt-4 text-white text-center font-semibold py-2 px-4 rounded-md': true,
          'bg-red-600': this.type === 'alert',
          'bg-blue-600': this.type === 'info',
          'bg-green-600': this.type === 'success',
        };
      }
    }
  }
  </script>