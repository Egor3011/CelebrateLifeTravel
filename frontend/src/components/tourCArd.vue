<script setup>

const props = defineProps({
    title: String,
    imgSrc: String,
    info: String,
    link: String
})

const urlOnClick = (url) => {
    window.open("/tours?tour=" + url)
}

const openUrlTG = () => {
  window.open("https://t.me/celebratelifetravel_bot?start", '_blank')
}
</script>


<template>
    <div class="container__tourCard">
        <img :src="props.imgSrc" alt="" style="width: 100%; border-radius: 20px;">
        <h3>{{ props.title }}</h3>
        <p class="textP__tourCard">{{props.info}}</p>
        <div class="learnMoreButton_block">
            <button @click="urlOnClick(props.link)" class="learnMoreButton_1">Подробнее</button>
            <button @click="openUrlTG" class="learnMoreButton_2">Забронировать</button>
        </div>
    </div>
</template>

<style>
.container__tourCard {
    width: auto;

    padding: 20px;

    border-radius: 20px;
    box-shadow: 0px 0px 10px var(--vt-shadow-color);
}

.textP__tourCard {
    font-size: 12px;
}

.learnMoreButton_1 {
    margin-right: 5px;
    font-size: 10px;
}

.learnMoreButton_2 {
    font-size: 10px;
    border: 2px solid var(--vt-second-color);
    background: none;
}

@media(max-width: 1024px) {
    .container__tourCard {
        padding: 10px;
    }
    .learnMoreButton_block {
        text-align: center;
    }
    .learnMoreButton_1 {
        margin-right: 0;
    }
}
</style>