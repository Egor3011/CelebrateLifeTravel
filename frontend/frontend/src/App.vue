<script setup>
import { RouterLink, RouterView } from 'vue-router'
import AboutUs from './components/blocks/AboutUs.vue';
import startImage from './components/blocks/startImage.vue';
import headerComp from './components/headerComp.vue';

</script>

<template>
  <headerComp/>
  
  <RouterView />
</template>

<style scoped>
</style>