<template>
  <div class="globalheader">
    <v-container>
      <v-row>
        <v-toolbar class="header-back" color="rgba(50, 100, 205, 1.0)">
          <v-toolbar-title class="header-title">
            <v-col cols="2"></v-col>
            <v-col cols="10">
              <div>Melchior</div>
            </v-col>
            <v-col cols="2"></v-col>
          </v-toolbar-title>
        </v-toolbar>
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
.header-back {
  display: flex;
  justify-content: center;
  text-align: center;
}

.header-title {
  font-family: "Arial, Helvetica, sans-serif";
  font-size: 20px;
  color: white;
  text-align: center;
}
</style>