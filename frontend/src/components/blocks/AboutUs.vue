<template>
    <div class="aboutUs-Block container">
        <div class="titleBlockDiv__aboutUs">
            <span class="headH1 komand--AboutUs">Команда</span>
            <h2 class="titleBlock">CELEBRATE LIFE TRAVEL  – это двигатель ваших приключений</h2>
        </div>
        <div style="text-align: center;">
            <h2>Организатор туров</h2>
        </div>
        <div class="aboutMe__aboutUs">
            <img src="https://clt.s3.cloud.ru/photos/ALL/organizator">
            <div style="display: block;">
                <p class="pText">Давай знакомится, меня зовут Екатерина Силищева, я организатор туров и основатель Celebrate Life Travel.</p>
                <p class="pText">Я путешественник с большим стажем и посетила более 30 стран. Живу в Москве, но большую часть времени провожу в своих турах и путешествиях.</p>
                <p class="pText">Мое агентство появилось 4 года назад просто из идеи - организовывать авторские туры в Дагестан. Я сильно загорелась этим делом, активно добавляла новые направления, мы отлично справлялись со всем, и моя компания стала одним из лидеров рынка. </p>
                <p class="pText">Сейчас мы проводим авторские туры по 10 направлениям, в моем штате работает 7 сотрудников и за 4 года мы свозили уже более 3500 людей в наши туры.</p>
                <p class="pText">Моя миссия - показать людям с лучшей стороны самые красивые уголки нашей планеты в своих авторских турах и объединить людей, схожих по духу и интересам.</p>
                <p class="pText">Если ты хочешь стать частью нашего клуба путешественников, мы ждём тебя в одном из наших туров!</p>
            </div>
            
        </div>

        <div style="text-align: center;">
            <h2>Наша команда</h2>
        </div>
        <Swiper 
        :modules="modules"
        :slides-per-view="2.5" 
        :space-between="40" 
        :freeMode="true"
        navigation
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

import { Navigation, Pagination, Scrollbar, A11y } from 'swiper/modules';
import {Swiper, SwiperSlide} from "swiper/vue";
import "swiper/css/bundle";
import 'swiper/css/navigation';
import 'swiper/css/pagination';
import 'swiper/css/scrollbar';

import axios from "axios";

import { ref } from "vue";

import { onMounted } from "vue";

import testCardCom from "./testCardCom.vue";

const modules = [Navigation, Pagination, Scrollbar, A11y]
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
</script>

<style>
.aboutUs-Block {
    margin-top: 40px;
}

.titleBlockDiv__aboutUs {
    width: 100%;
}

.aboutMe__aboutUs {
    display: flex;
    img {
        margin-right: 40px;
        width: 35%; 
        height: auto;
        max-height: 80vh;
        border-radius: 20px;
        object-fit: cover;
    }
    
}

.pText {
    width: auto;
}

@media(max-width: 1024px) {
    .aboutMe__aboutUs {
        display: block;
        text-align: center;
        img {
            margin-bottom: 40px;
            margin-right: 0;
            width: 100%;
            height: auto;
        }
    }
}

.pText {
    text-align: start;
    width: 100%;
}
</style>