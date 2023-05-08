<template>
  <div>
    <v-app-bar color="primary" dark app>
      <v-toolbar-title>ToDo</v-toolbar-title>
      <v-spacer></v-spacer>
    </v-app-bar>
    <v-container class="toolbar">
      <v-icon
        style="
           {
            border: '1px solid white';
          }
        "
        @click.stop="modal = true"
        >mdi-plus</v-icon
      >
    </v-container>
    <AddDialog v-model="modal" @update="updatestruct($event)" />
    <v-container class="todo-container">
      <v-container
        v-for="(group, idx) in structure"
        v-bind:key="idx"
        class="group-container"
      >
        <fieldset v-bind:key="idx">
          <legend>{{ group.name }}</legend>
          <draggable
            :list="group.group_todo"
            class="list-group"
            v-bind="dragOptions"
            v-bind:key="idx"
            group="todo"
            @change="handle(group.id)"
            :style="{ minHeight: '250px' }"
          >
            <template v-for="(todo, idx) in group.group_todo">
              <v-card :key="idx" class="card" :color="calcColor(todo)">
                <v-card-title>{{ todo.title }}</v-card-title>
                <v-card-subtitle>{{ todo.deadline }}</v-card-subtitle>

                <v-card-text>{{ todo.description }}</v-card-text>
              </v-card>
            </template>
          </draggable>
        </fieldset>
      </v-container>
    </v-container>
  </div>
</template>

<script>
import draggable from "vuedraggable";
import AddDialog from "@/components/AddDialog.vue";
import { api } from "@/plugins/axios";
import { calcColor } from "@/utility";

export default {
  name: "App",
  display: "Transitions",
  components: {
    draggable,
    AddDialog,
  },
  data() {
    return {
      structure: undefined,
      drag: false,
      modal: false,
      calcColor: calcColor,
    };
  },
  methods: {
    updatestruct(data) {
      console.log(data);
      this.structure
        .find((group) => group.id === data.groupId)
        .group_todo.push(data);
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
    handleGroupDrag: function (groupId) {
      console.log(groupId);
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
    dragOptionsGroup() {
      return {
        animation: 100,
        group: "group",
        disabled: false,
        ghostClass: "ghost",
      };
    },
    caldColor(item) {
      return calcColor(item);
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
.toolbar {
  display: flex;
  justify-content: flex-end;
}
.todo-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, 350px);
}
.group-container {
  padding: 10px;
}
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
