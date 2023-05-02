<template>
  <div>
    <template v-for="(group, idx) in structure">
      <draggable
        :list="group.items"
        class="list-group"
        v-bind="dragOptions"
        v-bind:key="idx"
        group="todo"
        @change="handle($event, group)"
        @start="drag = true"
        @end="drag = false"
      >
        <template v-for="todo in group.items">
          <v-card :key="todo.pos" class="card" max-width="250">
            <v-card-title>{{ todo.desc }}</v-card-title>
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
        order: 1,
        id: 2,
      },
      {
        desc: "Termin absagem",
        groupId: 0,
        subgroup: undefined,
        due: "Date",
        order: 2,
        id: 3,
      },
      {
        desc: "Folie 3 wiederholen",
        groupId: 0,
        subgroup: undefined,
        due: "Date",
        order: 3,
        id: 4,
      },
    ],
  },
  {
    name: "Arbeit",
    id: 1,
    items: [
      {
        desc: "Anmeldung machen",
        groupId: 1,
        subgroup: "Wichtig",
        due: "Date",
        pos: 0,
        id: 5,
      },
      {
        desc: "Arbeiten",
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
        desc: "Anmeldung machen",
        groupId: 2,
        subgroup: "Wichtig",
        due: "Date",
        order: 0,
        id: 5,
      },
      {
        desc: "Arbeiten",
        groupId: 2,
        subgroup: "Praktikum",
        due: "Date",
        order: 1,
        id: 6,
      },
    ],
  },
];

export default {
  name: "transition-example-2",
  display: "Transitions",
  order: 7,
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
    // test: function (e) {
    //   console.log(e.draggedContext.futureIndex);
    // },
    log: function (evt) {
      window.console.log(evt.added);
      //added , removed , moved
    },

    handle: function (evt, group) {
      if (evt.added !== undefined) {
        evt.added.element.group = "neu";
        evt.added.element.order = evt.added.newIndex;
        console.log(evt.added);
        console.log(group);
      }
      if (evt.moved !== undefined) {
        evt.added.element.order = evt.added.newIndex;
      }
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
