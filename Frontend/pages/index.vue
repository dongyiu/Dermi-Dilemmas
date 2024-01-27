<template>
  <div style="background-color: #e6e6cfc8;" class="w-full h-full items-center justify-center bg-white p-2 sortable-item edit-parent-border">
    <main class="editable min-h-screen p-8 sortable-item edit-border" draggable="false"  data-sortable-applied="true">
      <!-- Hero Section -->
      <div class="max-w-6xl mx-auto sortable-item">
        <div class="editable text-center text-black-700 py-20 sortable-item" draggable="false">
          <h1 class="editable text-6xl font-bold mb-4 sortable-item" draggable="false">Dermi Dilemmas</h1>
          <p class="editable text-xl mb-10 sortable-item" draggable="false">Detect skin rashes with AI</p>
          <button @click="showUploadModal = true" class="editable px-8 rounded-lg bg-yellow-400 text-gray-800 font-bold p-4 uppercase border-yellow-500 border-t border-b border-r sortable-item mt-16 mb-24">Upload Image</button>
        </div>
        
        <!-- Cards Section -->
        <div class="editable flex flex-wrap justify-center gap-8 mb-20 sortable-item edit-parent-border" draggable="false">
          <div v-for="(card, index) in cards" :key="index" class="editable bg-white rounded-lg shadow-lg p-6 w-80 sortable-item">
            <div class="flex justify-between items-center mb-6 sortable-item">
              <div class="sortable-item edit-parent-border">
                <p class="editable text-gray-900 text-lg font-semibold sortable-item edit-border">{{ card.title }}</p>
              </div>
            </div>
            <div class="flex items-center space-x-4 mb-6 sortable-item">
              <img :src="card.image" alt="profile" class="rounded-full sortable-item" draggable="false">
              <div class="sortable-item">
                <p class="text-gray-900 text-sm font-semibold sortable-item">{{ card.name }}</p>
                <p class="text-gray-600 text-xs sortable-item">{{ card.date }}</p>
                <p class="text-gray-600 text-xs sortable-item">{{ card.description }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>

    <!-- Upload Modal -->
    <upload v-if="showUploadModal" @close="showUploadModal = false"/>
  </div>
</template>

<script>

export default {
  data() {
    return {
      showUploadModal: false,
      cards: [
        { title: 'Abc', image: 'https://source.unsplash.com/random/80x80', name: 'Jackson Bennet', date: 'Apr 25, 2021', description: 'Great place would highly recommend for anyone wanting high value.' },
        // Add more card objects here
      ]
    };
  }
}
</script>

<style>
/* Add your styles here */
</style>
