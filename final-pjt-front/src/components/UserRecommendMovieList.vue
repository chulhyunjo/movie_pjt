<template>
<div class="card-header">
  <header>
    <h1 style="color:white;">{{ genre.name }}</h1>
    <hr>
  </header>
  <section class="card-wrapper">
    <MovieCards
    v-for="movie in recommendMovie" :key="movie.id"
        :movie='movie'
        :title='movie.title'
    />
  </section>
</div>
</template>

<script>
import axios from 'axios'
import MovieCards from '@/components/MovieCards'

const BACK_URL = 'http://127.0.0.1:8000'
// const BACK_URL='http://43.200.88.145:8000'
export default {
  data() {
    return {
      recommendMovie : [],
    }
  },
  created(){
    this.getMovieList()
  },
  components: {MovieCards},
  props: ['genre'],
  methods: {
    getMovieList(){
      axios({
        method: 'get',
        url: `${BACK_URL}/api/v1/recommend/${this.genre.id}/`,
        })
          .then(res => {
            this.recommendMovie = res.data
          })
          .catch(err => {
            console.log(err)
          })
    },
  },
}
</script>

<style scoped>
.card-header{
  margin-top:50px;
  background-color: rgb(0,0,0,0.6);
}
.card-wrapper{
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
  flex-direction: row;
}
</style>