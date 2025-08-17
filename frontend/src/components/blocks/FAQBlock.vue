<script setup>
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

import { ref } from "vue";
import { onMounted } from "vue";
import Acardion from "./Acardion.vue";

const faqBlock = ref([{title: "kdskfjds", info: "ghbdtn nen nfrfz byaf"},{title: "kdskfjds", info: "ghbdtn nen nfrfz byaf"},{title: "kdskfjds", info: "ghbdtn nen nfrfz byaf"}])

gsap.registerPlugin(ScrollTrigger);

onMounted(() => {
    gsap.from(".titleBlockDiv__FAQBlock", {
        scrollTrigger: {
            trigger: ".titleBlockDiv__FAQBlock",
            start: "10% top"
        },
        x: -100,
        opacity: 0,
        duration: 1,
        delay: 0
    })
})

</script>

<template>
    <div class="container">
        <div class="titleBlockDiv__FAQBlock">
            <span class="headH1">FAQ</span>
            <h2 class="titleBlock titleBlockDiv__FAQBlock__h1" style="width: 500px;">ОТВЕТЫ НА ЧАСТЫЕ ВОПРОСЫ</h2>
        </div>

        <div class="containerFAQ__blocks">
            <Acardion
                v-for="(el, index) in faqBlock"
                :key="index"
                :question="el.title"
                :answer="el.info"
            />
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



/*тут классы для кнопок*/
</style>