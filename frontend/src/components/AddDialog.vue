<template>
  <v-dialog persistent v-model="show" max-width="600">
    <v-card>
      <v-toolbar color="primary mb-5">
        <v-card-title>Todo hinzufügen</v-card-title>
      </v-toolbar>
      <v-card-text>
        <v-container>
          <v-row>
            <v-select
              v-model="model.groupId"
              label="Group"
              :items="groupNames"
              item-text="title"
              item-value="value"
            ></v-select>
          </v-row>
          <v-row>
            <v-text-field
              v-model="model.title"
              label="Titel"
              required
            ></v-text-field>
          </v-row>
          <v-row>
            <v-text-field
              v-model="model.description"
              label="Description"
            ></v-text-field>
          </v-row>
          <v-row>
            <v-menu
              ref="menu"
              v-model="menu"
              :close-on-content-click="false"
              :return-value.sync="model.deadline"
              transition="scale-transition"
              offset-y
              min-width="auto"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                  v-model="model.deadline"
                  label="Datum"
                  prepend-icon="mdi-calendar"
                  readonly
                  v-bind="attrs"
                  v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker v-model="model.deadline" no-title scrollable>
                <v-spacer></v-spacer>
                <v-btn text color="primary" @click="menu = false">
                  Cancel
                </v-btn>
                <v-btn
                  text
                  color="primary"
                  @click="$refs.menu.save(model.deadline)"
                >
                  OK
                </v-btn>
              </v-date-picker>
            </v-menu>
          </v-row>
        </v-container>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="red" text @click.stop="show = false">Close</v-btn>
        <v-btn color="green" text @click.stop="submit()">Anlegen</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script>
import { api } from "@/plugins/axios";

export default {
  name: "AddDialog",
  data() {
    return {
      groups: undefined,
      menu: false,
      model: {
        groupId: undefined,
        title: undefined,
        description: undefined,
        pos: undefined,
        deadline: null,
      },
    };
  },
  props: {
    value: {
      type: Boolean,
      default: false,
    },
    inputs: {
      type: Object,
    },
  },
  mounted() {
    api.get("todos/group/").then((response) => {
      this.groups = response.data;
    });
  },
  methods: {
    submit() {
      console.log(JSON.stringify(this.model));
      api.post("todos/todo/", JSON.stringify(this.model)).then((response) => {
        this.$emit("update", response.data);
        this.show = false;
      });
    },
  },
  computed: {
    groupNames() {
      var arr = [];
      if (this.groups)
        this.groups.map((group) => {
          arr.push({
            title: group.name,
            value: group.id,
          });
        });

      return arr;
    },
    show: {
      get() {
        return this.value;
      },
      set(value) {
        this.$emit("input", value);
      },
    },
  },
};
</script>
