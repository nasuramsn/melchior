<template>
  <div class="globalfooter">
    <v-container>
      <v-footer class="footer-back">
        <div class="footer-title">(C) 2020 Surnivers</div>
      </v-footer>
    </v-container>
  </div>
</template>

<script>
export default {
  name: "GlobalFooter"
};
</script>

<style scoped>
.footer-back {
  display: flex;
  justify-content: center;
  text-align: center;
}

.footer-title {
  font-family: "Courier New", Courier, monospace;
  font-size: 18px;
  color: gray;
}
</style>