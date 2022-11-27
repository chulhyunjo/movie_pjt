<template>
  <div class="selectGenreDiv">
    <p>선호하는 장르를 고르세요.({{selectedGenre.length}}/3) </p>
      <div class="genre-items">
          <GenreItems 
            v-for="genre in movieGenreList" :key="genre.id"
            :genre='genre'
            :selectedGenre = 'selectedGenre'
            @selectGenre = "selectGenre"
          />
      </div>
    <footer class="btn-wrapper">
      <button @click="pushSelectedGenre">다음</button>
      <button @click="goBack">처음으로</button>
    </footer>
  </div>
</template>

<script>
import GenreItems from '@/components/GenreItems'

export default {
  data() {
    return {
      selectedGenre : [],
    }
  },
  components: {
    GenreItems,
  },
  computed: {
    movieGenreList() {
      return this.$store.state.movieGenreList
    }
  },
  methods: {
    selectGenre(genreId) {
      if (this.selectedGenre.includes(genreId)){
        this.selectedGenre.splice(this.selectedGenre.indexOf(genreId),1)
      }else{
        if (this.selectedGenre.length>=3){
          alert("3개까지만 선택이 됩니다.")
          return
        }
        this.selectedGenre.push(genreId)
      }
    },
    pushSelectedGenre(){
      if (this.selectedGenre.length<3){
        alert(`${3 - this.selectedGenre.length}개를 더 선택하세요.`)
        return
      }
      this.$store.dispatch('pushSelectedGenre', this.selectedGenre)
      this.$router.push({ name: 'QuizView' , params:{count:1}})
    },
    goBack(){
      this.$router.push('/')
    },
  },
  created() {
    this.$store.dispatch('getGenre')
  },
  
}
</script>

<style scoped>
.selectGenreDiv{
  width: 100%;
}
.selectGenreDiv > p {
  color: white;

}

.genre-items {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr;
}
button{
  width: 120px;
  padding: 0;
  margin: 10px 20px 10px 0;
  line-height: 50px;
  color: black;
  background: white;
  border-radius: 5px;
  }
</style>