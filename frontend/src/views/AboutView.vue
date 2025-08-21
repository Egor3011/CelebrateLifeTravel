<template>
  <div class="about">
    <HeroBlock
      :title="tourInfo.title"
      :description="tourInfo.description"
      :backgroundImage="tourInfo.backgroundImage"
    />
    <TourContentBlock 
      :content="tourInfo.tourContent" 
      :backgroundImage="tourInfo.backgroundImage_tourContent" 
    />
    <TourProgramBlock 
      :programItems="tourInfo.programData" 
      :price="tourInfo.price" 
    />

    <div class="container">
      <div class="line"></div>
    </div>

    <TourDatesBlock 
      :tourDates="tourInfo.tourDatesData" 
    />
    
    <FAQBlock/>
    <formMore/>
    <TGbot/>

  </div>
</template>

<script setup>
import HeroBlock from '../components/blocks/HeroBlock.vue';
import TourContentBlock from '../components/blocks/TourContentBlock.vue';
import TourProgramBlock from '../components/blocks/TourProgramBlock.vue';
import TGbot from '@/components/blocks/TGbot.vue';
import FAQBlock from '@/components/blocks/FAQBlock.vue';
import formMore from '@/components/blocks/formMore.vue';
import TourDatesBlock from '@/components/TourDatesBlock.vue';

import { useRoute } from 'vue-router';
import { onMounted, ref } from 'vue';

import axios from 'axios';
// import bgStartImage from '../public/bgStart.png';

const tourInfo = ref({});

onMounted(() => {
  const route = useRoute();
  const tourValue = route.query.tour;
  if (tourValue) {
    console.log('Tour parameter from URL:', tourValue);

    axios.get(`/api/tours/${tourValue}`).then((res) => {
      tourInfo.value = res.data;
    });
  
  }
});
</script>

<style>
</style>
