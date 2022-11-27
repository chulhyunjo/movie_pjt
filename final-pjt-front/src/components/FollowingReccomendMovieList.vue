<template>
  <div class="follow-movie-list"  v-if="followMovieList?.length>0">
    <h1 style="color:white;">{{username}}님이 팔로우하는 유저 추천 목록</h1>
    <section class="card-wrapper">
      <MovieCards
      v-for="movie in followMovieList" :key="movie.id"
          :movie='movie'
          :title='movie.title'
      />
    </section>
  </div>
</template>

<script>
import axios from 'axios'
import MovieCards from '@/components/MovieCards'

const BACK_URL='http://43.200.88.145:8000'
export default {
  components: { MovieCards },
  data(){
    return{
      followMovieList: null,
    }
  },
  computed:{
    username(){
      return this.$store.state.username
    }
  },
  methods: {
    getFollowMovieList(){
      axios({
        method: 'get',
        url: `${BACK_URL}/api/v1/recommend/follow/${this.username}/`,
        headers: {
            Authorization: `Token ${this.$store.state.token}`
        },
        })
          .then(res => {
            this.followMovieList = res.data
          })
          .catch(err => {
            console.log(err)
          })
    },
  },
  created(){
    this.getFollowMovieList()
  },
}
</script>

<style scoped>
.follow-movie-list{
  margin-top:50px;
  background-color: rgba(0,0,0,0.6);
}
.card-wrapper{
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
  flex-direction: row;
}
</style>