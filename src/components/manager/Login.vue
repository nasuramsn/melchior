<template>
  <div class="managerlogin">
    <v-container>
      <v-form>
        <v-row>
          <v-col cols="2"></v-col>
          <v-col cols="10">
            <div class="title">Manager Login</div>
          </v-col>
          <v-col cols="2"></v-col>
        </v-row>
        <v-row>
          <v-col cols="2"></v-col>
          <v-col cols="5">
            <v-text-field label="login" single-line></v-text-field>
          </v-col>
          <v-col cols="5">
            <div class="items">password</div>
          </v-col>
          <v-col cols="2"></v-col>
        </v-row>
      </v-form>
    </v-container>
  </div>
</template>

<script>
export default {
  name: "ManagerLogin"
};
</script>

<style scoped>
</style>