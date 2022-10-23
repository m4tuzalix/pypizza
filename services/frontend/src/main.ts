import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import {store, key} from './store';
import BootstrapVue3 from 'bootstrap-vue-3'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue-3/dist/bootstrap-vue-3.css'
import "bootstrap";

const vue = createApp(App)

vue.use(store, key)
vue.use(router)
vue.use(BootstrapVue3)
vue.mount('#app');


