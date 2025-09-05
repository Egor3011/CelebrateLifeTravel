<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Navbar from './components/Navbar.vue';
import FooterBlock from './components/blocks/FooterBlock.vue';

</script>

<template>
  <Navbar/>
  
  <RouterView />
  <FooterBlock id="footerBlock"/>
</template>

<style scoped>
</style>