<script setup>
const props = defineProps({
    nameTitle: String,
    position: String,
    imgSrc: String,
    info: String
})
</script>

<template>
    <div class="commandContainerCard">
        <img :src="props.imgSrc" class="img__cardCommand">
        <div>
            <h3 class="without__margin">{{props.nameTitle}}</h3>
            <div class="lineInBox"></div>
            <h3 class="without__margin position__cardCommand" style="opacity: 0.7;">{{props.position}}</h3>
        </div>
        <p class="infoP__cardCommand">{{props.info}}</p>
    </div>
</template>

<style>
.without__margin {
    margin: 0%;
}

.commandContainerCard {
    background: #FFFFFF;
    border: #FFFFFF;
    border-radius: 25px;
    box-shadow: 0px 0px 10px var(--vt-shadow-color);

    width: auto;
    height: auto;

    padding: 20px;
}

.infoP__cardCommand {
    font-size: 12px;
}

.position__cardCommand {
    font-size: 14px;
}

.lineInBox {
    width: 100%;
    height: 2px;

    border-radius: 1px;

    background: var(--vt-text-color);
}

.img__cardCommand {
    width: 100%;
    height: auto;

    border-radius: 20px;
}
</style>