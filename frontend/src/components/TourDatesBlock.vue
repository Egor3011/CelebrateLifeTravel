<template>
  <div class="tour-dates-block">
    <h2 class="block-title">Даты туров</h2>
    <div class="dates-grid">
      <div class="date-column" v-for="(monthData, monthName) in tourDates" :key="monthName">
        <h3 class="month-name" style="margin-top: 0;">{{ monthName }}</h3>
        <div class="days-list">
          <span 
            v-for="(days, index) in monthData"
            :key="index"
            :class="['day-range', { 'is-unavailable': days.unavailable }]">
            {{ days.range }}
          </span>
        </div>
      </div>
    </div>
    <button class="book-button" @click="scrolToForm">Забронировать тур</button>
  </div>
</template>

<script>
export default {
  name: 'TourDatesBlock',
  props: {
    tourDates: {
      type: Object,
      required: true,
      default: () => ({}),
    },
  },
  methods: {
    scrolToForm() {
        const el = document.getElementById("form");
        el.scrollIntoView({behavior: "smooth"});
    }
  }
};
</script>

<style scoped>
.tour-dates-block {
  padding: 50px 20px;
  text-align: center;
  background-color: var(--vt-background);
}

.block-title {
  font-size: 36px;
  font-weight: bold;
  margin-bottom: 40px;
  color: var(--vt-text-color);
}

.dates-grid {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 20px;
  margin-bottom: 40px;
}

.date-column {
  background-color: #fff;
  border-radius: 15px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  padding: 20px;
  width: 150px; /* Adjust width as needed */
  display: flex;
  flex-direction: column;
  align-items: center;
}

.month-name {
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 15px;
  color: var(--vt-text-color);
}

.days-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.day-range {
  font-size: 16px;
  color: var(--vt-text-color);
  padding: 5px 0;
}

.day-range.is-unavailable {
  color: #a0a0a0; /* Grey out unavailable dates */
  text-decoration: line-through;
}

.book-button {
  font-size: 20px;
}

/* Responsive styles */
@media (max-width: 768px) {
  .block-title {
    font-size: 28px;
  }

  .date-column {
    width: 120px;
    padding: 15px;
  }

  .month-name {
    font-size: 16px;
  }

  .day-range {
    font-size: 14px;
  }

  .book-button {
    font-size: 16px;
    padding: 12px 25px;
  }
}

@media (max-width: 480px) {
  .block-title {
    font-size: 24px;
  }

  .dates-grid {
    gap: 15px;
  }

  .date-column {
    width: 100px;
    padding: 10px;
  }

  .month-name {
    font-size: 14px;
  }

  .day-range {
    font-size: 12px;
  }

  .book-button {
    font-size: 14px;
    padding: 10px 20px;
  }
}
</style>
