<template>
    <div class="aboutUs-Block">
        <div>
            <span class="headH1 komand--AboutUs">Команда</span>
            <h2 class="titleBlock" style="width: 500px;">CELEBRATE LIFE TRAVEL  – это двигатель ваших приключений</h2>
        </div>
        <div style="text-align: center;">
            <h2>Наша команда</h2>
        </div>
    </div>
</template>

<script setup>
import { gsap } from "gsap";
    
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { onMounted } from "vue";

gsap.registerPlugin(ScrollTrigger);

onMounted(() => {
    const tl = gsap.timeline()
    tl.from(".komand--AboutUs", {
        x: -100,
        opacity: 0,
        duration: 0.5
    })
    tl.from(".titleBlock", {
        x: -100,
        opacity: 0,
        duration: 1
    })
})
</script>