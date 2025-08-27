<template>
    <div class="reviewBlock container">
        <div class="titleBlockDiv__reviewBlock">
            <span class="headH1">Отзывы</span>
            <h2 class="titleBlock">Ваши отзывы о наших путешествиях</h2>
        </div>

        <swiper 
        :modules="modules"
        :slides-per-view="1.2" 
        :space-between="50" 
        :freeMode="true"
        navigation
        :breakpoints="{0: {slidesPerView: 1.0}, 320: {slidesPerView: 1.2, spaceBetween: 25}, 640: {slidesPerView: 2.1, spaceBetween: 40}, 1024: {slidesPerView: 2.6, spaceBetween: 50},}"
        style="padding: 0 20px; overflow: hidden;">
        
            <swiper-slide v-for="el in props.reviewLinks" >
                <img :src="el" style="width: 100%; height: auto;">
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
  reviewLinks: {
    type: Array,
    default: () => [],
  },
});
</script>