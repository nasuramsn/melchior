import App from "./App.vue";
import Vue from "vue";

import router from "./router";
import vuetify from "./plugins/vuetify";

import settings from "./consts/common";

Vue.config.productionTip = false;

new Vue({
  render: (h) => h(App),
  vuetify,
  router,
  settings,
}).$mount("#app");
