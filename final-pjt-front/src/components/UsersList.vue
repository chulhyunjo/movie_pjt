<template>
  <div class="user-list">
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

const API_URL='http://43.200.88.145:8000'
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
          label: '팔로잉',
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
  created(){
    this.getUserList()
  },
  methods: {
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
      })
    },
    goToProfile(record) {
      this.$router.push({name:"ProfileView", params:{'username': record.username}})
    }
  },
  computed: {
    rows() {
      return this.userList?.length
    },
  }
}
</script>

<style scoped>
.pagination{
  justify-content:center;
}

</style>