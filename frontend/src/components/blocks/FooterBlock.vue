<template>
  <footer class="app-footer">
    <div class="h1MainText__footer">
        <h1 style="color: var(--vt-second-color);">CELEBRATE LIFE TRAVEL</h1>
    </div>
    <div class="footer-content">
      
      <div class="footer-section navigation">
        <h3>Навигация</h3>
        <ul>
          <li><a href="#hero">Главная</a></li>
          <li><a href="#about">О нас</a></li>
          <li><a href="#tours">Туры</a></li>
          <li><a href="#faq">FAQ</a></li>
          <li><a href="#contact">Контакты</a></li>
        </ul>
      </div>

      <div class="footer-section legal-info">
        <p>ИП Силищева Е.Д.</p>
        <p>ИНН: 741709868650</p>
        <p>ОГРНИП: 321508100199293</p>
        <h3>Документы</h3>
        <ul>
          <li><a href="/documents#ip_info">Данные ИП</a></li>
          <li><a href="/documents#politika_konf">Политика конфиденциальности</a></li>
          <li><a href="/documents#oferta">Договор-оферта</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2023 Ваш сайт. Все права защищены.</p>
    </div>
  </footer>
</template>

<script setup>
</script>

<style scoped>
.app-footer {
  background-color: var(--vt-text-color);
  color: var(--vt-text2-color);
  padding: 40px 20px;
  border-top: 1px solid var(--vt-shadow-color);
}

.footer-content {
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
  max-width: 1200px;
  margin: 0 auto;
  padding-bottom: 20px;
}

.footer-section {
  flex: 1;
  min-width: 250px;
  margin: 10px;
}

.footer-section h3 {
  color: var(--vt-second-color);
  font-family: 'Unbounded-Bold';
  margin-bottom: 15px;
}

.footer-section p,
.footer-section li {
  font-family: 'Montserrat';
  font-size: 0.9em;
  line-height: 1.6;
}

.footer-section ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.footer-section a {
  color: var(--vt-text2-color);
  text-decoration: none;
  transition: color 0.3s ease;
}

.footer-section a:hover {
  color: var(--vt-second-color);
}

.footer-bottom {
  text-align: center;
  padding-top: 20px;
  border-top: 2px solid var(--vt-shadow-color);
  margin-top: 20px;
}

.footer-bottom p {
  font-family: 'Montserrat';
  font-size: 0.8em;
  color: var(--vt-text-h-color);
}

@media (max-width: 768px) {
  .footer-content {
    flex-direction: column;
    align-items: center;
  }

  .h1MainText__footer {
    text-align: center;
  }

  .footer-section {
    text-align: center;
  }
}
</style>
