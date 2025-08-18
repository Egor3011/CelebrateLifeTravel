<script>

const props = defineProps({
    nameTitle: String,
    position: String,
    imgSrc: String,
    info: String
})
</script>

<template>
    <div class="commandContainerCard">
        <div>
            <img :src="props.imgSrc" alt="">
            <h3>{{ props.name }}</h3>
            <div class="lineInBox"></div>
            <h3>{{ props.position }}</h3>
        </div>
        <p>{{ props.info }}</p>
    </div>
</template>

<style>
.commandContainerCard {
    background: #FFFFFF;
    border: #FFFFFF;
    border-radius: 25px;
    box-shadow: 0px 0px 10px var(--vt-shadow-color);

    width: 520px;
    height: 500px;

    padding: 20px;
    display: flex;
}
</style>