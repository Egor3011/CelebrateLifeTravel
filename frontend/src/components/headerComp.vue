<template>
    <div class="headerContainer container">
        <h4 style="margin: 0; font-size: 18px; font-family: 'Unbounded-Medium';">CELEBRATE LIFE TRAVEL</h4>
        <nav>
          <RouterLink class="routerLink" to="/">Home</RouterLink>
          <RouterLink class="routerLink" to="/about">About</RouterLink>
        </nav>
    </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';
</script>

<style>
.headerContainer {
    padding: 10px 30px;

    align-content: center;
    display: flex;
    justify-content: space-between;

    position: absolute;
    width: 80vw;


    color: #FFFFFF;

    background: rgba(255, 255, 255, 0.3);
    border: 1px solid #FFFFFF;

    border-radius: 25px;
}

.routerLink {
    color: #FFF;
    transition: 0.2s;
}

.routerLink:hover {
    color: var(--vt-text-h-color);
    transition: 0.3s;
}
</style>