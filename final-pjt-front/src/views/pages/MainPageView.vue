<template>
  <div class="main-page">
    <section class="top-movies">
    <h1 style="color:white;">Top 20</h1>
      <vueper-slides
        autoplay
        class="no-shadow"
        :visible-slides="6"
        slide-multiple
        :slide-ratio="1 / 4"
        :arrows-outside="false"
        :draggingDistance="1000"
        :touchable="false"
        :slideImageInside="true"
      >
      
        <vueper-slide
          class="image-poster"
          v-for="movie in top20MovieList"
          :key="movie.id"
          :image="`https://themoviedb.org/t/p/w600_and_h900_bestv2${movie.poster_path}`"
          :style="{'margin':'10px'}"
          @click.native="goToDetail(movie.id)"
        />
      </vueper-slides>
    </section>
    <section>
      <FollowingReccomendMovieList/>
    </section>
    <section>
      <GradeMovieList/>
    </section>
    <section>
      <UserRecommendLikeList :movies="mostLikeMovieList" />
    </section>
    <section>
      <div v-for="genre in userSelectedGenre" :key="genre.id">
        <UserRecommendMovieList :genre="genre" />
      </div>
    </section>
  </div>
</template>

<script>
import UserRecommendMovieList from "@/components/UserRecommendMovieList";
import UserRecommendLikeList from "@/components/UserRecommendLikeList";

import { VueperSlides, VueperSlide } from "vueperslides";
import "vueperslides/dist/vueperslides.css";
import GradeMovieList from '@/components/GradeMovieList';
import FollowingReccomendMovieList from '../../components/FollowingReccomendMovieList.vue';

export default {
  computed: {
    top20MovieList() {
      return this.$store.state.top20MovieList;
    },
    userSelectedGenre() {
      return this.$store.state.userSelectedGenre;
    },
    mostLikeMovieList() {
      return this.$store.state.mostLikeMovieList;
    },
  },
  components: {
    UserRecommendMovieList,
    UserRecommendLikeList,
    VueperSlides,
    VueperSlide,
    GradeMovieList,
    FollowingReccomendMovieList,
  },
  created() {
    this.$store.dispatch("getTop20MovieList");
    this.$store.dispatch("getUserMostLikes");
  },
  methods: {
    goToDetail(id) {
      this.$router.push({name:'DetailPage', params:{'movie_id': id} })
    },
  },
};
</script>

<style scoped>
.main-page{
  margin:50px
}
.header-wrapper {
  display: grid;
  justify-content: center;
  grid-template-columns: 1fr;
  margin-top: 30px;
  padding: 0 30%;
  margin-bottom: 10%;
}

.top-movies{
  margin-top: 50px;
  background-color:rgba(0,0,0,0.6)
}

.top-rank-movielist {
  height: 500px;
}

.top-chart {
  text-align: center;
}

.movieCarousel {
  margin: 0 15%;
}

.image-poster {
  width: 100%;
  height: 100%;
}
</style>
