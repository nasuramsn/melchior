<template>
  <div class="globalheader">
    <v-container>
      <v-row>
        <v-col cols="2"></v-col>
        <v-col cols="10">
          <div class="header-title">Melchior</div>
        </v-col>
        <v-col cols="2"></v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  name: "GlobalHeader"
};
</script>

<style scoped>
.header-title {
  font-family: "Courier New", Courier, monospace;
  font-size: 16px;
  color: red;
}
</style>