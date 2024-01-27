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
                <!-- <p class="text-gray-900 text-sm font-semibold sortable-item">{{ card.name }}</p> -->
                <!-- <p class="text-gray-600 text-xs sortable-item">{{ card.date }}</p> -->
                <p class="text-gray-600 text-sm sortable-item">{{ card.description }}</p>
                <a @click="openModal(card)" class="text-base text-blue-500 hover:text-blue-600 transition-colors sortable-item">Read more</a>

              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
    <Alert :show="showAlert" :message="message" :type="alertType" />
    <Modal v-if="showModal" :modalData="modalData" @close="closeModal" />
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
      showModal: false,
      modalData: {
          title: 'Abc Dermatology', 
          image: 'https://source.unsplash.com/random/80x80', 
          name: 'Dr. Jackson Bennet', 
          date: 'Apr 25, 2021', 
          description: 'Specializing in skin care and dermatological treatments.',
          symptoms: 'Fever, Rash',
          severity: 'Moderate',
          seriousness: 'Low',
          treatment: 'Rest and hydration',
          nhsLink: 'https://www.nhs.uk/' 
      },
      cards: [
        { 
          title: 'Abc Dermatology', 
          image: 'https://source.unsplash.com/random/80x80', 
          name: 'Dr. Jackson Bennet', 
          date: 'Apr 25, 2021', 
          description: 'Specializing in skin care and dermatological treatments.',
          symptoms: 'Fever, Rash',
          severity: 'Moderate',
          seriousness: 'Low',
          treatment: 'Rest and hydration',
          nhsLink: 'https://www.nhs.uk/' 
        },
        { 
          title: 'Skin Health Clinic', 
          image: 'https://source.unsplash.com/random/80x80', 
          name: 'Dr. Emily Johnson', 
          date: 'Apr 30, 2021', 
          description: 'Promoting skin health and well-being.',
          symptoms: 'Pain, Discomfort',
          severity: 'Mild',
          seriousness: 'Low',
          treatment: 'Pain relievers',
          nhsLink: 'https://www.nhs.uk/' 
        },
        { 
          title: 'Dermatology Solutions', 
          image: 'https://source.unsplash.com/random/80x80', 
          name: 'Dr. Sarah Adams', 
          date: 'May 15, 2021', 
          description: 'Committed to providing advanced dermatological care.',
          symptoms: 'Itching, Redness',
          severity: 'Severe',
          seriousness: 'Moderate',
          treatment: 'Prescription medication',
          nhsLink: 'https://www.nhs.uk/' 
        },
        { 
          title: 'Skin Care Center', 
          image: 'https://source.unsplash.com/random/80x80', 
          name: 'Dr. James Smith', 
          date: 'Jun 5, 2021', 
          description: 'Your trusted partner for healthy skin.',
          symptoms: 'Swelling, Dryness',
          severity: 'Mild',
          seriousness: 'Low',
          treatment: 'Moisturizers and anti-inflammatory creams',
          nhsLink: 'https://www.nhs.uk/' 
        },
        { 
          title: 'Healthy Skin Clinic', 
          image: 'https://source.unsplash.com/random/80x80', 
          name: 'Dr. Laura Wilson', 
          date: 'Jun 20, 2021', 
          description: 'Where beautiful skin begins.',
          symptoms: 'Flaking, Allergic Reaction',
          severity: 'Moderate',
          seriousness: 'Moderate',
          treatment: 'Topical ointments and allergy management',
          nhsLink: 'https://www.nhs.uk/' 
        },
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
        setTimeout(() => {
          this.showAlert = false;
        }, 6000);
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
    },
    openModal(card) {
      this.modalData = card;
      this.showModal = true;
    },
    closeModal() {
      this.showModal = false;
    },
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
