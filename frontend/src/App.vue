<template>
  <div id="app">{{ message }}</div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import api from "./lib/api";
import liff from "./lib/liff";

@Component
export default class App extends Vue {
  message = "初期化中";

  async created() {
    // TODO:LIFF IDを設定する
    const isInit = await liff.init('');
    if (isInit) {
      if (!liff.isLoggedIn()) {
        liff.login();
      } else {
        const idToken = liff.idToken();
        this.message = await api.postUserInfo(idToken);
      }
    } else {
      this.message = "初期化に失敗しました";
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
