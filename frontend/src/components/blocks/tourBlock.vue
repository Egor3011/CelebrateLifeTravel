<script setup>
import { gsap } from "gsap";
    
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { onMounted } from "vue";

gsap.registerPlugin(ScrollTrigger);

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
})

</script>

<template>
    <div class="container">
        <div class="titleBlockDiv__tourBlock">
            <span class="headH1">Каталог туров</span>
            <h2 class="titleBlock titleBlockDiv__tourBlock__h1" style="width: 500px;">Наши направления</h2>
        </div>
    </div>
</template>