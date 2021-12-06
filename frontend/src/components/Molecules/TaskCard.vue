<template>
<div class="card card-skin">
  <div class="card_imgframe">
    <p>タスク名: {{ task.taskname }}</p>
    <p>作成者: {{ task.user }}</p>
    <p>締め切り: {{ task.deadline_at }}</p>
    <button @click="openModal">Edit</button>
    <EditTask v-show="showContent"
              @from-child="closeModal"
              @edit="this.$store.dispatch('getCurrentGroupTasks')"
              :task_id="task.id"
              :prev_taskname="task.taskname" />
    <button @click="deleteTask(task.id)">Delete</button>
  </div>
</div>
</template>

<script>
import Button from '../Atoms/Button.vue'
import EditTask from './EditTask.vue'
export default {
    name: 'TaskCard',
    data() {
        return {
            showContent: false  
        }
    },
    components: {
        Button,
        EditTask
    },
    props:{
        task: {
            type: Object,
            required: true
        }
    },
    methods: {
        openModal: function() {
            this.showContent = true
        },
        closeModal: function() {
            this.showContent = false
        },
        deleteTask(task_id) {
            this.$store.dispatch('getCurrentGroupTasks')
            this.$store.dispatch('deleteTask', {task_id: task_id})
            this.$store.dispatch('getCurrentGroupTasks')
        }
    }
}
</script>

<style>
.card {
  width: 55%;
  margin-bottom: 1em;
}
.card-skin{
  overflow: hidden;
  border-radius: 8px;
  border-left: solid 1px #932993;
  border-right: solid 3px #932993;
  border-bottom: solid 3px #932993;
}

.card_imgframe {
  padding-top: 1rem;
}
</style>