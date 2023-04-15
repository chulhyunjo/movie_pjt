<template>
  <div class="user-list">
    <h1>팔로우</h1>
    <b-table
    id="like-movies"
    hover
    :items="userList"
    :per-page="perPage"
    :current-page="currentPage"
    :fields="fields"
    @row-clicked="goToProfile"
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
</template>

<script>
import axios from 'axios'

// const API_URL='http://43.200.88.145:8000'
const API_URL = 'http://127.0.0.1:8000'
export default {
  data(){
    return{
      fields: [
        {
          key : 'username',
          label: '유저이름',
          sortable: false
        },
        {
          key : 'followings.length',
          label: '팔로워',
          sortable: true
        },
        {
          key : 'like_movies.length',
          label: '좋아하는 영화 수',
          sortable: true
        },
        {
          key : 'score',
          label: '점수',
          sortable: true
        }
      ],
      perPage: 10,
      currentPage: 1,
      userList: null,
    }
  },
  computed:{
    userInform(){
      return this.$store.state.userInform
    },
    username(){
      return this.$route.params.username
    },
    rows() {
      return this.userList?.length
    },
  },
  created(){
    this.getUserList()
  },
  methods: {
    goToProfile(record) {
      this.$router.push({name:"ProfileView", params:{'username': record.username}})
    },
    getUserList(){
      axios({
        method: 'get',
        url: `${API_URL}/accounts/getUserList/`,
        headers: {
            Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        this.userList = res.data
        const userList = this.userList?.filter((user)=>{
          return user.username === this.username
        })
        const followUser = userList[0].followings
        this.userList = this.userList?.filter((user)=>{
          return followUser.includes(user.id)
        })
      })
    },
  },
}

</script>

<style scoped>
.pagination{
  justify-content:center;
}


.user-list{

  margin:50px;
  background-color:rgba(0,0,0,0.3);
  border-radius: 50px;
  padding : 20px;

}
</style>