// import http from "../http_commons";
import axios from "axios";
import settings from "../consts/common";

class ManagerServices {
  login(data) {
    axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
    axios.defaults.xsrfCookieName = "csrftoken";
    axios.defaults.withCredential = true;

    let csrftoken = this.getCookie("csrftoken");
    // http.headers.post["X-CSRFTOKEN"] = csrftoken;
    var headers = {
      "Content-Type": "application/json",
      "X-Requested-With": "XMLHttpRequest",
      "X-CSRFTOKEN": csrftoken,
    };

    // return http.post("/melchior/api/manager/login/", data, {
    return axios.post(
      settings.systemSettings.pythonHostUrl + "/melchior/api/manager/login/",
      data,
      {
        headers: headers,
      }
    );
  }

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
export default new ManagerServices();
