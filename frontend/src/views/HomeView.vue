<script setup>
import { RouterLink } from 'vue-router';
import AboutUs from '@/components/blocks/AboutUs.vue';
import startImage from '@/components/blocks/startImage.vue';
import TGbot from '@/components/blocks/TGbot.vue';
import tourBlock from '@/components/blocks/tourBlock.vue';
import FAQBlock from '@/components/blocks/FAQBlock.vue';
</script>

<template>
  <main>
    <startImage/>

    <AboutUs/>

    <tourBlock/>

    <FAQBlock/>

    <TGbot/>
    <button>Забронировать место</button>
  </main>
</template>
