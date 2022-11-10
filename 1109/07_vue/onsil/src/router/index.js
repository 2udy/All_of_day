import Vue from 'vue'
import VueRouter from 'vue-router'
import First from '../views/First.vue'
import SecondView from '../views/SecondView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/first',
    name: 'first',
    component:First
  },
  {
    path: '/second',
    name: 'second',
    component:SecondView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
