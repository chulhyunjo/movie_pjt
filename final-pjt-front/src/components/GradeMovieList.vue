<template>
  <div class="grade-movie-list" v-if="gradeMovieList?.length>0">
    <h1 style="color:white;">등급별 추천 영화</h1>
    <section class="card-wrapper">
      <MovieCards
      v-for="movie in gradeMovieList" :key="movie.id"
          :movie='movie'
          :title='movie.title'
      />
    </section>
  </div>

</template>

<script>
import axios from 'axios'
import MovieCards from '@/components/MovieCards'

// const BACK_URL='http://43.200.88.145:8000'
const BACK_URL = 'http://127.0.0.1:8000'
export default {
  components: { MovieCards },
  data(){
    return{
      gradeMovieList:null,
    }
  },
  computed:{
    username(){
      return this.$store.state.username
      } 
  },
  methods: {
    getGradeMovieList(){
      axios({
        method: 'get',
        url: `${BACK_URL}/api/v1/recommend/grade/${this.username}/`,
        headers: {
            Authorization: `Token ${this.$store.state.token}`
        },
        })
          .then(res => {
            this.gradeMovieList = res.data
          })
          .catch(err => {
            console.log(err)
          })
    },
  },
  created(){
    this.getGradeMovieList()
  }
}
</script>

<style scoped>
.grade-movie-list{
  margin-top:50px;
  background-color: rgba(0,0,0,0.6);
}
.card-wrapper{
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
  flex-direction: row;
}
</style>