<template>
  <div>
    <v-app-bar color="primary" dark app>
      <v-toolbar-title>ToDo</v-toolbar-title>
      <v-spacer></v-spacer>
    </v-app-bar>
    <template v-for="(group, idx) in structure">
      <draggable
        :list="group.items"
        class="list-group"
        v-bind="dragOptions"
        v-bind:key="idx"
        group="todo"
        @change="handle(group.id)"
      >
        <template v-for="todo in group.items">
          <v-card :key="todo.pos" class="card" max-width="250">
            <v-card-title>{{ todo.desc }}</v-card-title>
            <v-card-subtitle>{{ todo.pos }}</v-card-subtitle>
          </v-card>
        </template>
      </draggable>
    </template>
  </div>
</template>

<script>
import draggable from "vuedraggable";
const structure = [
  {
    name: "DBWT",
    id: 0,
    items: [
      {
        desc: "Praktiktum machen",
        groupId: 0,
        subgroup: "Praktikum",
        due: "Date",
        pos: 0,
        id: 1,
      },
      {
        desc: "E-Test bearbeiten",
        groupId: 0,
        subgroup: "Praktikum",
        due: "Date",
        pos: 1,
        id: 2,
      },
      {
        desc: "Praktikum gehen",
        groupId: 0,
        subgroup: undefined,
        due: "Date",
        pos: 2,
        id: 3,
      },
      {
        desc: "Folie 3 wiederholen",
        groupId: 0,
        subgroup: undefined,
        due: "Date",
        pos: 3,
        id: 4,
      },
    ],
  },
  {
    name: "Arbeit",
    id: 1,
    items: [
      {
        desc: "Account anlegen",
        groupId: 1,
        subgroup: "Wichtig",
        due: "Date",
        pos: 0,
        id: 5,
      },
      {
        desc: "Issue Closen",
        groupId: 1,
        subgroup: "Praktikum",
        due: "Date",
        pos: 1,
        id: 6,
      },
    ],
  },
  {
    name: "OM",
    id: 2,
    items: [
      {
        desc: "Videos schauen",
        groupId: 2,
        subgroup: "Wichtig",
        due: "Date",
        pos: 0,
        id: 7,
      },
      {
        desc: "Lachen",
        groupId: 2,
        subgroup: "Praktikum",
        due: "Date",
        pos: 1,
        id: 8,
      },
    ],
  },
];

export default {
  name: "transition-example-2",
  display: "Transitions",
  components: {
    draggable,
  },
  data() {
    return {
      structure: structure,
      drag: false,
    };
  },
  methods: {
    handle: function (groupId) {
      this.structure
        .filter((group) => group.id === groupId)[0]
        .items.map((todo, idx) => {
          todo.pos = idx;
        });

      //TODO: Send to Backend (update all/group)
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
