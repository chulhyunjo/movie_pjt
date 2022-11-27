<template>
  <div class="user-list-List">
    <h1>모든 사용자</h1>
    <hr>
    <UsersList/>

  </div>
</template>

<script>
import UsersList from '@/components/UsersList'
export default {
  components: { UsersList},
}

</script>

<style scoped>
.user-list-List{
  margin:50px;
  background-color:rgba(0,0,0,0.3);
  border-radius: 50px;
  padding : 20px;
}
</style>