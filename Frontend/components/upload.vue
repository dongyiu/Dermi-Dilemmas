<template>
    <!-- Modal Background -->
    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 flex items-center justify-center z-50">
      <!-- Modal Content -->
      <div class="bg-white rounded-lg shadow-lg p-8 max-w-lg w-full">
        <!-- Modal Header -->
        <div class="flex justify-between items-center pb-5 border-b border-gray-200">
          <h1 class="text-2xl font-semibold">Upload and attach files</h1>
          <button @click="$emit('close')" class="text-gray-500 hover:text-gray-800">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
            </svg>
          </button>
        </div>
  
        <!-- Modal Body -->
        <div class="py-6">
          <div @click="triggerFileUpload" class="flex justify-center items-center w-full">
            <div class="flex flex-col items-center justify-center w-full border-2 border-dashed border-gray-300 rounded-lg p-6 cursor-pointer">
              <p class="text-gray-500">Click to upload</p>
              <p class="text-gray-500">Maximum file size 50 MB.</p>
              <input type="file" ref="fileInput" @change="handleFileChange" accept="image/*" style="display: none;" multiple>
            </div>
          </div>
  
          <!-- File upload progress display -->
          <div v-for="(file, index) in uploadedFiles" :key="index" class="mt-4">
            <div class="flex items-center justify-between p-2 bg-gray-100 rounded-lg mb-2">
              <div class="flex items-center">
                <i class="fas fa-file-video mr-2 text-gray-500"></i>
                <span class="text-sm font-medium">{{ file.name }}</span>
              </div>
              <div class="text-sm text-gray-500">{{ file.size }} MB</div>
              <button class="text-black" @click="removeFileItem(index)">
                <i class="fas fa-times"></i>
              </button>
            </div>
            <div class="w-full bg-gray-200 rounded-full h-1.5 dark:bg-gray-700" v-if="file.progress < 100">
              <div class="bg-blue-600 h-1.5 rounded-full" :style="{ width: file.progress + '%' }"></div>
            </div>
          </div>
        </div>

        <!-- <div v-if="showAlert" class="fixed top-0 left-1/2 transform -translate-x-1/2 mt-4 bg-red-600 text-white text-center font-semibold z-60 py-2 px-4 rounded-md">
            {{ message }}
        </div> -->

        <Alert :show="showAlert" :message="message" :type="'alert'" />

  
        <!-- Modal Footer -->
        <div class="flex justify-end pt-6">
          <button @click="$emit('close')" class="text-white bg-black px-6 py-2 rounded-md font-medium hover:bg-opacity-90 focus:outline-none focus:ring-2 focus:ring-black focus:ring-opacity-50">Cancel</button>
          <button @click="attachFile" class="text-white bg-black px-6 py-2 rounded-md font-medium hover:bg-opacity-90 focus:outline-none focus:ring-2 focus:ring-black focus:ring-opacity-50 ml-4">Attach files</button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        uploadedFiles: [],
        showAlert: false,
        uploading: false,
        message: "File already uploaded. Please delete the existing file first.",
      };
    },
    methods: {
    attachFile() {
        if (this.uploading) {
            this.message = "Please wait for the file to finish uploading.";
            return this.showCustomAlert();
        }
        else if (this.uploadedFiles.length === 0) {
            this.message = "Please upload a file first.";
            return this.showCustomAlert();
        }
        this.$emit("attach", this.uploadedFiles);
    },
      triggerFileUpload() {
        this.$refs.fileInput.click();
      },
      handleFileChange(event) {
        const newFiles = Array.from(event.target.files);
        this.message = "File already uploaded. Please delete the existing file first.";
        if (newFiles.length === 0) return;
        if (newFiles.length > 1) {
          this.message = "You can only upload up to 1 files at a time.";
          this.showCustomAlert();
          return;
        }
        else if (this.uploadedFiles.length + 1 > 1) {
            this.showCustomAlert();
        }
  
        newFiles.forEach(newFile => {
          if (this.uploadedFiles.some(file => file.name === newFile.name)) {
            this.showCustomAlert();
          } else {
            const fileSizeMB = (newFile.size / 1024 / 1024).toFixed(2);
            const fileWithProgress = {
              name: newFile.name,
              size: fileSizeMB,
              progress: 0
            };
            this.uploadedFiles.push(fileWithProgress);
            this.simulateUploadProgress(this.uploadedFiles.length - 1);
          }
        });
  
        event.target.value = null;
      },
      simulateUploadProgress(index) {
        this.uploading = true;
        const interval = setInterval(() => {
          if (this.uploadedFiles[index].progress < 100) {
            this.uploadedFiles[index].progress += 20;
          } else {
            this.uploading = false;
            clearInterval(interval);
          }
        }, 1000);
      },
      removeFileItem(index) {
        this.uploadedFiles.splice(index, 1);
        this.uploading = false;
      },
      showCustomAlert() {
        this.showAlert = true;
        setTimeout(() => {
          this.showAlert = false;
        }, 3000);
      }
    }
  }
  </script>
  