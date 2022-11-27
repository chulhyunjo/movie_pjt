<template>
  <div class="profile-page" v-if="followers">
    <div class="profile-info">
      <img src="../../assets/profile_default.png" alt="" class="user-img">
      <div class="user-info">
        <h1>{{ username }} 프로필
        <span class="material-symbols-outlined">{{icon}}</span></h1>
        <hr>
        <p>등급: {{grade}}</p>
        <p>팔로워:<span v-if="followers">{{followers.length}}</span></p>
        <router-link :to="{ name:'UsersFollowList', params:{ 'username': userInform?.username } }" style="color:white"><p>팔로우:{{userInform?.followings.length}}</p></router-link>
        <div v-if="!(this.username===this.$store.state.username)">
          <button @click="follow" v-if="!isfollow" class="like-icon"><b-icon icon="person-plus" font-scale="2" ></b-icon></button>
          <button @click="follow" v-if="isfollow" class="like-icon"><b-icon icon="person-plus-fill" font-scale="2"></b-icon></button>
        </div>
      <p>선호 장르</p>
      <hr>
      <span v-for="genre in genreList" :key="genre.id">
          <ProfileLikeGenreItem
            :genre='genre'
            v-if='userInform?.like_genres.includes(genre.id)'/>
      </span>

      </div>
    </div>
    <section class="like-movie-list" v-if="userInform">
      <UserLikeMovieList :userInform="userInform"/>
    </section>
  </div>
</template>

<script>
import ProfileLikeGenreItem from '@/components/ProfileLikeGenreItem'
import UserLikeMovieList from '@/components/UserLikeMovieList'
import axios from 'axios'

const API_URL='http://43.200.88.145:8000'
export default {
  data() {
    return {
      username : this.$route.params.username,
      userInform : null,
      genreList: this.$store.state.movieGenreList,
      followers : null,
    }
  },
  components:{ ProfileLikeGenreItem, UserLikeMovieList },
  computed:{
    now_userId(){
      return this.$store.state.user_id
    },
    isfollow(){
      const follow = this.followers?.filter((user)=>{
      return (this.$store.state.username === user.username)
    })
    if (follow?.length>0){
      const isfollow = true
      return isfollow
    } else{
      const isfollow = false
      return isfollow
    }
    },
    grade(){ 
      if (this.userInform?.score<=30){
        return '초보'
      }else if (this.userInform?.score<=70){
        return '중수'
      }else{
        return '고수'
      }
    },
    icon(){
      if (this.userInform?.score<=30){
        return 'hiking'
      }else if (this.userInform?.score<=70){
        return 'snowshoeing'
      }else{
        return 'self_improvement'
      }
    },
  },
  created() {
    axios({
      method: 'get',
      url: `${API_URL}/accounts/mypage/${this.username}/`,
      headers: {
        Authorization: `Token ${this.$store.state.token}`
      }
      })
        .then(res => {
          this.userInform = res.data
        })
        .catch(err => {
          console.log(err)
        })
    this.$store.dispatch('getGenre')
  },
  methods:{
    follow() {
      const id = this.now_userId
      const username= this.$store.state.username
      axios({
          method: 'POST',
          url: `${API_URL}/accounts/${this.userInform.id}/follow/`,
          data: {
            id,
            username
          },
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
          })
          .then(()=>{
            this.getFollower()
          })
    },
    getFollower(){
      axios({
      method:'get',
      url: `${API_URL}/accounts/getFollowers/${this.username}/`,
    })
      .then((res)=>{
        this.followers = res.data
      })
      .catch((err)=>{
        console.log(err)
      })
    }
  },    
  beforeRouteUpdate(to,from,next){
    this.username = to.params.username
    this.userInform = null
    axios({
          method: 'get',
          url: `${API_URL}/accounts/mypage/${this.username}/`,
          headers: {
            Authorization: `Token ${this.$store.state.token}`
      }
          })
            .then(res => {
              this.userInform = res.data
            })
            .catch(err => {
              console.log(err)
            })
    axios({
      method:'get',
      url: `${API_URL}/accounts/getFollowers/${this.username}/`,
    })
      .then((res)=>{
        this.followers = res.data
      })
      .catch((err)=>{
        console.log(err)
      })
    next()
  },
  beforeRouteEnter(to,from,next){
    axios({
      method:'get',
      url: `${API_URL}/accounts/getFollowers/${to.params.username}/`,
    })
      .then((res)=>{
        next((follower)=> follower.followers=res.data)
      })
      .catch((err)=>{
        console.log(err)
      })
  },
  
}
</script>

<style scoped>
.profile-page{
  margin: 30px;
  padding: 20px;
  font-weight: bold;
  letter-spacing: 1px;
  background: rgba(0, 0, 0, 0.5);
  border-radius: 20px;
}
.profile-info{
  display:grid;
  grid-template-columns: 1fr 2fr;
  color: white;
  margin: 5% 20rem;
  background: rgba(0,0,0,0.3);
  width: 70%;
}

.user-info{
  text-align: start;
  padding: 5%;
  margin: 20px;
}

.user-img{
  height:100%;
  width:100%;
}

.user-genre{
  display: inline;
}

.like-movie-list{
  margin-top: 50px;
  background-color : rgba(0,0,0,0.3);
  color: white;
}
.material-symbols-outlined{
  font-size: 115%;
}

</style>