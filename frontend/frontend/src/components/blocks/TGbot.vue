<template>
    <div class="containerTGBOT__block">
        <h1>TELEGRAM-БОТ</h1>
        <p>Ваш помощник в поиске нужного тура </p>
        <button @click="urlOnClick_TG()" style="align-items: center;">
            <img src="/public/tg_icon.png" style="height: 10px;">
            Открыть
        </button>
    </div>
</template>

<style>
.containerTGBOT__block {
    text-align: center;
    align-content: center;
    height: 70vh;
}
</style>

<script setup>
import { gsap } from "gsap";
    
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { onMounted } from "vue";

gsap.registerPlugin(ScrollTrigger);


onMounted(() => {
    gsap.from(".containerTGBOT__block", {
        scrollTrigger: {
            trigger: ".containerTGBOT__block",
            start: "20% bottom"
        },
        y: 100,
        opacity: 0,
        duration: 1
    })
})


const urlOnClick_TG = () => {
    window.open("https://t.me/celebratelifetravel_bot")
}
</script>