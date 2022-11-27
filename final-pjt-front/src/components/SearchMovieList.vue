<template>
<div class="card-header">
  <header>
    <h1 style="color:white">검색 기록</h1>
    <hr>
  </header>
  <section class="card-wrapper">
    <SearchMovieItems
      v-for="movie in movies" :key="movie.id"
      :movie='movie'
      :title='movie.title'
      @closeSearch="closeSearch"
    />
  </section>
  <b-button variant="outline-primary" @click="closeSearch">닫기</b-button>
</div>
</template>

<script>
import SearchMovieItems from '@/components/SearchMovieItems'

export default {
  components:{SearchMovieItems},
  props: ['movies'],
  methods:{
    closeSearch(){
      this.$emit('closeSearch')
    }
  }
}
</script>
<style scoped>
.card-header{
  background-color: rgb(0,0,0,0.6);
  max-height: 35rem;
  padding:0 10%;
}
.card-wrapper{
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
  flex-direction: row;
}
</style>