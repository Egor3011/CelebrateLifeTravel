<template>
    <div class="container aboutAllSwiper">
        <div class="titleBlockDiv__ABOUTUSswiper">
            <span class="headH1">О нас</span>
            <div style="height: 2px;"></div>
            <h2 class="titleBlock">Celebrate Life Travel - кто мы такие?</h2>
        </div>
        <div class="swiperSS">
            <Swiper 
            :modules="modules"
            :slides-per-view="2.5" 
            :space-between="40" 
            :freeMode="true"
            navigation
            :breakpoints="{0: {slidesPerView: 1.2}, 320: {slidesPerView: 1.4, spaceBetween: 10}, 640: {slidesPerView: 2.2, spaceBetween: 25}, 1024: {slidesPerView: 2.8, spaceBetween: 40},}"
            style="height: auto; padding: 40px 20px; overflow: hidden;">
                <SwiperSlide>
                    <h3>Мы занимаемся авторскими турами уже 4 года и превращаем каждое путешествие в уникальную историю, наполненную комфортом, качественным наполнением программы и живым человеческим общением.</h3>
                    <h3> Наш подход —  внимательность к деталям и забота о каждом участнике, чтобы путешествие было не только красивым маршрутом, но и легким, приятным и вдохновляющим опытом.</h3>
                </SwiperSlide>
                <swiper-slide v-for="el in info" >
                    <TeamCard 
                        :image-url="el.imgSrc"
                        :rotation="el.rotation"
                        :title="el.title"
                        :items="el.items"
                    />
                </swiper-slide>
            </Swiper>
        </div>

    </div>
</template>

<script setup>
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

import { Navigation, Pagination, Scrollbar, A11y } from 'swiper/modules';
import {Swiper, SwiperSlide} from "swiper/vue";
import "swiper/css/bundle";
import 'swiper/css/navigation';
import 'swiper/css/pagination';
import 'swiper/css/scrollbar';

const modules = [Navigation, Pagination, Scrollbar, A11y]

import axios from 'axios';
import { ref, onMounted } from 'vue';
import TeamCard from './TeamCard.vue';

const info = ref([])

onMounted(() => {
    gsap.from(".titleBlockDiv__ABOUTUSswiper", {
        scrollTrigger: {
            trigger: ".aboutAllSwiper",
            start: "20% bottom",
        },
        x: -100,
        opacity: 0,
        duration: 1,
    })

    axios.get("https://be67bc91a5069fe3.mokky.dev/aboutUs").then((res) => {
        info.value = res.data
        console.log(info.value)
    })
})
</script>