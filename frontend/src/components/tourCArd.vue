<template>
  <div class="carousel">
    <div class="carousel-inner" :style="{ transform: `translateX(-${currentIndex * 100}%)` }">
      <div class="carousel-item" v.for="(slide, index) in slides" :key="index">{{ slide }}</div>
    </div>
    <button @click="prevSlide">Предыдущий</button>
    <button @click="nextSlide">Следующий</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      slides: ['Слайд 1', 'Слайд 2', 'Слайд 3'],
      currentIndex: 0
    };
  },
  methods: {
    nextSlide() {
      this.currentIndex = (this.currentIndex + 1) % this.slides.length;
    },
    prevSlide() {
      this.currentIndex = (this.currentIndex - 1 + this.slides.length) % this.slides.length;
    }
  }
};
</script>

<style>
.carousel {
  overflow: hidden;
  width: 300px;
}
.carousel-inner {
  display: flex;
  transition: transform 0.3s ease;
}
.carousel-item {
  min-width: 100%;
}
</style>
