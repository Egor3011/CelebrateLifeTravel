<template>
  <nav class="navbar container">
    <div class="navbar-brand">
      <RouterLink to="/" class="brand-link">
        <span class="brand-name">CELEBRATE LIFE</span>
        <span class="brand-travel">TRAVEL</span>
      </RouterLink>
    </div>

    <ul class="navbar-links">
      <li><a href="#about">О нас</a></li>
      <li><a href="#katalog">Каталог туров</a></li>
      <li><a href="#plus">Преимущества</a></li>
      <li><a href="#reviews">Отзывы</a></li>
    </ul>

    <div class="navbar-actions">
      <button class="request-button" @click="scrolToForm">Оставить заявку</button>
      <button class="hamburger-button" @click="toggleMenu">
        <div class="hamburger-icon"></div>
        <div class="hamburger-icon"></div>
        <div class="hamburger-icon"></div>
      </button>
    </div>
  </nav>
  <div class="mobile-menu" :class="{ 'is-open': isMenuOpen }">
    <ul class="mobile-navbar-links">
      <li><RouterLink to="/" @click="closeMenu">Главная</RouterLink></li>
      <li><a href="#about" @click="closeMenu">О нас</a></li>
      <li><a href="#katalog" @click="closeMenu">Каталог туров</a></li>
      <li><a href="#plus" @click="closeMenu">Преимущества</a></li>
      <li><a href="#reviews" @click="closeMenu">Отзывы</a></li>
      <li><RouterLink to="/documents" @click="closeMenu">Юридическая информация</RouterLink></li>
    </ul>
    <button class="request-button mobile-request-button" @click="closeMenu">Оставить заявку</button>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue';
import { RouterLink } from 'vue-router';

const isMenuOpen = ref(false);

const scrolToForm = () => {
    const el = document.getElementById("form");
    el.scrollIntoView({behavior: "smooth"});
}

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value;
};

const closeMenu = () => {
  isMenuOpen.value = false;
};

watch(isMenuOpen, (newValue) => {
  if (newValue) {
    document.body.classList.add('no-scroll');
  } else {
    document.body.classList.remove('no-scroll');
  }
});
</script>

<style scoped>
.navbar {
  position: fixed;
  top: 0;
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 40px;
  background-color: var(--vt-background);
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  z-index: 1000;
  border-radius: 50px;
  margin: 20px auto;
  max-width: calc(100% - 80px); /* This will constrain width and allow auto margins to center */
}

@media (min-width: 1025px) {
  .navbar {
    width: 80%; /* Keeping user's change to 80% */
    margin: 10px calc(10vw - 40px); /* Centering for wider screens */
    max-width: none; /* Remove previous max-width constraint */
  }
}

@media (max-width: 1024px) {
  .navbar {
    width: calc(100vw - 40px); /* Full width for smaller screens */
    max-width: none;
    margin: 0; /* Remove margins for full width */
    border-radius: 0; /* Remove border-radius for full width */
    padding: 10px 20px; /* Adjust padding for smaller screens */
  }
}

@media (max-width: 768px) {
  .navbar {
    padding: 10px 20px;
    border-radius: 0;
    max-width: 100%;
    margin: 0;
  }
}


.navbar-brand {
  display: flex;
  align-items: center;
}

.brand-link {
  text-decoration: none;
  display: flex;
  flex-direction: column;
  line-height: 1;
}

.brand-name {
  font-family: 'Unbounded-Bold';
  font-size: 1.2em;
}

.brand-travel {
  font-family: 'Montserrat';
  font-size: 0.8em;
  text-decoration: underline;
}

.brand-link:hover .brand-name,
.brand-link:hover .brand-travel {
  color: var(--vt-second-color);
  text-decoration: underline;
  transition: 0.3s;
}

.navbar-links {
  list-style: none;
  display: flex;
  margin: 0;
  padding: 0;
}

.navbar-links li a {
  text-decoration: none;
  color: var(--vt-text-color);
  font-family: 'Montserrat';
  margin: 0 15px;
  border-radius: 5px;
  padding: 3px;
  font-size: 0.9em;
  transition: 0.3s;
}

.navbar-links li a:hover {
  color: var(--vt-background-color);
  background: var(--vt-second-color);
  transition: 0.3s;
}

.request-button {
  background-color: var(--vt-second-color);
  color: var(--vt-text-color);
  border: none;
  border-radius: 25px;
  padding: 10px 20px;
  font-family: 'Unbounded-Bold';
  font-size: 0.9em;
  cursor: pointer;
}

.request-button:hover {
  transform: translate(10px, 0);
}

.hamburger-button {
  background: none;
  box-shadow: none;
  border: none;
  cursor: pointer;
  padding: 5px;
  display: none;
}

.hamburger-icon {
  width: 25px;
  height: 3px;
  background-color: var(--vt-text-color);
  margin: 5px 0;
  border-radius: 3px;
}

.mobile-menu {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: var(--vt-background);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  transform: translateX(-100%);
  transition: transform 0.3s ease-in-out;
  z-index: 999;
  padding: 20px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.mobile-menu.is-open {
  transform: translateX(0);
}

.mobile-navbar-links {
  list-style: none;
  padding: 0;
  margin: 0 0 30px 0;
  text-align: start;
}

.mobile-navbar-links li {
  margin-bottom: 20px;
}

.mobile-navbar-links a {
  text-decoration: none;
  color: var(--vt-text-color);
  font-family: 'Montserrat';
  font-size: 1.2em;
  transition: color 0.3s ease;
}

.mobile-navbar-links a:hover {
  color: var(--vt-second-color);
}

.mobile-request-button {
  background-color: #4285F4;
  color: var(--vt-text2-color);
  border: none;
  border-radius: 25px;
  padding: 10px 20px;
  font-family: 'Unbounded-Bold';
  font-size: 0.9em;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.mobile-request-button:hover {
  background-color: #357ae8;
}

@media (max-width: 1024px) {
  .navbar-links {
    display: none;
  }
  .hamburger-button {
    display: block;
  }

  .request-button {
    display: none;
  }
}

@media (max-width: 768px) {
  .navbar {
    padding: 10px 20px;
    border-radius: 0;
    max-width: 100%;
    margin: 0;
  }
}
</style>
