import { createRouter, createWebHistory } from 'vue-router'
import TaskBoard from '../components/Templates/TaskBoard.vue'
import About from '../views/About.vue'
import MyPage from '../views/MyPage.vue'
import CreateTask from '../components/Molecules/CreateTask.vue'
import CreateGroup from '../views/CreateGroup.vue'
import SearchGroup from '../components/Templates/SearchGroup.vue'
import EditTask from '../components/Molecules/EditTask.vue'


const routes = [
  {
    // path名 = router-link :to=path名
    path: '/',
    name: 'TaskBoard',
    component: TaskBoard
  },
  {
    path: '/about',
    name: 'About',
    component: About
  },
  {
    path: '/createTask',
    name: 'Task',
    component: CreateTask
  },
  {
    path: '/editTask',
    name: 'EditTask',
    component: EditTask
  },
  {
    path: '/createGroup',
    name: 'CreateGroup',
    component: CreateGroup
  },
  {
    path: '/searchGroup',
    name: 'SearchGroup',
    component: SearchGroup
  },
  {
    path: '/mypage',
    name: 'MyPage',
    component: MyPage
  }
]

const router = createRouter({
  history: createWebHistory(/* process.env.BASE_URL */),
  routes
})

export default router
