<template>
  <div id="app">
    <GlobalHeader />
    <router-view />
    <GlobalFooter />
  </div>
</template>

<script>
import GlobalHeader from "./components/GlobalHeader";
import GlobalFooter from "./components/GlobalFooter";

export default {
  name: "app",
  components: {
    GlobalHeader,
    GlobalFooter
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
