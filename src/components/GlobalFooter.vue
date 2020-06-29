<template>
  <div class="globalfooter">
    <v-container>
      <v-row>
        <v-col cols="2"></v-col>
        <v-col cols="10">
          <div class="footer-title">Copy Right by Surnivers</div>
        </v-col>
        <v-col cols="2"></v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  name: "GlobalFooter"
};
</script>

<style scoped>
.footer-title {
  font-family: "Courier New", Courier, monospace;
  font-size: 16px;
  color: blue;
}
</style>