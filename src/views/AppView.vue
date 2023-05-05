<template>
  <div>
    <v-app-bar color="primary" dark app>
      <v-toolbar-title>ToDo</v-toolbar-title>
      <v-spacer></v-spacer>
    </v-app-bar>
    <template v-for="(group, idx) in structure">
      <draggable
        :list="group.group_todo"
        class="list-group"
        v-bind="dragOptions"
        v-bind:key="idx"
        group="todo"
        @change="handle(group.id)"
      >
        <template v-for="todo in group.group_todo">
          <v-card :key="todo.pos" class="card" max-width="250">
            <v-card-title>{{ todo.description }}</v-card-title>
            <v-card-subtitle>{{ todo.pos }}</v-card-subtitle>
          </v-card>
        </template>
      </draggable>
    </template>
    <v-btn @click="goggl()">KLICK MI</v-btn>
  </div>
</template>

<script>
import draggable from "vuedraggable";

import { api } from "@/plugins/axios";

export default {
  name: "transition-example-2",
  display: "Transitions",
  components: {
    draggable,
  },
  data() {
    return {
      structure: undefined,
      drag: false,
    };
  },
  methods: {
    goggl() {
      console.log(this.structure);
    },
    handle: function (groupId) {
      this.structure
        .filter((group) => group.id === groupId)[0]
        .group_todo.map((todo, idx) => {
          todo.pos = idx;
          todo.groupId = groupId;
        });

      //TODO: Send all todos Backend (update all/group)
      // console.log(this.structure);
      var todos = [];
      this.structure.map((group) => {
        group.group_todo.map((todo) => {
          todos.push(todo);
        });
      });
      api.put("todos/todo/", todos);
    },
  },
  computed: {
    dragOptions() {
      return {
        animation: 100,
        group: "description",
        disabled: false,
        ghostClass: "ghost",
      };
    },
  },
  mounted() {
    api.get("todos/struct/").then((response) => {
      this.structure = response.data;
    });
  },
};
</script>

<style>
.button {
  margin-top: 35px;
}
.card {
  margin-top: 5px;
}
.flip-list-move {
  transition: transform 0.1s;
}
.no-move {
  transition: transform 0s;
}
.list-group {
  min-height: 20px;
  margin-bottom: 50px;
}
.list-group-item {
  cursor: move;
}
.list-group-item i {
  cursor: pointer;
}
</style>
