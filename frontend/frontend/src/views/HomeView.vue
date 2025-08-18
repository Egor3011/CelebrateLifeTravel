<script setup>
import { RouterLink } from 'vue-router';
import AboutUs from '@/components/blocks/AboutUs.vue';
import startImage from '@/components/blocks/startImage.vue';
import TGbot from '@/components/blocks/TGbot.vue';
import tourBlock from '@/components/blocks/tourBlock.vue';
import FAQBlock from '@/components/blocks/FAQBlock.vue';
import reviewsBlock from '@/components/blocks/reviewsBlock.vue';
import formMore from '@/components/blocks/formMore.vue';
</script>

<template>
  <main>

    <startImage/>

    <AboutUs/>

    <tourBlock/>

    <reviewsBlock/>

    <FAQBlock/>
    <formMore/>

    <TGbot/>
    <h1>Че за хуйня?</h1>
    <button>Забронировать место</button>
  </main>
</template>
