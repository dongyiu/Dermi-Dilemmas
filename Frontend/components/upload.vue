<template>
    <div class="w-full h-full items-center justify-center bg-white dark:bg-black p-2">
      <main class="bg-white min-h-screen flex items-center justify-center p-6">
        <div class="bg-white rounded-lg shadow-lg p-8 max-w-lg w-full">
          <div class="flex justify-between items-center pb-5 border-b border-gray-200">
            <h1 class="text-2xl font-semibold">Upload and attach files</h1>
          </div>
          <div class="py-6">
            <div @click="triggerFileUpload" class="flex justify-center items-center w-full">
              <div class="flex flex-col items-center justify-center w-full border-2 border-dashed border-gray-300 rounded-lg p-6 cursor-pointer">
                <p class="text-gray-500">Click to upload</p>
                <p class="text-gray-500">Maximum file size 50 MB.</p>
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
          <div class="flex justify-end pt-6">
            <button @click="$emit('close')" class="text-white bg-black px-6 py-2 rounded-md font-medium hover:bg-opacity-90 focus:outline-none focus:ring-2 focus:ring-black focus:ring-opacity-50">Cancel</button>
            <button @click="$emit('attach', uploadedFiles)" class="text-white bg-black px-6 py-2 rounded-md font-medium hover:bg-opacity-90 focus:outline-none focus:ring-2 focus:ring-black focus:ring-opacity-50 ml-4">Attach files</button>

            <!-- <button class="text-white bg-black px-6 py-2 rounded-md font-medium hover:bg-opacity-90 focus:outline-none focus:ring-2 focus:ring-black focus:ring-opacity-50">Cancel</button> -->
            <!-- <button class="text-white bg-black px-6 py-2 rounded-md font-medium hover:bg-opacity-90 focus:outline-none focus:ring-2 focus:ring-black focus:ring-opacity-50 ml-4">Attach files</button> -->
          </div>
        </div>
      </main>
      <input type="file" ref="fileInput" @change="handleFileChange" style="display: none;" multiple>
      <!-- Custom Alert -->
      <div v-if="showAlert" class="fixed top-0 inset-x-0 p-4 bg-red-600 text-white text-center font-semibold z-50">
        {{ message }}
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        uploadedFiles: [],
        showAlert: false,
        message: "File already uploaded. Please delete the existing file first.",
      };
    },
    methods: {
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
        const interval = setInterval(() => {
          if (this.uploadedFiles[index].progress < 100) {
            this.uploadedFiles[index].progress += 20;
          } else {
            clearInterval(interval);
          }
        }, 1000);
      },
      removeFileItem(index) {
        this.uploadedFiles.splice(index, 1);
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
  
  <style>
  /* Add your Tailwind CSS classes or custom styles here */
  </style>
  