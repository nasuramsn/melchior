<template>
  <div class="managerlogin">
    <v-container>
      <v-form>
        <v-row>
          <v-col cols="2"></v-col>
          <v-col cols="8">
            <div class="title">{{ manage_screen }}</div>
          </v-col>
          <v-col cols="2"></v-col>
        </v-row>
        <v-row>
          <v-col cols="2"></v-col>
          <v-col cols="5">
            <v-text-field label="login" single-line></v-text-field>
          </v-col>
          <v-col cols="5"></v-col>
        </v-row>
        <v-row>
          <v-col cols="2"></v-col>
          <v-col cols="5">
            <v-text-field
              v-model="password"
              :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
              :rules="[rules.required, rules.min]"
              :type="show1 ? 'text' : 'password'"
              name="input-10-1"
              label="Normal with hint text"
              hint="At least 8 characters"
              counter
              @click:append="show1 = !show1"
            ></v-text-field>
          </v-col>
          <v-col cols="5"></v-col>
        </v-row>
        <v-row>
          <v-col cols="2"></v-col>
          <v-col cols="2">
            <v-btn color="success" dark>Login</v-btn>
          </v-col>
          <v-col cols="2">
            <v-btn color="primary" dark>Sign In</v-btn>
          </v-col>
          <v-col cols="6"></v-col>
        </v-row>
      </v-form>
    </v-container>
  </div>
</template>

<script>
import ScreenConsts from "../../consts/screen";

export default {
  name: "ManagerLogin",
  data() {
    return {
      show1: false,
      password: "",
      rules: {
        required: value => !!value || "Required.",
        min: v => v.length >= 8 || "Min 8 characters",
        emailMatch: () => "The email and password you entered don't match"
      },
      manage_screen: ""
    };
  },
  created: function() {
    this.manage_screen = ScreenConsts.SCREEN_CONSTS.MANAGE_SCREEN;
  }
};
</script>

<style scoped></style>
