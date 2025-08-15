<template>
    <div class="aboutUs-Block container">
        <div class="titleBlockDiv__aboutUs">
            <span class="headH1 komand--AboutUs">Команда</span>
            <h2 class="titleBlock" style="width: 500px;">CELEBRATE LIFE TRAVEL  – это двигатель ваших приключений</h2>
        </div>
        <div style="text-align: center;">
            <h2>Наша команда</h2>
        </div>
        <Swiper 
        :slides-per-view="2.5" 
        :space-between="40" 
        :freeMode="true"
        :breakpoints="{0: {slidesPerView: 1.2}, 320: {slidesPerView: 1.4, spaceBetween: 10}, 640: {slidesPerView: 2.8, spaceBetween: 25}, 1024: {slidesPerView: 3.5, spaceBetween: 40},}"
        style="height: auto; padding: 40px 20px; overflow: hidden;">
            <swiper-slide v-for="el in comandInfo" >
                <testCardCom :name-title="el.name" :img-src="el.imgSrc" :info="el.info" :position="el.position"/>
            </swiper-slide>
        </Swiper>
    </div>
</template>

<script setup>
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import {Swiper, SwiperSlide} from "swiper/vue";
import "swiper/css/bundle";
import axios from "axios";

import { ref } from "vue";

import { onMounted } from "vue";

import testCardCom from "./testCardCom.vue";

gsap.registerPlugin(ScrollTrigger);

const comandInfo = ref([])



onMounted(() => {
    gsap.from(".titleBlockDiv__aboutUs", {
        scrollTrigger: {
            trigger: ".aboutUs-Block",
            start: "5% bottom",
        },
        x: -100,
        opacity: 0,
        duration: 1,
    })

    axios.get("https://be67bc91a5069fe3.mokky.dev/command").then((res) => {
        comandInfo.value = res.data
    })
})

const getCommandCardsInfo = () => {
    axios.get("https://be67bc91a5069fe3.mokky.dev/command").then((res) => {
        return res.data
    })
}
</script>