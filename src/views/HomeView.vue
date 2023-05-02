<template>
  <form>
    <v-text-field
      v-model="this.name"
      :counter="10"
      :error-messages="this.name"
      label="Name"
    ></v-text-field>
    <v-text-field label="Password" type="input"></v-text-field>
    <v-btn>Submit</v-btn>
  </form>
</template>
<script>
export default {
  name: "HomeView",
  data() {
    return {
      name: null,
    };
  },
  components: {},
  computed: {},
  methods: {},
};
</script>
