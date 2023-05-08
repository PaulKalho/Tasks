<!-- LOGIN -->
<template>
  <v-container class="main">
    <v-card min-width="300" min-height="300" class="login-card">
      <form>
        <v-text-field v-model="name" label="Name"></v-text-field>
        <v-text-field
          label="Password"
          type="input"
          v-model="passwort"
        ></v-text-field>
        <v-btn min-width="200" @click="login">Log-in</v-btn>
      </form>
    </v-card>
  </v-container>
</template>
<script>
import { api } from "@/plugins/axios";
export default {
  name: "HomeView",
  data() {
    return {
      name: null,
      passwort: null,
    };
  },
  components: {},
  computed: {},
  methods: {
    login() {
      api
        .post("/token/", { username: this.name, password: this.passwort })
        .then((response) => {
          api.defaults.headers.common[
            "Authorization"
          ] = `Bearer ${response.access}`;
        });
    },
  },
};
</script>
<style>
.main {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.login-card {
  display: flex;
  justify-content: space-around;
  align-items: center;
}
</style>
