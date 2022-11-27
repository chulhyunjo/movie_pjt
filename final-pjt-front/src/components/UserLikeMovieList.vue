<template>
  <div>
    <h1>좋아요 목록</h1>
    <hr>
    <div class="overflow-auto">
    <b-table
    id="like-movies"
    :items="user_movieList"
    :per-page="perPage"
    :current-page="currentPage"
    :fields="fields"
    @row-clicked="goToDetail"
    style="color:white;"
    >
    </b-table>

    <b-pagination
    v-model="currentPage"
    :total-rows="rows"
    :per-page="perPage"
    aria-controls="like-movies"
    ></b-pagination>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return{
      fields: [
        {
          key : 'title',
          sortable: false,
        },
        {
          key : 'overview',
          sortable: false
        },
      ],
      perPage: 10,
      currentPage: 1,
      user_movieList:null,
    }
  },
  props:['userInform'],
  computed: {
    movieList() {
      return this.$store.state.movieList
    },
    rows() {
      return this.user_movieList?.length
    }
  },
  created() {
    this.$store.dispatch('getMovieList')
    const movieList = this.movieList.filter((movie)=>{
        return this.userInform?.like_movies.includes(movie.id)
      })
    movieList.map((movie)=>{
      movie.overview = movie.overview.slice(0,50) + '...'
      if (movie?.title.length>10){
        movie.title = movie.title.slice(0,10) + '...'
      }

    })
    this.user_movieList = movieList
  },
  methods: {
    goToDetail(record) {
      this.$router.push({name:'DetailPage', params:{'movie_id': record.id} })
    },
  }
}
</script>

<style scoped>
.pagination{
  justify-content:center;
}
</style>