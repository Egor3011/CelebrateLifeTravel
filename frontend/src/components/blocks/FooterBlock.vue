<template>
  <footer class="app-footer">
    <div class="h1MainText__footer">
        <h1 style="color: var(--vt-second-color);">CELEBRATE LIFE TRAVEL</h1>
    </div>
    <div class="footer-content">

      <div class="footer-section navigation">
        <h3>Мы в социальных сетях</h3>
        <ul>
          <li>
            <a href="https://instagram.com/kate_cl_travel?igshid=YmMyMTA2M2Y=" class="links_sites">
              <img src="/public/icons/instagram.png" alt="">
              <h3 style="color: #0073FF;">Instagram</h3>
            </a>
          </li>
          <li>
            <a href="https://t.me/celebrate_life_travel" class="links_sites">
              <img src="/public/icons/tg.png" alt="">
              <h3 style="color: #0073FF;">Telegram</h3>
            </a>
          </li>
          <li>
            <a href="https://vk.com/celebratelifetravel" class="links_sites">
              <img src="/public/icons/vk.png" alt="">
              <h3 style="color: #0073FF;">VK</h3>
            </a>
          </li>
        </ul>
      </div>
      
      <div class="footer-section navigation">
        <h3>Контакты</h3>
        <p>Почта: <a href="mailto:silisheva92@mail.ru">silisheva92@mail.ru</a></p>
        <p>Менеджер: <a href="tel:79647272870">+7 964 727-28-70</a></p>
        <ul>
          <li><a href="https://wa.me/79647272870" class="link_blue">WhatsApp</a></li>
        </ul>
        <p>Директор: <a href="tel:79816989974">+7 981 698-99-74</a></p>
        <ul>
          <li><a href="https://wa.me/79816989974" class="link_blue">WhatsApp</a></li>
          <li><a href="https://t.me/+79816989974" class="link_blue">Telegram</a></li>
        </ul>
      </div>

      <div class="footer-section legal-info">
        <h3>Юридическая информация</h3>
        <p>ИП Силищева Е.Д.</p>
        <p>ИНН: 741709868650</p>
        <p>ОГРНИП: 321508100199293</p>
        <p>Рассчетный счет: 40802810100004028266</p>
        <p>БИК банка: 044525974</p>
        <p>Банк: АО "ТИНЬКОФФ БАНК"</p>
        <p>142438 Московская область, г. Ногинск, п.Новостройка д19, кв44</p>
        <p>Директор: Силищева Екатерина Дмитриевна</p>
        <h3>Документы</h3>
        <ul>
          <li><a href="/documents#ip_info" class="link_blue">Данные ИП</a></li>
          <li><a href="/documents#politika_konf" class="link_blue">Политика конфиденциальности</a></li>
          <li><a href="/documents#oferta" class="link_blue">Договор-оферта</a></li>
          <li><a href="/documents#dogovor" class="link_blue">Договор</a></li>
          <li><a href="/documents#efrt" class="link_blue">Выписка из ЕФРТ</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p style="opacity: 0.5; font-size: 14px;">* Instagram — принадлежит компании Meta, запрещённой на территории РФ</p>
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
  color: #0073FF;
  text-decoration: underline;
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

.links_sites {
  display: flex;
  align-items: center;
}

.links_sites img {
  width: 25px;
  height: 25px;
  margin-right: 10px;
}
</style>
