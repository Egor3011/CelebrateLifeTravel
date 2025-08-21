<template>
  <div class="hero-block" :style="{ '--bg-image': `url(${backgroundImage})` }">
    <div class="overlay"></div>
    <div class="content">
      <h1 class="main-title">{{ title }}</h1>
      <p class="description">{{ description }}</p>
      <button class="book-button">Забронировать тур</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HeroBlock',
  props: {
    title: {
      type: String,
      required: true,
    },
    description: {
      type: String,
      required: true,
    },
    backgroundImage: {
      type: String,
      required: true,
    },
  },
};
</script>

<style scoped>
.hero-block {
  position: relative;
  width: 100%;
  height: 100vh;
  background-size: cover;
  background-position: center;
  display: flex;
  flex-direction: column; /* Add flex-direction column */
  justify-content: space-between; /* Distribute space between nav and content */
  align-items: flex-start; /* Align content to the start (left) */
  color: white;
}

.hero-block::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: var(--bg-image);
  background-size: cover;
  background-position: center;
  z-index: 0;
}

.overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.4); /* Dark overlay */
  z-index: 1;
}

.content {
  position: relative;
  align-content: center;
  z-index: 2;
  display: flex;
  flex-direction: column;
  align-items: flex-start; /* Align content to the left */
  max-width: 800px; /* Adjust as needed */
  padding: 0 50px 80px 50px; /* Adjust padding for bottom and sides */
  text-align: left; /* Align text to the left */
}

/* .nav-bar {
  width: 100%;
  display: flex;
  justify-content: flex-end;
  padding: 20px 50px;
  margin-bottom: 80px;
}

.search-bar {
  background-color: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.5);
  border-radius: 20px;
  padding: 10px 20px;
  font-size: 16px;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
}

.search-bar p {
    margin: 0;
} */

.main-title {
  font-size: 48px;
  font-weight: bold;
  margin-bottom: 20px;
  color: var(--vt-second-color); /* Yellow color */
}

.description {
  font-size: 18px;
  margin-bottom: 40px;
  line-height: 1.5;
}

.book-button {
  font-size: 18px;
  border: none;

  box-shadow: none;
}

.book-button:hover {
  box-shadow: none;
  border: none;
}
</style>
