<template>
  <div class="team-card-container">
    <div class="photo-frame" :style="{ transform: 'rotate(' + props.rotation + 'deg)' }">
      <img src="/public/pick.png" alt="Paperclip" class="paperclip" />
      <img :src="props.imageUrl" alt="Team member" class="team-photo" />
    </div>
    <div class="text-content">
      <h3>{{ props.title }}</h3>
      <ul>
        <li v-for="(item, index) in props.items" :key="index">{{ item }}</li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { defineProps } from 'vue';

const props = defineProps({
  imageUrl: {
    type: String,
    required: true,
  },
  rotation: {
    type: Number,
    default: 0,
  },
  title: {
    type: String,
    required: true,
  },
  items: {
    type: Array,
    default: () => [],
  },
});
</script>

<style scoped>
.team-card-container {
  background-color: var(--vt-background);
  border-radius: 20px;
  box-shadow: 0 0px 10px rgba(0, 0, 0, 0.1);
  max-width: 350px;
  margin: 20px auto;
  text-align: left;
}

.photo-frame {
  position: relative;
  background-color: var(--vt-second-color);
  padding: 15px;
  margin: 20px 15px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  /* The rotation is applied via inline style from props */
}

.paperclip {
  position: absolute;
  top: -15px;
  left: 50%;
  transform: translateX(-50%) rotate(25deg); /* Slight rotation for paperclip */
  width: 40px;
  height: auto;
  z-index: 2;
}

.team-photo {
  width: 100%;
  height: auto;
  display: block;
  border-radius: 10px;
}

.text-content {
  padding: 20px;
}

.text-content h3 {
  font-family: 'Unbounded-Bold';
  color: var(--vt-text-color);
  font-size: 1.5em;
  margin-top: 0;
  margin-bottom: 15px;
  text-align: center;
}

.text-content ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.text-content li {
  font-family: 'Montserrat';
  color: var(--vt-text-color);
  font-size: 0.95em;
  line-height: 1.6;
  margin-bottom: 8px;
  padding-left: 15px; /* Indent bullet points */
  position: relative;
}

@media (max-width: 768px) {
  .team-card-container {
    margin: 15px auto;
  }

  .photo-frame {
    margin: 15px;
    padding: 10px;
  }

  .text-content {
    padding: 15px;
  }

  .text-content h3 {
    font-size: 1.3em;
  }

  .text-content li {
    font-size: 0.9em;
  }
}
</style>
