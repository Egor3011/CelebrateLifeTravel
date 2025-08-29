<template>
  <div class="hero-tour-block">
    <div class="content">
      <img src="/public/celebrate_life_travel.svg" alt="Celebrate Life Travel Logo" class="logo" />
      <h1>АВТОРСКИЕ ТУРЫ</h1>
      <p>Насыщенные и комфортные путешествия, с душой и вниманием к деталям</p>
      <button class="book-tour-button" @click="scrolToForm">Забронировать тур</button>
    </div>
  </div>
</template>

<script setup>

const scrolToForm = () => {
    const el = document.getElementById("form");
    el.scrollIntoView({behavior: "smooth"});
}
</script>

<style scoped>
/* Default styles (for mobile and smaller desktops) */
.hero-tour-block {
  position: relative;
  width: 100vw;
  height: 100vh; /* Full viewport height */
  background-image: url('https://clt.s3.cloud.ru/photos/ALL/katya_mainPage'); /* Background image from the provided image */
  background-size: cover;
  background-position: center; /* Makes the background move with scrolling */
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  color: var(--vt-text2-color); /* White text */
  overflow: hidden; /* Ensure content doesn't spill */
  box-sizing: border-box;
}

.content {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 10;
  padding: 20px;
  max-width: 90%; /* Max width for content */
}

.content h1 {
    margin-top: 0;
}

.logo {
  max-width: 200px;
  margin-bottom: 20px;
  filter: drop-shadow(0 0 5px rgba(0, 0, 0, 0.5));
  border-bottom: 1px solid #ffffff;
}

h1 {
  font-family: 'Unbounded-Bold';
  font-size: 3.5em;
  color: var(--vt-second-color);
  margin-bottom: 20px;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
}

p {
  font-family: 'Montserrat';
  font-size: 1.2em;
  margin-bottom: 40px;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.7);
}

.book-tour-button {
  background-color: var(--vt-second-color);
  color: var(--vt-text-color);
  border: none;
  border-radius: 30px;
  padding: 15px 40px;
  font-family: 'Unbounded-Bold';
  font-size: 1.1em;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.2s ease;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
}

.book-tour-button:hover {
  background-color: #e6e600; /* Slightly darker yellow */
  transform: translateY(-2px);
}

/* Desktop styles */
@media (min-width: 1025px) {
  .hero-tour-block {
    justify-content: flex-start; /* Align content to the left */
    padding-left: 10vw; /* Desktop left padding */
  }

  .content {
    position: relative; /* Override absolute for desktop */
    top: auto;
    left: auto;
    transform: none;
    max-width: 500px; /* Adjust max-width for desktop content */
    text-align: left; /* Align text to the left */
  }

  .logo {
    margin-left: 0; /* Ensure logo aligns left */
  }

  h1,
  p {
    text-align: left; /* Align title and paragraph to the left */
  }

  .book-tour-button {
    display: inline-block; /* Allow button to be part of left-aligned flow */
  }
}

@media (max-width: 1024px) {
  h1 {
    font-size: 2.5em;
  }

  p {
    font-size: 1em;
  }

  .book-tour-button {
    padding: 12px 30px;
    font-size: 1em;
  }

  .logo {
    max-width: 150px;
  }
}

@media (max-width: 768px) {
  .hero-tour-block {
    height: 100vh; /* Adjust height for smaller mobile screens */
    background-image: url('https://clt.s3.cloud.ru/photos/ALL/mainPage_phone');
  }

  h1 {
    font-size: 2em;
  }

  p {
    font-size: 0.9em;
  }

  .book-tour-button {
    width: 80%;
    max-width: 300px;
    font-size: 12px;
  }
}
</style>
