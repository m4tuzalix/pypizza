import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import Menu from '../views/Menu.vue';
import Summary from '../views/Summary.vue'
import {store} from '../store/index'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
  },
  {
    path: '/menu',
    name: 'menu',
    component: Menu,
  },
  {
    path: '/summary',
    name: 'summary',
    component: Summary,
    props:{
      final_orders: store.state.final_orders,
      order_value: store.state.order_value
    },
    meta:{
      allowed: !store.getters.empty_cart
    }
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue'),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach((to, from, next) => {
  if(to.fullPath === '/summary' && !to.meta.allowed){alert('your cart is empty'); return next({name:"home"})}
  next()
})

export default router;
