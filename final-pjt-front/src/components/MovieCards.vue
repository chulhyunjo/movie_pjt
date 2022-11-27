<template>
  <div class="card-div" v-b-hover="hoverHandler">
    <img :src="image" alt="" class="poster " @click="goToDetail">
    <span v-if="movie_title" class="movie-title">{{ title }}</span>
    <b-icon v-if="!likes" icon="suit-heart" variant="danger" @click="like_movie" font-scale="3" class="like-icon"></b-icon>
    <b-icon v-if="likes" icon="suit-heart-fill" variant="danger" @click="like_movie" font-scale="3" class="like-icon"></b-icon>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL='http://43.200.88.145:8000'
export default {
  data(){
    return{
      movie_title : '',
      likes : false,
    }
  },
  props:['movie','title',],
  computed:{
    image() {
      return `https://themoviedb.org/t/p/w600_and_h900_bestv2${this.movie.poster_path}`
    },
    username() {
      return this.$store.state.username
    },
    userInform() {
      return this.$store.state.userInform
    },
  },
  methods: {
    goToDetail() {
      this.$router.push({name:'DetailPage', params:{'movie_id': this.movie.id} })
    },
    hoverHandler(isHovered){
      if(isHovered){
        this.movie_title = this.title
      }else{
        this.movie_title = ''
      }
    },
    like_movie() {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/like/${this.username}/${this.movie.id}/`,
        headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
        })
        .then(() =>{
          this.likes = this.likes ? false : true
        })
    },
  },
  created() {
    this.$store.dispatch('getUserInfo', this.username)
    this.likes = this.userInform.like_movies.includes(this.movie.id)
  },
}
</script>

<style scoped>
.card-div{
  width: 20rem;
  height: 30rem;
  position : relative;
  transform: scale(0.8);
  border:1px solid white;
  border-radius: 15px;
  box-shadow: 0px 10px 15px 0px white;
}

.poster{
  width: 20rem;
  height: 30rem;
  border-radius: 15px;

  transition: all 0.5s;
}
.card-div:hover{
  transition: transform 0.5s linear;
  transform: scale(1);
  
}

.like-icon{
  position: absolute;
  top:0%;
  left:85%;
  transform: translate(-50%,-50%);
  transform: scale(.75);
}

.like-icon:hover{
  transition: transform 0.2s linear;
  transform: skew(0, 0);

}

.movie-title{
  padding: 5px 10px;
  background-color: white;
  text-align: center;
  position: absolute;
  top:50%;
  left:50%;
  width: 70%;
  transform: translate(-50%, -50%);
  border-radius: 5px;
  font-size: 15px;
  font-weight:bold;
}

button{
  border:none;
  background-color: white;
}

</style>