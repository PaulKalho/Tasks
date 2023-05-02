import Vue from "vue";
import VueRouter from "vue-router";
import HomeView from "@/views/HomeView";
import AppView from "@/views/AppView";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Index",
    props: true,
    component: HomeView,
  },
  {
    path: "/app",
    name: "App",
    props: true,
    component: AppView,
  },
];

const router = new VueRouter({
  mode: "history",
  base: "/",
  routes,
});

export default router;
