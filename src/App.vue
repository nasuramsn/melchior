<template>
  <v-app>
    <v-content>
      <GlobalHeader />
      <router-view />
      <GlobalFooter />
    </v-content>
  </v-app>
</template>

<script>
import GlobalFooter from "./components/GlobalFooter";
import GlobalHeader from "./components/GlobalHeader";

export default {
  name: "App",
  components: {
    GlobalFooter,
    GlobalHeader
  },
  data: () => ({
    //
  })
};
</script>
