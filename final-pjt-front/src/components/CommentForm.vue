<template>
  <div class="comment-form">
    <div>
      <b-icon icon="chat-square-text" scale=1.2></b-icon>
      <span class="space">  댓글 작성</span>
    </div>
    <hr>
    <div>
      <b-form-textarea
      id="textarea"
      v-model="content"
      placeholder="Enter something..."
      rows="3"
      max-rows="6"
    ></b-form-textarea>
    </div>
    <div class="rating-star">
          <b-form-rating
            id="rating-inline"
            v-model="value"
            show-value
            show-value-max
            variant="danger"
            precision="0"
          >
          </b-form-rating>
          <div class="submit">
            <button type="submit" @click="putComment" class="btn-submit">제출</button>
          </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import swal from 'sweetalert'

// const API_URL='http://43.200.88.145:8000'
const API_URL = 'http://127.0.0.1:8000'
export default {
  data() {
    return{
      content: null,
      value: null,
    }
  },
  computed: {
    username() {
      return this.$store.state.username
    },
    user_id() {
      return this.$store.state.user_id
    }
  },
  methods: {
    putComment(){
      const content = this.content
      const rating = this.value
      const username = this.username
      if (!content){
        swal({
          title: "댓글을 입력하세요.",
          icon: "error",
          button: "확인",
        });
      }else if(!rating){
        swal({
          title: "평점을 남겨주세요.",
          icon: "error",
          button: "확인",
        });
      }else{
        axios({
          method: 'post',
          url: `${API_URL}/api/v1/${this.$route.params.movie_id}/comments/${this.username}/`,
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          },
          data: {
            content,
            rating,
            username
          }
          })
          .then(() => {
            this.$emit('getComment')
            this.content = null
            this.value = null
          })
      }
    }
  }

}
</script>

<style scoped>

.comment-form{
  display: flex;
  flex-direction: column;
  width: 100%;
  text-align: start;
  background: rgba(255, 255, 255, 0.5);
  margin-top: 150px;
}
.title{
  background: #eee;
  padding: 16px;
  margin: 10px;
  width: 20%;
  border: 0;
  border-radius: 20px;
  box-shadow: inset 7px 2px 10px #babebc, inset -5px -5px 12px #fff;
}
.content{
  background: #eee;
  padding: 16px;
  margin: 10px;
  width: 50%;
  border: 0;
  border-radius: 20px;
  box-shadow: inset 7px 2px 10px #babebc, inset -5px -5px 12px #fff;
}
.btn-submit{
  width: 10%;
}
.space {
  margin: 10px;
  font-size: 120%;
}
.rating-star {
  display: grid;
  grid-template-columns: 1fr 4fr;
  margin-left: 50px;
  padding: 10px;
}
.submit {
  text-align: end;
}
</style>