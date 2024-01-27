<template>
<div style="background: linear-gradient(to bottom right, #c8017e, #0c0e3f);" class="w-full h-full items-center justify-center bg-white p-2 sortable-item edit-parent-border">
    <main class="editable min-h-screen p-8 sortable-item edit-border" draggable="false" data-sortable-applied="true">
      <!-- Hero Section -->
      <div class="max-w-6xl mx-auto sortable-item">
        <div class="w-full md:w-2/3 mx-auto py-12">
          <div class="px-10">
            <div class="editable text-center text-black-700 py-5 sortable-item rounded-lg bg-white shadow-lg">
              <h1 class="editable text-6xl font-bold sortable-item" draggable="false">Dermi-Dilemmas</h1>
              <p class="editable text-xl mb-5 sortable-item" draggable="false">Detect skin rashes with AI</p>
              <p class="editable text-sm mb-10 sortable-item" draggable="false">Disclaimer: Please consult a medical professional for a proper diagnosis.</p>
              <button @click="showUploadModal = true" class="editable px-8 rounded-lg bg-yellow-400 text-gray-800 font-bold p-4 border-yellow-500 border-t border-b border-r sortable-item my-10">Upload Image</button>
            </div>
          </div>
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
              <img :src="card.image" alt="condition image" class="rounded-full w-16 h-16 object-cover sortable-item" draggable="false">
              <div class="sortable-item">
                <!-- <p class="text-gray-900 text-sm font-semibold sortable-item">{{ card.name }}</p> -->
                <!-- <p class="text-gray-600 text-xs sortable-item">{{ card.date }}</p> -->
                <p class="text-gray-600 text-sm sortable-item">
                  {{ card.description.length < 100 ? card.description : card.description.slice(0, 100) + '...' }}
                </p>
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
const THRESHOLD = 0.5; // Threshold for confidence score
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
    title: 'Actinic Keratosis', 
    image: '/0.png',
    description: 'A precancerous skin condition caused by long-term exposure to ultraviolet (UV) radiation primarily from the sun, appearing as rough scaly patches on the skin.',
    symptoms: 'Rough scaly patches on sun-exposed areas like face, lips, ears, scalp, hands, or arms. Patches may be red, pink, brown, or flesh-colored. Some AKs may itch or feel tender.',
    severity: 'Considered precancerous but not cancerous themselves. While most remain as mild patches, a small percentage can develop into squamous cell carcinoma (SCC) if left untreated.',
    seriousness: 'Early diagnosis and treatment of AKs are crucial to prevent progression to SCC. Untreated SCC can grow deeper into the skin and potentially spread to other parts of the body.',
    treatment: 'Topical creams or gels containing retinoids, imiquimod, or fluorouracil. Cryotherapy (freezing) or cauterization (burning) of lesions. Laser therapy in some cases.',
    nhsLink: 'https://www.newcastle-hospitals.nhs.uk/services/dermatology/patient-dermatology-information-leaflets/actinic-keratosis-also-known-as-solar-keratosis/' 
  },
  { 
    title: 'Atopic Dermatitis', 
    image: '/1.png',
    description: 'A chronic inflammatory skin condition that causes dry, itchy, and inflamed patches. It typically affects children and tends to improve with age.',
    symptoms: 'Dry itchy skin, red inflamed patches, small fluid-filled bumps, thickened scaly skin.',
    severity: 'Can range from mild to severe with persistent itching, redness, and inflammation.',
    seriousness: 'Significantly impacts quality of life with sleep disturbance and potential for skin infections.',
    treatment: 'Emollients, topical corticosteroids, antihistamines, phototherapy, lifestyle changes.',
    nhsLink: 'https://www.nhs.uk/conditions/atopic-eczema/' 
  },
  { 
    title: 'Benign Keratosis', 
    image: '/2.png',
    description: 'Also known as seborrheic keratosis or senile wart, it is a harmless skin growth that commonly appears with age.',
    symptoms: 'Rough wart-like bumps, color variations, size variations, and typically no pain or discomfort.',
    seriousness: 'Not medically serious but can sometimes be mistaken for other skin conditions like skin cancer.',
    treatment: 'Observation, topical creams, cryotherapy, electrocautery, or laser therapy.',
    nhsLink: '' // No specific NHS link provided in the text
  },
  { 
    title: 'Dermatofibroma', 
    image: '/3.png',
    description: 'A common benign skin growth composed of fibrous tissue, typically painless and requires no treatment.',
    symptoms: 'Firm small bump, color variation, dimpling sign, and usually painless.',
    seriousness: 'Not medically serious but can cause anxiety or concerns about appearance.',
    treatment: 'Observation, topical treatments, injections, or surgical removal for cosmetic reasons.',
    nhsLink: '' // No specific NHS link provided in the text
  },
  { 
    title: 'Melanocytic Nevi', 
    image: '/4.png',
    description: 'Benign collections of melanocytes, appearing as raised or flat pigmented spots on the skin.',
    symptoms: 'Variations in appearance, location, and growth.',
    seriousness: 'Not considered a disease but some can develop into melanoma.',
    treatment: 'Most require no treatment unless they cause discomfort or cosmetic concerns.',
    nhsLink: 'https://www.nhs.uk/conditions/moles/'
  },
  { 
    title: 'Melanoma', 
    image: '/5.png',
    description: 'The most serious type of skin cancer developing from melanocytes.',
    symptoms: 'Changes in existing moles, new unusual moles, darkening of existing freckles, or bleeding without obvious cause.',
    seriousness: 'The most dangerous form of skin cancer due to its ability to spread quickly.',
    treatment: 'Surgery, radiotherapy, immunotherapy, targeted therapy.',
    nhsLink: 'https://www.nhs.uk/conditions/melanoma-skin-cancer/'
  },
  {
  title: 'Squamous Cell Carcinoma',
  image: '/6.png',
  description: 'Squamous cell carcinoma is a type of skin cancer that develops in squamous cells. It often appears on sun-exposed areas like the face, ears, and hands.',
  symptoms: 'Rough scaly patches, open sores that do not heal, elevated growths with a central depression, changes in existing moles.',
  severity: 'Can range from mild to severe, with advanced cases potentially spreading to other parts of the body.',
  seriousness: 'Early detection and treatment are critical. Large or neglected SCCs can lead to disfigurement, infection, or spread to other organs.',
  treatment: 'Treatment options include surgical excision, cryotherapy, electrodesiccation, Mohs surgery, and radiotherapy.',
  nhsLink: 'https://www.nhs.uk/conditions/non-melanoma-skin-cancer/'
},
{
  title: 'Tinea Ringworm Candidiasis',
  image: '/7.png',
  description: 'Tinea and ringworm refer to fungal infections of the skin, while candidiasis is caused by an overgrowth of Candida yeast.',
  symptoms: 'For Tinea/Ringworm: Red, itchy, circular patches with raised borders. For Candidiasis: Red, itchy patches with white discharge, cracks in the skin.',
  severity: 'Symptoms range from mild to severe, potentially leading to more extensive infections.',
  seriousness: 'While not life-threatening, they can cause significant discomfort and affect quality of life. Can spread and lead to secondary infections if untreated.',
  treatment: 'Antifungal creams, lotions, or tablets, depending on the severity and location of the infection.',
  nhsLink: 'https://www.nhs.uk/conditions/athletes-foot/' // Athlete's foot is a common tinea infection.
},
{
  title: 'Vascular Lesion',
  image: '/9.png',
  description: 'Vascular lesions are abnormalities in blood vessels, presenting in various forms like hemangiomas, vascular malformations, and spider angiomas.',
  symptoms: 'They can appear as flat or raised patches, bumps, lumps, or spider-like patterns, in red, purple, blue, or flesh colors. Some can cause discomfort or bleeding.',
  seriousness: 'Some lesions are painless and pose no health risks, while others can affect organ function or lead to complications.',
  treatment: 'Treatment varies and may include observation, topical medications, laser therapy, or surgery depending on the type and severity of the lesion.',
  nhsLink: '' // No specific NHS link provided in the text; a suitable link should be found.
}
],
      selectedCardIndex: -1 // Initialize selected card index to -1 (none selected by default)
    };
  },
  methods: {
    showAttach(files, confidence) {
      this.selectedCardIndex = -1;
      if (files == undefined || isNaN(files) || !Number.isInteger(Number(files))) {
        this.alertType = 'alert';
        this.message = "Error uploading file. Please try again."
      }
      else if (confidence < THRESHOLD) {
        this.alertType = 'success';
        this.message = "No skin condition detected."
      }
      else {
        this.alertType = 'alert';
        this.message = `Skin condition detected!`;
        this.selectedCardIndex = Number(files);
      }
      
      this.showUploadModal = false;
      // this.message = `You are not healthy!`;
      this.showAlert = true;
        setTimeout(() => {
          this.showAlert = false;
        }, 6000);
      // this.selectedCardIndex = 2;
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
