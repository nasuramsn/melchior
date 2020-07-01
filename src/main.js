import Vue from "vue";
import App from "./App.vue";

import router from "./router";
import vuetify from './plugins/vuetify';

import ConstScreen from "./consts/screen";

Vue.config.productionTip = false;

new Vue({
  render: (h) => h(App),
  vuetify,
  router,
  ConstScreen
}).$mount("#app");
