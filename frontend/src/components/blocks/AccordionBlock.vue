<template>
    <div class="container">
        <div>
            <AccordionGB
                question="Что входит в стоимость?"
                :items="props.infoG"
            />
        </div>
        <div>
            <AccordionGB
                question="Что НЕ входит в стоимость?"
                :items="props.infoB"
            />
        </div>
    </div>
</template>

<script setup>
import { defineProps, onMounted } from 'vue';
import AccordionGB from './AccordionGB.vue';


const props = defineProps({
  infoG: {
    type: Array,
    required: true,
  },
  infoB: {
    type: Array,
    required: true,
  }
});
</script>