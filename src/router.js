import Vue from "vue";
import Router from "vue-router";

import HelloWorld from "./components/HelloWorld.vue";
import ManagerLogin from "./components/manager/Login.vue";
import NotFound from "./components/NotFound.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    { path: "/manager/login", name: "ManagerLogin", component: ManagerLogin },
    { path: "/", name: "home", component: HelloWorld },
    { path: "*", name: "NotFound", component: NotFound },
  ],
});
