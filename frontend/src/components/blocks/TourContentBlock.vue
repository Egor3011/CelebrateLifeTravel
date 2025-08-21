<template>
  <div class="tour-content-block" :style="{ '--bg-image': `url(${backgroundImage})` }">
    <h2 class="block-title">Наполнение тура</h2>
    <div class="content-card">
      <ul>
        <li v-for="(item, index) in content" :key="index">{{ item }}</li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TourContentBlock',
  props: {
    content: {
      type: Array,
      required: true,
      default: () => [],
    },
    backgroundImage: {
      type: String,
      required: false,
      default: '',
    },
  },
};
</script>

<style scoped>
.tour-content-block { /* Dark background similar to the image */
  padding: 50px 20px;
  text-align: center;
  color: white;
  background-size: cover;
  background-position: center;
  
  background-image: var(--bg-image); 
}

.tour-content-block {
  background-image: var(--bg-image); 
}

.block-title {
  font-size: 36px;
  font-weight: bold;
  margin-bottom: 40px;
}

.content-card {
  background-color: rgba(255, 255, 255, 0.1); /* Semi-transparent white background for the card */
  border: 1px solid rgba(255, 255, 255, 0.3); /* Light border */
  border-radius: 20px;
  padding: 40px 20px;
  max-width: 700px;
  margin: 0 auto;
  backdrop-filter: blur(5px); /* Optional: for frosted glass effect */
}

.content-card ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.content-card li {
  font-size: 20px;
  margin-bottom: 15px;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.content-card li:last-child {
  margin-bottom: 0;
}

/* Responsive styles */
@media (max-width: 768px) {
  .block-title {
    font-size: 28px;
    margin-bottom: 30px;
  }

  .content-card {
    padding: 30px 15px;
  }

  .content-card li {
    font-size: 16px;
    margin-bottom: 10px;
  }
}

@media (max-width: 480px) {
  .block-title {
    font-size: 24px;
    margin-bottom: 20px;
  }

  .content-card {
    padding: 20px 10px;
  }

  .content-card li {
    font-size: 14px;
    margin-bottom: 8px;
  }
}
</style>
