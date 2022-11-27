<template>
  <div class="comment-wrapper">
    <section class="userInfo"></section>
    <section class="comment-cont">
      <div class="header-wrapper">
        <span class="username">작성자: {{ comment.username }}</span>
            <div class="rating-star">
            <b-form-rating
                class="rating-inline"
                :value="`${comment.rating}`"
                show-value
                show-value-max
                variant="danger"
                precision="1"
                readonly
              >
            </b-form-rating>
          </div>
      </div>
        <div class="delete">

          <button @click="deleteComment" v-if="username === comment.username" class="delete-btn">
            <b-icon icon="trash" scale=1.2></b-icon>
          </button>
        </div>
        <p>{{ comment.content }}</p>
    </section>
    <hr />
  </div>
</template>

<script>
import axios from "axios";
export default {
  props: ["comment", "commentList"],
  methods: {
    deleteComment() {
      const API_URL = "http://43.200.88.145:8000";
      axios({
        method: "delete",
        url: `${API_URL}/api/v1/comment/${this.comment.id}`,
        headers: {
            Authorization: `Token ${this.$store.state.token}`
        },
      }).then(() => {
        if (this.commentList.length === 1) {
          this.$emit("empty");
        } else {
          this.$emit("getComment");
        }
      });
    },
  },
  computed: {
    username() {
      return this.$store.state.username;
    },
  },
};
</script>

<style scoped>
.comment-wrapper {
  text-align: start;
}

.header-wrapper{
  display: grid;
  grid-template-columns: 5fr 1fr;
}
.username {
  font-weight: bolder;
  font-size: 130%;
}
.delete {
  text-align: end;
}

.delete-btn{
  border:none;
  background-color:rgba(255, 255, 255, 0.5);
  
}
</style>
