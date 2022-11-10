import Vue from 'vue'
import VueRouter from 'vue-router'
import LunchView from '@/views/LunchView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'lunchView',
    component: LunchView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
