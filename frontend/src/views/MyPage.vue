<template>
  <div class="mypage">
    <h1>{{ this.$store.state.UserInfo }}</h1>
    <hr>
    <h1>{{ this.$store.state.currentGroupID }}</h1>
    <h1>{{ this.$store.state.Group }}</h1>
  </div>
</template>


<script>
import { axios } from "@/common/api.service.js";
// import NavbarComponent from "../components/Navbar.vue"
export default {
    name: 'MyPage'
}
</script>


<style>
.h1 {
    color: red;
}
</style>
