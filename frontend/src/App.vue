<script setup>
import { RouterLink, RouterView } from 'vue-router'
import AboutUs from './components/blocks/AboutUs.vue';
</script>

<template>
  <header>
    <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" />

    <div class="wrapper">

      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
  <a href="">testtest</a>
  <AboutUs/>
  
  <button>Забронировать место</button>
</template>

<style scoped>
</style>