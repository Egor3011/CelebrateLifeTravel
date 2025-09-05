<template>
  <div class="question-block-container">
    <div class="question-block">
      <div class="content-section">
        <h2 style="margin-top: 0;">ОСТАЛИСЬ ВОПРОСЫ?</h2>
        <form>
          <button type="submit" class="submit-button" @click="openUrl">Оставить заявку</button>
        </form>
      </div>
      <div class="image-section">
        <img src="https://clt.s3.cloud.ru/photos/perezaGruzia/8" alt="Landscape with person in national attire" />
      </div>
    </div>
  </div>
</template>

<script setup>


const openUrl = () => {
  window.open("https://t.me/celebratelifetravel_bot?start", '_blank')
}
</script>

<style scoped>
.question-block-container {
  background-image: url('https://clt.s3.cloud.ru/photos/perezaGruzia/4'); /* Use your desired background image */
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
  background-color: rgba(0, 0, 0, 0.5); /* Dark overlay for text readability */
  height: 100vh;
  width: 100vw;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0;
  margin: 0;
}

.question-block {
    background: rgba(0, 0, 0, 0.1);
    backdrop-filter: blur(10px); /* Slightly transparent white for the form container */
  
  border: 2px solid var(--vt-text2-color);
  border-radius: 20px;

  box-shadow: 0 0 30px rgba(0, 0, 0, 0.3);
  display: flex;
  overflow: hidden;
  max-width: 1000px;
  width: 90%; /* Adjust width for better responsiveness */
  max-height: 90vh; /* Limit height to prevent overflow on smaller screens */
  z-index: 1;
}

.content-section {
  flex: 1;
  padding: 40px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.content-section h2 {
  font-family: 'Unbounded-Bold';
  color: var(--vt-background-color);
  font-size: 2em;
  margin-bottom: 20px;
}

.content-section p {
  font-family: 'Montserrat';
  font-size: 0.9em;
  margin-bottom: 30px;
}

.input-field {
  width: calc(100% - 20px);
  padding: 5px 10px;
  margin-bottom: 20px;
  border: 1px solid var(--vt-shadow-color);
  border-radius: 15px;
  font-family: 'Montserrat';
  font-size: 1em;
  color: var(--vt-text-color);
  background-color: #f8f8f8;
}

.input-field::placeholder {
  color: var(--vt-text-h-color);
}

.checkbox-container {
  display: flex;
  align-items: center;
  margin-bottom: 25px;
}

.checkbox-container input[type="checkbox"] {
  margin-right: 10px;
  margin-top: 5px; /* Align checkbox with text */
  min-width: 18px;
  min-height: 18px;
}

.checkbox-container label {
  font-family: 'Montserrat';
  font-size: 0.8em;
  line-height: 1.4;
}

.submit-button {
  width: 100%;
  padding: 15px;
  font-family: 'Unbounded-Bold';
  font-size: 1.2em;
  border: none;
  box-shadow: none;
  
}

.image-section {
  flex: 1;
  background-color: #f0f0f0;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
}

.image-section img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

@media (max-width: 768px) {
  .question-block {
    flex-direction: column;
    box-shadow: none;
    border-radius: 20px;
  }

  .content-section {
    padding: 20px;
  }

  .content-section h2 {
    font-size: 1.8em;
    text-align: center;
  }

  .content-section p {
    text-align: center;
  }

  .image-section {
    display: none; /* Hide image on mobile */
  }

  .question-block-container {
    padding: 0;
  }
}

@media(max-width: 1024px) {
  .checkbox-container input[type="checkbox"] {
    width: 10px;
    height: 10px;
  }
}

.question-block {
    color: #FFFFFF;
}
</style>
