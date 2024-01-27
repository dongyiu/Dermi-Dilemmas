<template>
    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 flex items-center justify-center z-50">
      <!-- Modal content with max height and responsive centering -->
      <div class="bg-white rounded-lg shadow-lg p-8 max-w-lg w-full max-h-full overflow-auto mx-4 my-8">
        <div class="flex justify-between items-start mb-4">
          <h2 class="text-xl font-semibold">{{ modalData.title }}</h2>
          <button @click="closeModal" class="text-gray-500 hover:text-gray-800">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
            </svg>
          </button>
        </div>
        
        <!-- Image centered above text content -->
        <div class="text-center mb-4">
          <img class="rounded-lg w-64 h-auto mx-auto" :src="modalData.image" alt="Condition Image">
        </div>
        <!-- Scrollable text content with max height -->
        <div class="overflow-auto max-h-60 mb-4">
            <div class="mb-4">
        <p class="text-sm text-gray-600 whitespace-normal">{{ modalData.description }}</p> 
      </div>
          <p class="text-sm text-gray-500 mb-4">Symptoms: {{ modalData.symptoms }}</p>
          <p class="text-sm text-gray-500 mb-4">Severity: {{ modalData.severity }}</p>
          <p class="text-sm text-gray-500 mb-4">Seriousness: {{ modalData.seriousness }}</p>
          <p class="text-sm text-gray-500 mb-4">Treatment: {{ modalData.treatment }}</p>
        </div>
        <button v-if="modalData.nhsLink.length > 1" @click="openNhsLink" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center w-full inline-flex items-center justify-center">
          NHS Link
        </button>
      </div>
    </div>
  </template>
  
  
  
  
  <script>
  export default {
    props: {
      modalData: {
        type: Object,
        required: true,
      },
    },
    methods: {
      closeModal() {
        this.$emit('close'); // Emit close event to close the modal
      },
      openNhsLink() {
        window.open(this.modalData.nhsLink, '_blank');
      },
    },
  };
  </script>
  