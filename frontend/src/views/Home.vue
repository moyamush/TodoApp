<template>
  <div class="home">
    <h1>{{ this.$store.state.currentGroupID }}</h1>
  </div>
</template>

<script>
// @ is an alias to /src
import { axios } from "@/common/api.service.js";

export default {
    name: 'Home',
    computed: {
      now() {
        return Date.now()
      }
    },
    methods: {
      date() {
        return Date.now()
      }
    }
}
</script>
