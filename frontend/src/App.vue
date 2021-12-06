<template>
  <div id="app">
    <NavbarComponent />
    <br><br>
    <!-- router-viewでrouter/index.jsに書かれているcomponentを表示できるようにする -->
    <router-view />
  </div>
</template>

<script>
import NavbarComponent from "./components/Molecules/Navbar.vue"
import { axios } from "@/common/api.service.js";

export default {
    name: "App",
    components: {
        NavbarComponent
    }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
