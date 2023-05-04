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
        <v-btn min-width="200">Log-in</v-btn>
      </form>
    </v-card>
  </v-container>
</template>
<script>
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
  methods: {},
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
