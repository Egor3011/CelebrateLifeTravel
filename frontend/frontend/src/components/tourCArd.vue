<script setup>

const props = defineProps({
    title: String,
    imgSrc: String,
    info: String,
    link: String
})

const urlOnClick = (url) => {
    window.open(url)
}
</script>


<template>
    <div class="container__tourCard">
        <img :src="props.imgSrc" alt="" style="width: 100%; border-radius: 20px;">
        <h3>{{ props.title }}</h3>
        <p class="textP__tourCard">{{props.info}}</p>
        <button @click="urlOnClick(props.link)">Подробнее</button>
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

@media(max-width: 1024px) {
    .container__tourCard {
        padding: 10px;
    }
}
</style>