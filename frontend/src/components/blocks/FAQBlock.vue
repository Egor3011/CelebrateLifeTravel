<script setup>
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import axios from "axios";

import { ref } from "vue";
import { onMounted } from "vue";
import AccordionItem from "./AccordionItem.vue";

const faqBlock = ref([])

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

    axios.get("https://be67bc91a5069fe3.mokky.dev/faq").then((res) => {
        faqBlock.value = res.data
    })
})

</script>

<template>
    <div class="container">
        <div class="titleBlockDiv__FAQBlock">
            <span class="headH1">FAQ</span>
            <h2 class="titleBlock titleBlockDiv__FAQBlock__h1">ОТВЕТЫ НА ЧАСТЫЕ ВОПРОСЫ</h2>
        </div>

        <div class="containerFAQ__blocks">
            <AccordionItem
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
    margin-top: 60px;
}

@media(max-width: 1024px) {
    .titleBlockDiv__FAQBlock {
        width: 100%;
    }
}



/*тут классы для кнопок*/

.FAQButton__container {
    padding: 0px 40px;
    margin: 30px;

    align-content: center;

    border-radius: 20px;
    box-shadow: 0 0 10px var(--vt-shadow-color);

    overflow: hidden;
    transition: 1s;
}

.FAQButton__container:hover {
    transition: 1s;

    .FAQButton__mainText {
        display:block;
    }
}

.FAQButton__titleText {
    margin: 5px 0;
}

.FAQButton__mainText:not(.active) {
    display: none;
}
</style>