<template>
<div class="card-header">
  <header>
    <h1 style="color:white">전체 유저들이 가장 좋아하는 영화</h1>
    <hr>
  </header>
  <section class="card-wrapper">
    <MovieCards
      v-for="movie in movies" :key="movie.id"
      :movie='movie'
      :title='movie.title'
    />
  </section>
</div>
</template>

<script>
import MovieCards from '@/components/MovieCards'

export default {
  components:{MovieCards},
  props: ['movies'],
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