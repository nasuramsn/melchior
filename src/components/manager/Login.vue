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
            <v-text-field v-model="loginId" label="login" single-line></v-text-field>
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
            <v-btn color="success" dark v-on:click="doLogin">Login</v-btn>
          </v-col>
          <v-col cols="2">
            <v-btn color="primary" dark v-on:click="doCheckCsrf">Sign In</v-btn>
          </v-col>
          <v-col cols="6"></v-col>
        </v-row>
      </v-form>
    </v-container>
  </div>
</template>

<script>
// import ManagerServices from "../../services/manager";
import { i18n } from "../../messages/login";

import axios from "axios";
// import settings from "../../consts/common";

export default {
  name: "ManagerLogin",
  data() {
    return {
      show1: false,
      loginId: "",
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
    this.manage_screen = i18n.tc("screen.manage_screen");
  },
  methods: {
    doCheckCsrf: function() {
      axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
      axios.defaults.xsrfCookieName = "csrftoken";
      axios.defaults.withCredentials = true;

      let csrftoken = this.getCookie("csrftoken");
      var headers = {
        "Content-Type": "application/json",
        // "X-Requested-With": "XMLHttpRequest",
        "X-CSRFTOKEN": csrftoken
      };

      axios
        .get(
          "http://localhost:8010/melchior/api/manager/checkcsrf/",
          {},
          {
            headers: headers
          }
        )
        .then(res => {
          alert(res);
        })
        .catch(err => {
          alert(err);
        });

      return;
    },
    doLogin: function() {
      // check loginId and password
      if (this.loginId.length < 1) {
        alert(i18n.tc("message.no_input"));
        return;
      } else if (this.password.length < 1) {
        alert(i18n.tc("message.no_input"));
        return;
      } else {
        // check CORS => this will do in vue.config.js
        // do login
        axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
        axios.defaults.xsrfCookieName = "csrftoken";
        axios.defaults.withCredentials = true;

        let csrftoken = this.getCookie("csrftoken");
        var headers = {
          "Content-Type": "application/json",
          "X-Requested-With": "XMLHttpRequest",
          "X-CSRFTOKEN": csrftoken
        };

        let params = new URLSearchParams();
        params.append("loginid", this.loginId);
        params.append("password", this.password);

        alert(this.getCookie("csrftoken"));

        // ManagerServices.login(params)
        axios
          .post("http://localhost:8010/melchior/api/manager/login/", params, {
            headers: headers
          })
          .then(res => {
            alert(res);
          })
          .catch(err => {
            alert(err);
          });

        return;
      }
    },
    getCookie(data) {
      var name = data + "=";
      var decodedCookie = decodeURIComponent(document.cookie);
      var ca = decodedCookie.split(";");
      for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == " ") {
          c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
          return c.substring(name.length, c.length);
        }
      }
      return "";
    }
  }
};
</script>

<style scoped></style>
