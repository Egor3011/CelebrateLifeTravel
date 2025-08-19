<template>
  <div class="tour-program-block container">
    <h2 class="block-title">Программа тура</h2>
    <div class="accordion-list">
      <AccordionItem
        v-for="(item, index) in programItems"
        :key="index"
        :question="item.question"
        :answer="item.answer"
      />
    </div>
    <div class="price-block">
      <span class="price-text" style="font-family: 'Unbounded-Bold';">Цена тура {{ price }} рублей</span>
    </div>
  </div>
</template>

<script>
import AccordionItem from './AccordionItem.vue';

export default {
  name: 'TourProgramBlock',
  components: {
    AccordionItem,
  },
  props: {
    programItems: {
      type: Array,
      required: true,
      default: () => [],
    },
    price: {
      type: String,
      required: true,
    },
  },
};
</script>

<style scoped>
.tour-program-block {
  padding: 50px 20px;
  text-align: center;
  background-color: var(--vt-background); /* Light background to differentiate from hero block */
}

.block-title {
  font-size: 36px;
  font-weight: bold;
  margin-bottom: 40px;
  color: var(--vt-text-color); /* Dark text color */
  position: relative;
  display: inline-block;
}

.block-title::after {
  content: '';
  position: absolute;
  left: 0;
  bottom: -10px;
  width: 100%;
  height: 11px; /* Height of the SVG */
  background-image: url('/underline.svg'); /* Use the SVG image */
  background-size: contain;
  background-repeat: no-repeat;
  background-position: center;
}

.accordion-list {
  margin: 0 auto 40px auto;
}

.price-block {
  background-color: var(--vt-second-color); /* Yellow background for price */
  border-radius: 25px;
  padding: 15px 30px;
  display: inline-block;
  margin-top: 20px;
}

.price-text {
  font-size: 24px;
  font-weight: bold;
  color: var(--vt-text-color); /* Dark text color */
}

/* Responsive styles */
@media (max-width: 768px) {
  .block-title {
    font-size: 28px;
    margin-bottom: 30px;
  }

  .price-text {
    font-size: 20px;
  }

  .accordion-list {
    margin-bottom: 30px;
  }
}

@media (max-width: 480px) {
  .block-title {
    font-size: 24px;
    margin-bottom: 20px;
  }

  .price-text {
    font-size: 18px;
  }

  .price-block {
    padding: 10px 20px;
  }
}
</style>
