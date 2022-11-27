<template>
  <div class="err">
    <img src="@/assets/image_404.png" style="margin-bottom:100px">
    <br>
    <router-link :to="{ name: 'MainPageView'}"><b-button variant="outline-primary" style="margin-bottom:150px">처음으로</b-button></router-link>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
.err{
  background-color: white;
  border-radius: 20px;
  margin: 50px;
}
</style>