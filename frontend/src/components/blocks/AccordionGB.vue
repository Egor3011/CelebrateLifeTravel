<template>
  <div class="accordion-item">
    <div class="accordion-header" @click="toggleAccordion">
      <h3 class="accordion-question">{{ question }}</h3>
      <div :class="['accordion-icon', { 'is-open': isOpen }]">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M12 4V20" stroke="#000000" stroke-width="2" stroke-linecap="butt" stroke-linejoin="round"/>
          <path d="M4 12H20" stroke="#000000" stroke-width="2" stroke-linecap="butt" stroke-linejoin="round"/>
        </svg>
      </div>
    </div>
    <div :class="['accordion-content', { 'is-open': isOpen }]">
      <p v-for="el in items">{{ el }}</p>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    question: {
      type: String,
      required: true
    },
    items: {
        type: Array,
        default: () => [],
    }
  },
  data() {
    return {
      isOpen: false
    };
  },
  methods: {
    toggleAccordion() {
      this.isOpen = !this.isOpen;
    }
  }
};
</script>

<style scoped>
.accordion-item {
  background-color: #fff;
  border-radius: 30px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  margin-bottom: 16px;
  overflow: hidden;
}

.accordion-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 24px;
  cursor: pointer;
  background-color: #fff;
}

.accordion-header:hover {
  background-color: #f9f9f9;
}

.accordion-question {
  margin: 0;
  text-align: start;
  font-size: 18px;
  font-weight: bold;
  color: #333;
}

.accordion-icon {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 24px; /* Set explicit width and height to match SVG */
  height: 24px;
  transition: transform 0.3s ease;
}

.accordion-icon.is-open {
  transform: rotate(45deg);
}

.accordion-content {
  padding: 0 24px;
  border-top: 1px solid #eee;
  font-size: 16px;
  line-height: 1.6;
  max-height: 0;
  overflow: hidden;
  text-align: start;
  transition: max-height 0.5s linear, padding 0.5s linear;
}

.accordion-content.is-open {
  max-height: 500px; /* Adjust this value based on your content's maximum height */
  padding: 16px 24px;
}
</style>
