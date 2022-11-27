<template>
  <div>
    <h1>회원가입</h1>
    <form @submit.prevent="signUp">
      <div class="signupform">
      <input type="text" id="username" v-model="username" placeholder="Username">
      <button @click.prevent="checkUsername">중복 확인</button><br>
      <input type="password" id="password" v-model="password" placeholder="Password"><br>

      <input type="password" id="password_confirmation" v-model="password_confirmation" placeholder="Password Confirmation">
      </div>
      <p v-if="errorMsg" style="color:red; font-weight: bold;">{{errorMsg}}</p>
      <p class="tmi">※ 비밀번호는 특수문자를 포함해 8자이상으로 만들어 주세요.</p>      <br>
      <br>
      <footer class="button-wrapper">
        <button type="submit">회원가입</button>
        <button @click="goBack">처음으로</button>
      </footer>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
import swal from 'sweetalert'
const API_URL = 'http://43.200.88.145:8000'
export default {
  name: 'SignUpView',
  data() {
    return {
      username: null,
      password: null,
      password_confirmation: null,
      errorMsg : null,
      userList : null,
      isGood : false,
    }
  },
  created(){
    this.getUserList()
  },
  computed:{
    score() {
      return this.$store.state.score
    }
  },
  methods: {
    signUp() {
      if(!this.isGood){
        swal({
          title: "닉네임을 확인하세요.",
          icon: "error",
          button: "확인",
        });
        return
      }
      const username = this.username
      const password = this.password
      const password_confirmation = this.password_confirmation
      const score = this.score
      const like_genres = this.$store.state.selectedGenre
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username,
          password,
          password_confirmation,
          'score':score,
          like_genres,
        }
      })
        .then((res) => {
          if (res.data.fail){
            swal({
              title: `${res.data.fail}`,
              icon: "error",
              button: "확인",
            });
            return false
          }
          else{
            this.$router.push('/')
          }
        })
        .catch((err) => {
          console.log(err)
        })
    },
    goBack(){
      this.$router.push('/')
    },
    getUserList(){
      axios({
        method: 'get',
        url: `${API_URL}/accounts/getUserList/`
      })
      .then((res) => {
        this.userList = res.data
      })
    },
    goToProfile(record) {
      this.$router.push({name:"ProfileView", params:{'username': record.username}})
    },
    checkUsername(){
      if (this.userList){
        const username = this.userList.filter((user)=>{
          return user.username === this.username
          })
        if (username.length>0){
          swal({
            title: "사용중인 닉네임입니다.",
            icon: "error",
            button: "확인",
          });
          this.isGood = false
          }
        else if (this.username.length===0){
          console.log(username.length)
          swal({
            title: "닉네임을 입력하세요.",
            icon: "error",
            button: "확인",
          });
          this.isGood = false
        }
        else{
          swal({
            title: "사용가능한 닉네임입니다",
            icon: "success",
            button: "확인",
          });
          this.isGood = true
        }
      }else{
        swal({
            title: "사용가능한 닉네임입니다",
            icon: "success",
            button: "확인",
          });
          this.isGood = true
      }
    },
  },
  updated(){
    if (this.password_confirmation && !(this.password_confirmation === this.password)){
      this.errorMsg = '비밀번호가 일치하지 않습니다!'
    } else{
      this.errorMsg = null
    }
  }
}
</script>

<style scoped>
h1{
  color: white;
}
input{
  background: #eee;
  padding: 16px;
  margin: 10px;
  width: 50%;
  border: 0;
  border-radius: 20px;
  box-shadow: inset 7px 2px 10px #babebc, inset -5px -5px 12px #fff;
}

button{
  background-color: #00AE68;
  border-radius: 20px;
  font-size: 12px;
  font-weight: bold;
  padding: 15px 25px;
  margin: 10px;
  letter-spacing: 1px;
}
.tmi {
  color: white;
}
.signupform{
  text-align: start;
  margin-left: 100px;
  /* display: grid; */
  /* grid-template-columns: 5fr 1fr; */
}
</style>