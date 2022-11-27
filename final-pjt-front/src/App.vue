<template>
  <div id="app">
    <div class="backgroundImage" :style="{backgroundImage : `url(${url})`}"></div>
    <!-- 로그인전 화면 -->
    <div v-if="!isLogin" class="before-login">
      <header class="logo-wrapper">
        <img src="./assets/logo_transparent.png" alt='pic' class="before-logo-img">
      </header>
      <section class="login-wrapper">
        <LoginForm v-if="this.$route.path==='/'"/>
        <router-view v-if="isSignupPage"/>
      </section>
    </div>

    <!-- 로그인후 화면 -->
    <div v-if="isLogin" class="after-login">
      <nav class="navbar">
        <div class="container-fluid">
          <router-link :to="{ name: 'MainPageView'}"><button class="logo-btn"><img src="./assets/logo.png" alt='pic' class="after-logo-img"></button></router-link>
          <form class="d-flex nav-form" role="search" @submit.prevent>
            <input 
            style="margin-right: 30px"
            class="form-item"
            type="search" 
            placeholder="Search" 
            aria-label="Search" 
            v-model="search_word" 
            :class="visible ? null : 'collapsed'"
            :aria-expanded="visible ? 'true' : 'false'"
            aria-controls="search-collapse"
            @click="visible = true"
            @input="search"
            >
            <router-link :to="{ name:'UserListPage' }">
              <b-icon icon="people" font-scale="2" class="like-icon compo2" ></b-icon>
            </router-link>
            <div>
            <router-link :to="{ name: 'ProfileView' , params: { 'username':username } }">
              <b-icon icon="person-square" font-scale="2" class="like-icon" ></b-icon>
              <b-button class="btn compo2" @click="logOut" style="color:white;" variant="outline-primary">로그아웃</b-button>
            </router-link>
            </div>
      
          </form>
        </div>
      </nav>
            <b-collapse id="search-collapse" v-model="visible">
              <SearchMovieList id="SearchList" :movies="searchMovieList" @closeSearch="closeSearch"/>
            </b-collapse>
      <router-view/>
    </div>
    <footer class="app-footer">
      <span>기획....조현철....유정안</span>
    </footer>
  </div>
</template>

<script>
import axios from 'axios'
import LoginForm from '@/components/LoginForm'
import SearchMovieList from './components/SearchMovieList.vue'

const API_URL='http://43.200.88.145:8000'
export default {
  data(){
    return{
      url: null,
      randomNum: Math.floor(Math.random()*180)+1,
      search_word: null,
      searchMovieList : null,
      visible: false,
    }
  },
  components:{LoginForm,SearchMovieList},
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
    username() {
      return this.$store.state.username
    },
    backdropList() {
      return this.$store.state.backdropList
    },
    isSignupPage() {
      return this.$route.path.includes('signup')
    }
  },
  methods: {
    logOut(){
      this.$store.dispatch('logOut')
    },
    search(){
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/search/${this.search_word}/`,
      })
      .then((res)=>{
        this.searchMovieList = res.data
      })
      .catch((err)=>{
        console.log(err)
      })
    },
    closeSearch(){
      this.visible=false
    }
  },
  created() {
      this.$store.dispatch('getBackdropPath')
      this.visible=false
      if (this.$route.path.includes('/movie/detail/')){
        const backdropList = this.backdropList.filter((movie) =>{
          return movie.id == this.$route.params.movie_id
        })
      if (backdropList.length===0){
        this.url = `https://themoviedb.org/t/p/w600_and_h900_bestv2${this.backdropList[this.randomNum].backdrop_path}`
      } else{
        this.url = `https://themoviedb.org/t/p/w600_and_h900_bestv2${backdropList[0].backdrop_path}`
      }
      }else{
        this.url = `https://themoviedb.org/t/p/w600_and_h900_bestv2${this.backdropList[this.randomNum].backdrop_path}`
      }
  },
  watch:{
    $route(to){
      if (to.name==="DetailPage"){
        this.$store.dispatch('getUserInfo', this.username)
        const backdropList = this.backdropList.filter((movie) =>{
          return movie.id === to.params.movie_id
        })
        this.url = `https://themoviedb.org/t/p/w600_and_h900_bestv2${backdropList[0].backdrop_path}`
      }else if (to.name==="ProfileView"){
        this.$store.dispatch('getUserInfo', to.params.username)
      }
      else{
      const randomNum=Math.floor(Math.random()*180)+1
      this.url = `https://themoviedb.org/t/p/w600_and_h900_bestv2${this.backdropList[randomNum].backdrop_path}`
      }
      this.visible=false
      this.search_word=null
    },
  }
}
</script>

<style>
*{
  font-family: 'Open Sans', sans-serif;
  font-weight: 300;
}

ul{
  list-style: none;
}
html {
  margin: 0;
  min-height: 100%;
}

body {
  min-height: 100vh;
}

#app {
  position: relative;
  overflow: hidden;
  text-align: center;
  min-height: 100vh;
}
.after-logo-img{
  height: 150px;
}

.before-logo-img{
  height: 400px;
}


.backgroundImage{
  opacity: 0.6;
  position: absolute;
  left: 0;
  top: 0;
  bottom:0;
  width: 100%;
  height: 100%;
  background-repeat: round;
  background-size: auto;
  background-position: 50% 0;
  z-index: -1;
}
.backgroundImage::after{
  position: absolute;
  left: 0;
  top: 0;
  opacity: 0.3;
  z-index: 1;
}

.before-login {
  display: grid;
  position: relative;
  margin: 10%;
  grid-template-columns: 1fr 1fr;
  justify-content: center;
  align-items: center;
  background-color: rgb(0,0,0,0.4);
  height: 40em;
}

.login-wrapper {
  margin-left: 50px;
  max-width: 100%;
}

.logo-wrapper {
  margin: 10px;
}

.after-login{
  position: relative;
}

.app-footer{
  margin-top: 100px;
}

.navbar{
  background-color: rgba(0,0,0,0.8);
}
.logo-btn img{
  height: 100px;
}

.container-fluid{
  padding-left: 50px;
  margin-left: 100px;
}

.compo2{
  margin-inline: 30px;
}
</style>

