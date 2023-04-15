<template>
  <div v-if="commentList">
    <div class="detail-card">
      <section class="movie-info">
        <div>
          <span class="movie-title">{{ movieDetail?.title }}</span>
        </div>
        <div class="movie-original-title">
          <span>{{ movieDetail?.original_title }}</span>
          <span style="margin-left:100px">조회수: {{views}} </span>
        </div>
        <hr>
        <p>{{ movieDetail?.overview }}</p>
        <p>장르 : <span v-for="(genre, index) in this.movieDetail?.genres"
        :key="index">{{genre?.name}}  </span></p>
        <p>개봉일자: {{ movieDetail?.release_date }}</p>
        <p>상영시간: {{ movieDetail?.runtime }}분</p>
        <div class="star-like">
          <div class="rating-star">
            <p>관람객 : </p>
            <b-form-rating
              id="rating-inline"
              v-model="value"
              show-value
              show-value-max
              variant="danger"
              precision="1"
              readonly
            >
          </b-form-rating>
          <b-icon v-if="!likes" icon="suit-heart" variant="danger" @click="like_movie" font-scale="2" class="like-icon"></b-icon>
          <b-icon v-if="likes" icon="suit-heart-fill" variant="danger" @click="like_movie" font-scale="2" class="like-icon"></b-icon>
        </div>
        <hr>
        </div>
      </section>
      <section class="image-section ">
        <img :src="image" alt="#"/>
      </section>
    </div>
      <div class="comments">
        <h3>리뷰</h3>
        <p>총 {{commentList?.length}} 개</p>
        <hr>
        <CommentList 
        v-for="comment in commentList "
        :key="comment.id" 
        :comment="comment"
        :commentList="commentList"
        @getComment="getComment"
        @empty="empty"
        />
        <div class="comment">
          <CommentForm @getComment="getComment"/>
        </div>
      </div>
  </div>
</template>

<script>
import axios from "axios";
import CommentForm from "@/components/CommentForm"
import CommentList from "@/components/CommentList"

const API_URL = 'http://127.0.0.1:8000'
// const API_URL='http://43.200.88.145:8000'
export default {
  data() {
    return{
      movieDetail : null,
      commentList : null,
      value: null,
      likes: false,
      views: 0,
    }
  },
  components: {CommentForm, CommentList},
  computed: {
    movieId() {
      return this.$route.params.movie_id
    },
    image() {
      return `https://themoviedb.org/t/p/w600_and_h900_bestv2${this.movieDetail?.poster_path}`
    },
    username() {
      return this.$store.state.username
    },
    userInform() {
      return this.$store.state.userInform
    }
  },
  methods: {
    like_movie() {
      const API_URL='http://127.0.0.1:8000'
      axios({
        method: 'post',
        url: `${API_URL}/accounts/like/${this.username}/${this.movieId}/`,
        headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
        })
        .then(() =>{
          this.likes = this.likes ? false : true
        })
    },
    getCommentList() {
      const API_URL='http://127.0.0.1:8000'
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/commentlist/`,
      })
      .then((res)=>{
        this.commentList = res.data.filter((comment)=>{
          return comment.movie === this.$route.params.movie_id*1
        })
      })
    },
    getComment(){
      this.getCommentList()
    },
    empty(){
      this.commentList = []
    },
    getMovieDetail(){
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/getMovieDetail/${this.movieId}`,
      })
      .then((res) => {
        this.movieDetail = res.data
        this.value = res.data.vote_average/2
      })
      .catch((err)=>{
        console.log(err)
      })
    },
  },
  created() {
    this.getMovieDetail()
    this.getCommentList()
    this.likes = this.userInform.like_movies.includes(this.movieId*1)
  },
  beforeRouteEnter(to,from,next){
    const API_URL='http://127.0.0.1:8000'
    axios({
          method: 'get',
          url: `${API_URL}/api/v1/getMovieDetail/${to.params.movie_id}/`,
      })
      .then((res)=>{
        axios({
              method: 'put',
              url: `${API_URL}/api/v1/getMovieDetail/${to.params.movie_id}/`,
              data:{
                id: res.data.id,
                views: res.data.views+1
              }
            })
        next((movie)=> movie.views=res.data.views+1)
      })
      .catch((err)=>{
        console.log(err)
      })
  },
  beforeRouteUpdate(to,from,next){
    const API_URL='http://127.0.0.1:8000'
    axios({
          method: 'get',
          url: `${API_URL}/api/v1/getMovieDetail/${to.params.movie_id}/`,
      })
      .then((res)=>{
        this.movieDetail = res.data
        this.views = res.data.views+1
        axios({
              method: 'put',
              url: `${API_URL}/api/v1/getMovieDetail/${to.params.movie_id}/`,
              data:{
                id: res.data.id,
                views: res.data.views+1
              }
            })
        next()
      })
      .catch((err)=>{
        console.log(err)
      })
  },
};
</script>

<style scoped>
.detail-card{
  background: rgba(0, 0, 0, 0.5);
  border-radius: 20px;
  padding: 50px;
  margin-top: 50px;
  margin: 10px;
  
}
.comments{
  text-align: start;
  margin: 50px;
  padding: 100px;
  background: rgba(255, 255, 255, 0.9);
  border-radius: 40px;
}
.movie-title{
  color: white;
  font-size: 30px;
  font-weight: bolder;
}

.movie-info p{
  color: white;
}
.movie-original-title{
  color: white;
  margin-left:100px;
}
.image-section {
  display: flex;
  justify-content: center;
  align-items: center;
}
.image-section img {
  height: 400px;
  width: 300px;
}
.detail-card{
  display: grid;
  grid-template-columns: 1fr 1fr;
  margin: 50px;
}

.rating-star{
  display: flex;
  width:50%;
  display: grid;
  grid-template-columns: 1fr 2fr 1fr;
}
.like-icon{
  margin-left: 20px;
}
</style>