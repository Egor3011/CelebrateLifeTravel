<script setup>
import { gsap } from "gsap";
    
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { onMounted } from "vue";

gsap.registerPlugin(ScrollTrigger);

onMounted(() => {
    gsap.from(".titleBlockDiv__FAQBlock", {
        scrollTrigger: {
            trigger: ".titleBlockDiv__FAQBlock",
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
        <div class="titleBlockDiv__FAQBlock">
            <span class="headH1">FAQ</span>
            <h2 class="titleBlock titleBlockDiv__FAQBlock__h1" style="width: 500px;">ОТВЕТЫ НА ЧАСТЫЕ ВОПРОСЫ</h2>
        </div>
    </div>
</template>

<style>
.titleBlockDiv__FAQBlock {
    margin-top: 100px;
}

@media(max-width: 1024px) {
    .titleBlockDiv__FAQBlock {
        width: 60vw;
    }
}
</style>