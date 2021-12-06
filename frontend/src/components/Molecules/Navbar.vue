<template>
    <div class="container">
        <nav class="navbar navbar-expand-lg navbar-light bg-light my-navbar">
            <router-link :to="{ name : 'TaskBoard' }" class="navbar-brand">
                TodoApp
            </router-link>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav mr-auto">
            <li class="nav-item active nav-link">
                <router-link :to="{ name : 'TaskBoard' }">
                    TaskBoard
                </router-link>
            </li>
            <li class="nav-item active nav-link">
                <router-link :to="{ name : 'About' }">
                    About
                </router-link>
            </li>
            <li class="nav-item active nav-link">
                <router-link :to="{ name : 'CreateGroup' }">
                    CreateGroup
                </router-link>
            </li>
            <li class="nav-item active nav-link">
                <router-link :to="{ name : 'SearchGroup' }">
                    SearchGroup
                </router-link>
            </li>
            <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                Groups
                </a>
                <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                    <div v-for="(group, index) in this.$store.state.UserInfo.groups" :key="group.id" class="dropdown-item">
                        <div @click="getGroupID(group)">ID: {{ group }},{{ this.$store.state.Group[index].name }} </div>
                    </div>
                </div>
            </li>
            <li class="nav-item">
                <a class="nav-link active" href="/accounts/logout/">Logout</a>
            </li>
            </ul>
            <!-- <form class="form-inline my-2 my-lg-0">
            <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
            <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
            </form> -->
            <button class="btn btn-outline-success ">
                <router-link :to="{ name : 'MyPage' }">
                    ようこそ{{ this.$store.state.UserInfo.username }}
                </router-link>
            </button>
        </div>
        </nav>
    </div>
</template>

<script>
    export default {
        name: "NavbarComponent",
        data() {
            return {
            }
        },
        methods: {
            getGroupID(group_id) {
                this.$store.commit('setCurrentGroupID', group_id)
                this.$store.dispatch('getCurrentGroupTasks')
            }
        },
        created() {
        },
    }
</script>

<style scoped>
.my-navbar {
    border-bottom: 1px solid #DDD;
}
.navbar-brand:hover{
    color : gray;
}
</style>

