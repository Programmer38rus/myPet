import Vue from 'vue';
import VueRouter from 'vue-router';
import Family from '../components/family.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Family',
    component: Family,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
