<template>
  <div class="values-block-container">
    <div class="header-section">
      <span class="tag">Преимущества</span>
      <h2 style="margin-top: 10px;">ТО, ЧТО ДЕЛАЕТ КАЖДОЕ <br />ПУТЕШЕСТВИЕ С НАМИ ОСОБЕННЫМ</h2>
    </div>

    <div class="cards-grid">
      <div v-for="(card, index) in cards" :key="index" class="value-card">
        <h3>{{ card.title }}</h3>
        <p>{{ card.description }}</p>
      </div>
    </div>

    <button class="cta-button" @click="scrolToTours">Выбрать путешествие</button>
  </div>
</template>

<script setup>
import { defineProps, onMounted } from 'vue';
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);

const props = defineProps({
  cards: {
    type: Array,
    required: true,
  },
});

const scrolToTours = () => {
    const el = document.getElementById("katalog");
    el.scrollIntoView({behavior: "smooth"});
}

onMounted(() => {
  gsap.to('.cta-button', {
    x: 3, // horizontal shake
    y: 2, // vertical shake
    rotation: 2, // slight rotation
    duration: 0.1, // very short animation for each shake direction
    repeat: 2,     // 2 repeats + initial = 3 shakes forward/back
    yoyo: true,    // for back and forth motion
    repeatDelay: 1, // wait 1 second after the full shake sequence
    repeat: -1,
    ease: 'power1.inOut',
  });

  gsap.from('.value-card', {
    opacity: 0,
    y: 100, // Start from 100px to the left
    duration: 1,
    stagger: 0.3, // Stagger the animation for each card
    ease: 'power2.out',
    scrollTrigger: {
      trigger: '.cards-grid',
      start: 'top 25%',
      end: 'bottom 80%',
      toggleActions: 'play none none none',
      // markers: true, // Uncomment for debugging scroll trigger
    },
  });
});
</script>

<style scoped>
.values-block-container {
  background-image: url('https://clt.s3.cloud.ru/photos/osetia_ingushetia/1');/* Assuming a similar background as the form block */
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
  padding: 60px 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  color: var(--vt-text2-color); /* White text on dark background */
}

@media(max-width: 768px) {
  .values-block-container {
    background-image: url("https://clt.s3.cloud.ru/photos/baical/12");
  }
}

.header-section {
  text-align: center;
  margin-bottom: 50px;
}

.tag {
  background-color: var(--vt-second-color);
  color: var(--vt-text-color);
  padding: 8px 20px;
  border-radius: 20px;
  font-family: 'Montserrat';
  font-size: 0.9em;
  font-weight: bold;
  margin-bottom: 20px;
  display: inline-block;
}

h2 {
  font-family: 'Unbounded-Bold';
  font-size: 2.8em;
  line-height: 1.2;
  margin-top: 20px;
  color: var(--vt-text2-color);
}

.cards-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 30px;
  max-width: 1200px;
  width: 100%;
  margin-bottom: 50px;
}

.value-card {
  background-color: rgba(0, 0, 0, 0.1); /* Semi-transparent dark background for cards */
  backdrop-filter: blur(10px);
  border-radius: 15px;
  padding: 30px;
  border: 1px solid var(--vt-text2-color);
}

.value-card h3 {
  font-family: 'Unbounded-Bold';
  font-size: 1.5em;
  margin-top: 0;
  margin-bottom: 15px;
  color: var(--vt-text2-color);
}

.value-card p {
  font-family: 'Montserrat';
  font-size: 0.95em;
  line-height: 1.6;
  color: rgba(255, 255, 255, 0.8);
}

.cta-button { /* Orange color from image */
  border: none;
  border-radius: 25px;
  padding: 15px 30px;
  font-family: 'Unbounded-Bold';
  font-size: 1.1em;
  cursor: pointer;
  transition: 0.2s;
}

.cta-button:hover {
  box-shadow: none;
  opacity: 0.8;
  transition: 0.2s;
}

.cta-button:active {
  opacity: 0.5;
  transition: 0.2s;
}

@media (max-width: 1024px) {
  .cards-grid {
    grid-template-columns: 1fr; /* Single column on smaller screens */
    padding: 0 20px;
  }

  h2 {
    font-size: 2em;
    padding: 0 20px;
  }

  .value-card {
    padding: 25px;
  }
}

@media (max-width: 768px) {
  .values-block-container {
    padding: 40px 15px;
  }

  h2 {
    font-size: 1.8em;
  }

  .cta-button {
    width: 90%;
    padding: 12px 20px;
    font-size: 1em;
  }
}
</style>
