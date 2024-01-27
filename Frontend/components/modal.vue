<template>
    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 flex items-center justify-center z-50">
      <!-- Modal content -->
      <div class="bg-white rounded-lg shadow-lg p-8 max-w-lg w-full">
        <div class="flex justify-between items-center mb-4 sortable-item">
          <h2 class="text-xl font-semibold sortable-item">{{ modalData.title }}</h2>
          <button @click="closeModal" class="text-gray-500 hover:text-gray-800">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
            </svg>
          </button>
          
        </div>
        <p class="text-sm text-gray-600 mb-4 sortable-item">{{ modalData.description }}</p> 
        <div class="flex items-center mb-3 sortable-item">
        <img class="rounded-lg w-1/2 h-auto mr-3 sortable-item" :src="modalData.image" alt="Doctor Image">
        <div class="flex flex-col w-1/2 sortable-item">
          <div class="flex flex-col space-y-2 sortable-item">
            <p class="text-sm mb-2 text-gray-500 sortable-item">Symptoms: {{ modalData.symptoms }}</p>
            <p class="text-sm mb-2 text-gray-500 sortable-item">Severity: {{ modalData.severity }}</p>
            <p class="text-sm mb-2 text-gray-500 sortable-item">Seriousness: {{ modalData.seriousness }}</p>
            <p class="text-sm mb-2 text-gray-500 sortable-item">Treatment: {{ modalData.treatment }}</p>
          </div>
        </div>
      </div>
      <button @click="openNhsLink" class="mt-auto text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center flex items-center justify-center w-full inline-flex dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
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
  