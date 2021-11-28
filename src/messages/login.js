import Vue from 'vue'
import VueI18n from 'vue-i18n'

const messages = {
    "ja": {
        "screen": {
            "manage_screen": "管理画面"
        },
        "message": {
            "no_input": "%sが入力されていません"
        }
    }
}

Vue.use(VueI18n);

export const i18n = new VueI18n({
    locale: 'ja',
    messages,
});