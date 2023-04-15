<template>
  <div class="quiz-page">
    <h1>Quiz({{page}}/10)</h1>
    <p>현재 점수 : {{ score }}</p>
    <div class="quiz-wrapper" v-if="quizList">
      <div class="quiz-img">
        <img :src="image" alt=""><br>
      </div>
      <div class="btn-wrapper">
        <button 
        v-for="(movie,index) in quizList" :key="index" 
        class="answer-btn"
        @click="checkAnswer(movie.title)"
        >
          {{movie?.title}}
        </button>
      </div>


    </div>
      <button @click="goBack" class="back-btn">처음으로</button>
  </div>
</template>

<script>
import axios from 'axios'
import swal from 'sweetalert'

const API_URL = 'http://127.0.0.1:8000'
// const API_URL='http://43.200.88.145:8000'
export default {
  data(){
    return{
      quizList:null,
      randomNum: Math.floor(Math.random()*3),
      score: 0,
    }
  },
  computed:{
    image(){
      return `https://themoviedb.org/t/p/w600_and_h900_bestv2${this.quizList[this.randomNum]?.backdrop_path}`
    },
    title_answer() {
      return this.quizList[this.randomNum]?.title
    },
    index_answer() {
      const quizList = this.quizList.map((movie)=>{
        if (movie.title === this.title_answer){
          return 'O'
        } else{
          return 'X'
        }
      })
      return quizList.indexOf('O')+1
    },
    page(){
      return this.$route.params.count
    },
    grade(){ 
      if (this.score<=30){
        return '초보'
      }else if (this.score<=70){
        return '중수'
      }else{
        return '고수'
      }
    },
  },
  methods:{
    goBack(){
      this.$router.push('/')
    },
    checkAnswer(title) {
      if (title===this.title_answer){
        this.score = this.score + 10
        swal({
          title: "정답",
          text: `+10점 현재 ${this.score}점입니다.`,
          icon: "success",
          button: "확인",
        });
      }else{
        swal({
          title: "오답",
          text: `정답은 ${this.index_answer}번입니다.`,
          icon: "error",
          button: "확인",
        });
      }

      if (this.page === 10){
        swal({
          title: `당신은 ${this.score}점입니다!`,
          text: "재도전 하시겠습니까?",
          buttons: ["NO", true],
        })
        .then((tryagain) => {
          if (tryagain) {
            swal("재도전!", {
              icon: "success",
            });
            this.score = 0
            this.$router.push({name:"QuizView", params:{count:1}})
          } else {
            swal(`당신은 ${this.grade}!`, {
              icon: "success",
            });
            this.$store.state.score = this.score
            this.$router.push({name:'SignupView'})
          }
        });
      }else{
        this.$router.push({name:'QuizView', params:{count: (this.page*1)+1}})
      }
    }
  },
  created(){
    axios({
        method: 'get',
        url: `${API_URL}/api/v1/quizlist/`,
      })
        .then((res) => {
          this.quizList = res.data
        })
        .catch((err)=>{
          console.log(err)
        })
  },
  beforeRouteUpdate(to,from,next){
    console.log(to)
    this.randomNum=Math.floor(Math.random()*3)
    axios({
        method: 'get',
        url: `${API_URL}/api/v1/quizlist/`,
      })
        .then((res) => {
          this.quizList = res.data
        })
        .catch((err)=>{
          console.log(err)
        })
    next()
  },
  beforeRouteEnter(to, from, next){
      if (to.path === '/signup/quiz/1'){
        next()
      }else{
        next({path:'/signup/quiz/1'})
      }
    }
}
</script>

<style scoped>
.quiz-page p, h1{
  color:white
}
.quiz-wrapper{
  display:flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.quiz-img{
  width:250px;
  height:250px
}

.quiz-img img{
  width: 100%;
  height:100%;
}

.btn-wrapper{
  display:grid;
  grid-template-columns: 1fr 1fr;
}

.back-btn{
  width: 100px;
  padding: 0;
  margin: 10px 20px 10px 0;
  line-height: 50px;
  color: black;
  background: white;
  border-radius: 5px;
  }

.answer-btn{
  font-size: 10px;
  max-width: 250px;
  width: 250px;
  padding: 0;
  margin: 20px 20px 10px 0;
  line-height: 50px;
  color: black;
  background: white;
  border-radius: 5px;
}
</style>