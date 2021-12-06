<template>
    <div>
        <h1>TaskCard (currentGroupID): {{ this.$store.state.currentGroupID }}</h1>
        <hr>
        <div v-for="task in this.$store.state.GroupTasks" :key="task.id">
            <p>タスク名: <span class="task-color">{{ task.taskname }}</span></p>
            <p>作成者: <span class="task-color">{{ task.user }}</span></p>
            <p>グループ: <span class="task-color">{{ task.group }}</span></p>
            <p>締め切り: <span class="task-color">{{ task.deadline_at }}</span></p>
            <router-link :to="{ name : 'EditTask', 
                                params: { task_id: task.id }
                              }">
                              <button>Edit</button>
            </router-link>
            <button @click="deleteTask(task.id)">Delete</button>
            <hr>
        </div>
    </div>
</template>

<script>
import { axios } from "@/common/api.service.js";

export default {
    name: "TaskCards",
    methods: {
        deleteTask(task_id) {
            this.$store.dispatch('getCurrentGroupTasks')
            this.$store.dispatch('deleteTask', {task_id: task_id})
            this.$store.dispatch('getCurrentGroupTasks')
        },
        editTask(task_id) {
            this.$store.dispatch('editTask', {task_id: task_id, taskname: taskname, deadline_at: deadline_at})
        }
    }
}
</script>

<style>
.task-color {
    color: red;
}

</style>