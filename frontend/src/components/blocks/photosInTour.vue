<template>
    <div class="reviewBlock container">
        <div class="titleBlockDiv__reviewBlock">
            <span class="headH1">Галерея</span>
            <h2 class="titleBlock">Фотографии из этого путешествия</h2>
        </div>

        <swiper 
        :modules="modules"
        :slides-per-view="1.2" 
        :space-between="10" 
        :freeMode="true"
        navigation
        :breakpoints="{0: {slidesPerView: 1.0, spaceBetween: 10}, 640: {slidesPerView: 1.2, spaceBetween: 20}, 1024: {slidesPerView: 2, spaceBetween: 40},}"
        style="padding: 0 20px; overflow: hidden;">
        
            <swiper-slide v-for="el in props.photos" >
                <img :src="el" style="width: 100%; height: auto; border-radius: 30px;">
            </swiper-slide>
        </swiper>
    </div>
</template>

<script setup>
import { Navigation, Pagination, Scrollbar, A11y } from 'swiper/modules';
import {Swiper, SwiperSlide} from "swiper/vue";
import "swiper/css/bundle";
import 'swiper/css/navigation';
import 'swiper/css/pagination';
import 'swiper/css/scrollbar';

import { onMounted, ref, defineProps } from 'vue';
const modules = [Navigation, Pagination, Scrollbar, A11y]

const props = defineProps({
  photos: {
    type: Array,
    default: () => [],
  },
});
</script>