import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '@/router'
Vue.use(Vuex)


// const API_URL = 'http://43.200.88.145:8000'
const API_URL = 'http://127.0.0.1:8000'
// const API_URL = 'http://localhost:8000'

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    user_id: null,
    username: null,
    token: null,
    selectedGenre: null,
    backdropList : [],
    top20MovieList : null,
    userInform: null,
    userSelectedGenre: [],
    movieGenreList: null,
    movieList: null,
    mostLikeMovieList: [],
    score:null,
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    },
  },
  mutations: {
    SAVE_TOKEN(state, payload) {
      state.token = payload.token
      state.username = payload.username
      router.push({name:'MainPageView'})
    },
    DELETE_TOKEN(state) {
      state.token = null
      state.username = null
      router.push('/')
    },
    PUSH_SELECTED_DATA(state, selectedGenre) {
      state.selectedGenre = selectedGenre
    },
    GET_BACKDROP_PATH(state, backdropList){
      state.backdropList = backdropList
    },
    GET_USER_INFO(state, userInform){
      state.userInform = userInform
    },
    SAVE_LIKE_GENRES(state, data){
      state.userSelectedGenre = data
    },
    GET_GENRE_LIST(state, data){
      state.movieGenreList = data
    },
    GET_MOVIE_LIST(state,data){
      state.movieList = data
    },
    SAVE_USER_LIKE(state, data){
      state.mostLikeMovieList = data
    },
    GET_USER_ID(state,data){
      state.user_id = data.id
    },
    GET_TOP20_MOVIES(state,data){
      state.top20MovieList = data
    }
  },
  actions: {
    logIn(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username: payload.username,
          password: payload.password,
        }
      })
        .then((res) => {
          const datas = {token: res.data.key, username: payload.username}
          context.commit('SAVE_TOKEN', datas)
        })

      axios({
        method: 'get',
        url: `${API_URL}/api/v1/getGenreName/${payload.username}/`
      })
      .then((res) => {
        context.commit('SAVE_LIKE_GENRES', res.data)
      })

      axios({
        method: 'get',
        url: `${API_URL}/accounts/getUserId/${payload.username}/`,
        })
          .then(res => {
            context.commit('GET_USER_ID', res.data)
          })
          .catch(err => {
            console.log(err)
          })
    },
    logOut(context) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/logout/`,
      })
        .then(() => {
          context.commit('DELETE_TOKEN')
        })
    },
    pushSelectedGenre(context, selectedGenre){
      context.commit("PUSH_SELECTED_DATA", selectedGenre)
    },
    getBackdropPath(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/backdrop_path/`,
        })
          .then(res => {
            context.commit('GET_BACKDROP_PATH', res.data)
          })
          .catch(err => {
            console.log(err)
          })
    },
    getMovieList(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movielist/`,
        })
          .then(res => {
            context.commit('GET_MOVIE_LIST', res.data)
          })
          .catch(err => {
            console.log(err)
          })
    },
    getTop20MovieList(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/Top20List/`,
        })
          .then(res => {
            context.commit('GET_TOP20_MOVIES', res.data)
          })
          .catch(err => {
            console.log(err)
          })
    },
    getUserInfo(context, username){
        axios({
          method: 'get',
          url: `${API_URL}/accounts/mypage/${username}/`,
          headers: {
            Authorization: `Token ${this.state.token}`
          }
          })
            .then(res => {
              context.commit('GET_USER_INFO', res.data)
            })
            .catch(err => {
              console.log(err)
            })
    },
    getGenre(context){
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/genrelist/`,
        })
          .then(res => {
            context.commit('GET_GENRE_LIST', res.data)
          })
          .catch(err => {
            console.log(err)
          })
    },
    getUserMostLikes(context){
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/recommend/usermostlike/`
      })
      .then((res) => {
        context.commit('SAVE_USER_LIKE', res.data)
      })
    }
  },
  modules: {
  }
})