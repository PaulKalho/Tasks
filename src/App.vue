<template>
  <v-app>
    <v-app-bar color="primary" dark app>
      <v-toolbar-title>ToDo</v-toolbar-title>
      <v-spacer></v-spacer>
    </v-app-bar>
    <v-main class="section" app>
      <v-container>
        <router-view />
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "App",

  components: {},

  data: () => ({
    //
  }),
};
</script>
