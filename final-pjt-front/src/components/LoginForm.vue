<template>
  <div v-if="!isLogin">
    <form @submit.prevent="logIn">
      <section>
        <input type="text" id="username" placeholder="User" v-model="username"><br>
        <input type="password" id="password" placeholder="Password" v-model="password"><br>
      </section>
      
      <footer class="button-wrapper">
        <button type="submit">로그인</button>
        <button @click="goSignup">회원가입</button>
      </footer>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: null,
      password: null,
    }
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  methods: {
    logIn() {
      const username = this.username
      const password = this.password
      
      const payload = {
        username: username,
        password: password,
      }
      this.$store.dispatch('logIn', payload)
    },
    goSignup(){
      this.$router.push({ name: 'SelectGenres' })
    },
  }
}
</script>

<style scoped>
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

.button-wrapper{
  justify-items: end;
}
</style>