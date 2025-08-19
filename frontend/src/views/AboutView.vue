<template>
  <div class="about">
    <HeroBlock
      :title="tourInfo.title"
      :description="tourInfo.description"
      :backgroundImage="tourInfo.backgroundImage"
    />
    <TourContentBlock 
      :content="tourInfo.tourContent" 
      backgroundImage="/bgStart.png" 
    />
    <TourProgramBlock 
      :programItems="tourInfo.programData" 
      :price="tourInfo.price" 
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

import { useRoute } from 'vue-router';
import { onMounted, ref } from 'vue';

import axios from 'axios';
// import bgStartImage from '../public/bgStart.png';

const tourInfo = ref({});

const tourContent = ref([
  'СУЛАКСКИЙ КАНЬОН',
  'ПРОГУЛКА НА КАТЕРЕ ПО ЧИРКЕЙСКОМУ ВОДОХРАНИЛИЩУ',
  'САМЫЙ ДРЕВНИЙ ГОРОД РОССИИ - ДЕРБЕНТ',
  'САМЫЙ БОЛЬШОЙ В РОССИИ ФОНТАН',
  'САМЫЙ БОЛЬШОЙ ВОДОПАД ДАГЕСТАНА - ТОБОТ',
  'ПУСТЫНЯ БАРХАН САРЫКУМ',
  'ФОТОСЕССИЯ НА ЗНАМЕНИТОМ ЯЗЫКЕ ТРОЛЛЯ',
  'УНИКАЛЬНЫЙ РАКЕТОНОСЕЦ ЭКРАНОПЛАН ЛУНЬ',
  'ЗАБРОШЕННОЕ СЕЛО ГАМСУТЛЬ',
]);

const programData = ref([
  {
    question: 'ПЕРВЫЙ ДЕНЬ: СУЛАКСКИЙ КАНЬОН, КАТЕР, ПУСТЫНЯ БАРХАН САРЫКУМ',
    answer: 'ВСТРЕЧА В ПЕРВЫЙ ДЕНЬ ТУРА В АЭРОПОРТУ Г. МАХАЧКАЛЫ (ПРИЛЕТ ДО 11 Ч). ПЕРВАЯ И НЕОБЫЧНАЯ ЛОКАЦИЯ - ПУСТЫНЯ БАРХАН САРЫКУМ. ГОР ОБРАЗОВАЛАСЬ ПУСТЫНЯ В ДАГЕСТАНЕ УЗНАЕШЬ, КАК СРЕДИ ВИЗИТНАЯ КАРТОЧКА ДАГЕСТАНА - СУЛАКСКИЙ КАНЬОН, САМЫЙ ГЛУБОКИЙ КАНЬОН В МИРЕ. ДАЛЕЕ ТЕБЯ ЖДЕТ ПРОГУЛКА НА СКОРОСТНОМ КАТЕРЕ ПО ЧИРКЕЙСКОМУ ВОДОХРАНИЛИЩУ ПРОЕДЕШЬ ЧЕРЕЗ САМЫЙ ДЛИННЫЙ ТОННЕЛЬ В РОССИИ! НАЦИОНАЛЬНЫЙ УЖИН И НОЧЕВКА В КОМФОРТАБЕЛЬНОМ ГОРНОМ ОТЕЛЕ. (НОМЕРА ДВУХ- И ТРЕХМЕСТНЫЕ, СО ВСЕМИ УДОБСТВАМИ: ДУШ, ТУАЛЕТ, КОНД ИЦИОНЕР, ПОЛОТЕНЦА, ФЕН)'
  },
  {
    question: 'ВТОРОЙ ДЕНЬ: СТОРОЖЕВЫЕ БАШНИ, КАРАДАХСКАЯ ТЕСНИНА',
    answer: 'Контент для второго дня.'
  },
  {
    question: 'ТРЕТИЙ ДЕНЬ: КРЕПОСТЬ НА КРЕПОСТИ, СЕЛЕНИЯ В ГОРАХ',
    answer: 'Контент для третьего дня.'
  }
]);

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
