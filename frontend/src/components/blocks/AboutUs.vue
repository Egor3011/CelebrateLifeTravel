<template>
    <div class="aboutUs-Block container">
        <div class="titleBlockDiv__aboutUs">
            <span class="headH1 komand--AboutUs">Команда</span>
            <h2 class="titleBlock" style="width: 500px;">CELEBRATE LIFE TRAVEL  – это двигатель ваших приключений</h2>
        </div>
        <div style="text-align: center;">
            <h2>Наша команда</h2>
        </div>
        <testCardCom/>
    </div>
</template>

<script setup>

import { gsap } from "gsap";
    
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { onMounted } from "vue";

import testCardCom from "./testCardCom.vue";

gsap.registerPlugin(ScrollTrigger);

let comandInfo = [{name: "ghdbfjs", imgSrc: "afssdf", info: "dsfssd", position: "fdsfdsfdsfsdguyhfbguyregvhv hvghefv hufe whvhdfsghjv"}]

onMounted(() => {
    gsap.from(".titleBlockDiv__aboutUs", {
        scrollTrigger: {
            trigger: ".aboutUs-Block",
            start: "5% bottom",
            markers: true
        },
        x: -100,
        opacity: 0,
        duration: 1
    })
})
</script>