<template>
  <div class="about">
    <h1>This is an about page</h1>
    <h1>{{this.$store.state.UserInfo.groups}}</h1>
    <hr>
    <TaskCards />
  </div>
</template>


<script>
import { axios } from "@/common/api.service.js";
import TaskCards from '../components/TaskCards.vue';

export default {
  name: "About",
  components: {
    TaskCards
  },
  data() {
    return {
    }
  },
  created() {
    this.$store.dispatch('')
    this.$store.dispatch('getCurrentGroupTasks')
  },
};
</script>