<script setup>
import { RouterLink } from 'vue-router';
import AboutUs from '@/components/blocks/AboutUs.vue';
import startImage from '@/components/blocks/startImage.vue';
import TGbot from '@/components/blocks/TGbot.vue';
import tourBlock from '@/components/blocks/tourBlock.vue';
import FAQBlock from '@/components/blocks/FAQBlock.vue';
import reviewsBlock from '@/components/blocks/reviewsBlock.vue';
import formMore from '@/components/blocks/formMore.vue';
import QuestionBlock from '@/components/blocks/QuestionBlock.vue';
import ValuesBlock from '@/components/blocks/ValuesBlock.vue';
import HeroTourBlock from '@/components/blocks/HeroTourBlock.vue';
import TeamCard from '@/components/blocks/TeamCard.vue';
import preimushestva from '@/components/blocks/preimushestva.vue';

import { onMounted, watch } from 'vue';

onMounted(() => {
    openUrl()
})

const openUrl = () => {
    let hash = window.location.hash
    if(hash) {
      const hashNew = hash.slice(1)
      const el = document.getElementById(hashNew);
      el.scrollIntoView();
      el.scrollIntoView();
      el.scrollIntoView({behavior: "smooth"});
      setTimeout(() => {
        const el1 = document.getElementById(hashNew);
        el1.scrollIntoView({behavior: "smooth"});

      }, 500)

    }
}


const valuesCards = [
  {
    title: 'Комфорт',
    description: 'Все наши туры - про комфорт, удобство, внимание к деталям. Мы не допускаем, чтобы на отдыхе ваши впечатления омрачались некачественным жильем или грубым водителем. Мы тщательно подбираем лучшие условия для наших гостей. Ваш комфортный и качественный отдых - наш главный приоритет.'
  },
  {
    title: 'Насыщенность программ',
    description: 'В наших турах нет пробелов и пустых бестолковых дней. Все дни максимально заполнены экскурсиями, локациями и различными активностями. Каждый день не похож на предыдущий. Да, возможно где-то вы не выспитесь, где-то  немного устанете, но вы точно кайфанете от такого активного отдыха и захотите еще!',
  },
  {
    title: 'Крутые гиды',
    description: 'Наши гиды - наша гордость. В каждом направлении мы выбрали лучших из лучших. Гид - один из самых ключевых якорей, от которого зависит атмосфера, настроение и впечатление от самого тура. Поэтому мы не берём кого попало, а работаем только с профессионалами своего дела, которые влюблены в свою работу и горят тем, чем они занимаются.',
  },
  {
    title: 'Лучшие цены',
    description: 'Оптимальное соотношение цены и качества. Высокий уровень сервиса и комфорта по разумной цене. Достойное размещение, питание, комфортный трансфер, насыщенные экскурсии без переплат и посредников.',
  },
  {
    title: 'Оплата по договору',
    description: 'Наша компания зарегистрирована в реестре турагентов, и с каждым путешественником мы заключаем договор перед внесением предоплаты. Никаких серых схем и подводных камней.',
  },
  {
    title: 'Сопровождение и поддержка',
    description: 'Мы проконсультируем и поможем вам в по любым вопросам: расскажем подробно про тур и его особенности, пришлем памятку по сборам, поможем выбрать оптимальный билет из вашего города, пришлем нашу подборку проверенных отелей, если вы решите прилететь до начала тура или остаться после.',
  }
];

import LineRoad from '@/components/blocks/LineRoad.vue';
</script>

<template>
  <main>
    <HeroTourBlock id="heroBlock_Home"/>

    <preimushestva id="about"/>

    <AboutUs/>

    <tourBlock id="katalog"/>

    <ValuesBlock :cards="valuesCards" id="plus"/>

    <LineRoad style="margin-top: 40px;"/>

    <reviewsBlock id="reviews"/>

    <QuestionBlock id="form"/>

    <TGbot v-show="false"/>
  </main>
</template>
