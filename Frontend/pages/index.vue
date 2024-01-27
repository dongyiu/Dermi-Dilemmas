<template>
  <div style="background-color: #e6e6cfc8;" class="w-full h-full items-center justify-center bg-white p-2 sortable-item edit-parent-border">
    <main class="editable min-h-screen p-8 sortable-item edit-border" draggable="false" data-sortable-applied="true">
      <!-- Hero Section -->
      <div class="max-w-6xl mx-auto sortable-item">
        <div class="editable text-center text-black-700 py-20 sortable-item" draggable="false">
          <h1 class="editable text-6xl font-bold mb-4 sortable-item" draggable="false">Dermi Dilemmas</h1>
          <p class="editable text-xl mb-10 sortable-item" draggable="false">Detect skin rashes with AI</p>
          <button @click="showUploadModal = true" class="editable px-8 rounded-lg bg-yellow-400 text-gray-800 font-bold p-4 uppercase border-yellow-500 border-t border-b border-r sortable-item mt-16 mb-24">Upload Image</button>
        </div>
        
        <!-- Cards Section -->
        <div class="editable flex flex-wrap justify-center gap-8 mb-20 sortable-item edit-parent-border" draggable="false">
          <div
            v-for="(card, index) in cards"
            :key="index"
            :id="'card' + (index + 1)"
            :class="{
              'glowing-blue-border': selectedCardIndex === index
            }"
            class="editable bg-white rounded-lg shadow-lg p-6 w-80 sortable-item cursor-pointer"
          >
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
            <a class="text-blue-500 hover:text-blue-600 transition-colors sortable-item">Read more</a>
          </div>
        </div>
      </div>
    </main>
    <Alert :show="showAlert" :message="message" :type="alertType" />

    <!-- Upload Modal -->
    <upload v-if="showUploadModal" @close="showUploadModal = false" @attach="showAttach"/>
  </div>
</template>

<script>
export default {
  data() {
    return {
      alertType: 'success',
      showUploadModal: false,
      showAlert: false,
      message: '',
      cards: [
        { title: 'Abc', image: 'https://source.unsplash.com/random/80x80', name: 'Jackson Bennet', date: 'Apr 25, 2021', description: 'Great place would highly recommend for anyone wanting high value.' },
        { title: 'Abc', image: 'https://source.unsplash.com/random/80x80', name: 'Jackson Bennet', date: 'Apr 25, 2021', description: 'Great place would highly recommend for anyone wanting high value.' },
        { title: 'Abc', image: 'https://source.unsplash.com/random/80x80', name: 'Jackson Bennet', date: 'Apr 25, 2021', description: 'Great place would highly recommend for anyone wanting high value.' },
        { title: 'Abc', image: 'https://source.unsplash.com/random/80x80', name: 'Jackson Bennet', date: 'Apr 25, 2021', description: 'Great place would highly recommend for anyone wanting high value.' },
        { title: 'Abc', image: 'https://source.unsplash.com/random/80x80', name: 'Jackson Bennet', date: 'Apr 25, 2021', description: 'Great place would highly recommend for anyone wanting high value.' },
        // Add more card objects here
      ],
      selectedCardIndex: -1 // Initialize selected card index to -1 (none selected by default)
    };
  },
  methods: {
    showAttach(files) {
      this.alertType = 'alert';
      this.showUploadModal = false;
      this.message = `You are not healthy!`;
      this.showAlert = true;
      this.selectedCardIndex = 2;
      // Optionally, scroll to the selected card
      this.scrollToCard(this.selectedCardIndex);
    },
    scrollToCard(index) {
      const cardId = `card${index + 1}`;
      const element = document.getElementById(cardId);
      if (element) {
        element.scrollIntoView({ behavior: 'smooth' });
      }
    }
  }
}
</script>

<style>
/* Add a glowing blue border to the selected card */
.glowing-blue-border {
  border: 2px solid #db3442; /* Blue border color */
  box-shadow: 0 0 10px #db345e; /* Blue box shadow */
}
</style>
