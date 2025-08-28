<script setup>
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";


import { Navigation, Pagination, Scrollbar, A11y } from 'swiper/modules';
import {Swiper, SwiperSlide} from "swiper/vue";
import "swiper/css/bundle";
import 'swiper/css/navigation';
import 'swiper/css/pagination';
import 'swiper/css/scrollbar';
    
import { onMounted } from "vue";
import { ref } from "vue";
import axios from "axios";

import tourCArd from "../tourCArd.vue";

gsap.registerPlugin(ScrollTrigger);

const modules = [Navigation, Pagination, Scrollbar, A11y]

const tourInfo = ref([])

onMounted(() => {
    gsap.from(".titleBlockDiv__tourBlock", {
        scrollTrigger: {
            trigger: ".titleBlockDiv__tourBlock",
            start: "top bottom",
        },
        x: -100,
        opacity: 0,
        duration: 1
    })
    axios.get("https://be67bc91a5069fe3.mokky.dev/tour").then((res) => {
        tourInfo.value = res.data
    })
})

</script>

<template>
    <div class="container">
        <div class="titleBlockDiv__tourBlock">
            <span class="headH1">Каталог туров</span>
            <h2 class="titleBlock titleBlockDiv__tourBlock__h1">Наши направления</h2>
        </div>
        <Swiper 
        :modules="modules"
        :slides-per-view="2.5" 
        :space-between="40" 
        :freeMode="true"
        navigation
        :breakpoints="{0: {slidesPerView: 1.3}, 320: {slidesPerView: 1.7, spaceBetween: 10}, 640: {slidesPerView: 2.5, spaceBetween: 25}, 1024: {slidesPerView: 2.8, spaceBetween: 40},}"
        style="height: auto; padding: 40px 20px; overflow: hidden;">
            <swiper-slide v-for="el in tourInfo" >
                <tourCArd :title="el.title" :img-src="el.imgSrc" :info="el.info" :link="el.link"/>
            </swiper-slide>
        </Swiper>
    </div>
</template>