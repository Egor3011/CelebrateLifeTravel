<template>
    <div class="headerContainer container">
        <h4 style="margin: 0; font-size: 18px; font-family: 'Unbounded-Medium';">CELEBRATE LIFE TRAVEL</h4>
        <nav>
          <RouterLink to="/">Home</RouterLink>
          <RouterLink to="/about">About</RouterLink>
        </nav>
    </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';
</script>

<style>
.headerContainer {
    padding: 0 30px;

    position: fixed;
    width: 80vw;
    height: 50px;

    align-content: center;

    color: #FFFFFF;

    background: rgba(255, 255, 255, 0.3);
    border: 1px solid #FFFFFF;

    border-radius: 25px;
}
</style>