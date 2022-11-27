import Vue from 'vue'
import VueRouter from 'vue-router'
import SignupView from '@/views/accounts/SignupView'
import ProfileView from '@/views/accounts/ProfileView'
import SelectGenres from '@/views/accounts/SelectGenres'
import QuizView from '@/views/accounts/QuizView'
import MainPageView from '@/views/pages/MainPageView'
import DetailPage from '@/views/pages/DetailPage'
import UserListPage from '@/views/pages/UserListPage'
import UsersFollowList from '@/views/pages/UsersFollowList'
import ErrorPage from '@/views/pages/ErrorPage'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'MainPageView',
    component: MainPageView
  },
  {
    path: '/signup/1',
    name: 'SelectGenres',
    component: SelectGenres,
  },
  {
    path: '/signup/quiz/:count',
    name: 'QuizView',
    component: QuizView,
  
  },
  {
    path: '/signup/2',
    name: 'SignupView',
    component: SignupView
  },
  {
    path: '/main',
    name: 'MainPageView',
    component: MainPageView
  },
  {
    path: '/profile/:username',
    name: 'ProfileView',
    component: ProfileView,
  },
  {
    path: '/movie/detail/:movie_id',
    name: 'DetailPage',
    component: DetailPage
  },
  {
    path: '/users/all',
    name: 'UserListPage',
    component: UserListPage
  },
  {
    path: '/users/:username/follow',
    name: 'UsersFollowList',
    component: UsersFollowList
  },
  {
    path: '/404-error',
    name: 'ErrorPage',
    component: ErrorPage
  },
  {
    path: '*',
    redirect: {name : 'ErrorPage'}
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
