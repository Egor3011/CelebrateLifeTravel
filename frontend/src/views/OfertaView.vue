<template>
  <div class="oferta-page">
    <h1 style="margin-top: 70px;">Документы</h1>
    <h2 class="docs_INFO" id="oferta">Договор-оферта</h2>
    <iframe src="/api/documents/oferta" class="pdf-viewer" frameborder="0"></iframe>

    <h2 class="docs_INFO" id="politika_konf">Политика конфиденциальности</h2>
    <iframe src="/api/documents/politika_konf" class="pdf-viewer" frameborder="0"></iframe>
    
    <h2 class="docs_INFO" id="ip_info">Информация по ИП</h2>
    <iframe src="/api/documents/skan_ip" class="pdf-viewer" frameborder="0"></iframe>

    <h2 class="docs_INFO" id="ip_info">Договор</h2>
    <iframe src="/api/documents/dogovor" class="pdf-viewer" frameborder="0"></iframe>

    <h2 class="docs_INFO" id="ip_info">Выписка из единого Федерального реестра турагентов</h2>
    <div class="container">
      <img src="https://clt.s3.cloud.ru/photos/ALL/tour_docs" style="width: 100%; height: auto;">
    </div>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';
</script>

<style scoped>
.oferta-page {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  min-height: calc(100vh - var(--header-height) - var(--footer-height)); /* Adjust header/footer height as needed */
}

.docs_INFO {
  color: var(--vt-text-color);
  font-family: 'Unbounded-Bold';
  text-decoration: underline;
  margin-bottom: 20px;
}

.pdf-viewer {
  width: 100%;
  max-width: 900px;
  height: 80vh; /* Adjust height as needed */
  border: 1px solid var(--vt-shadow-color);
}

@media (max-width: 768px) {
  .pdf-viewer {
    height: 60vh;
  }
}
</style>
