<template>
  <span>
    {{ genre.name }}
  </span>
</template>

<script>
export default {
  props:['genre']
}
</script>

<style scoped>
span{
  background-color: #00AE68;
  border-radius: 20px;
  font-size: 12px;
  font-weight: bold;
  padding: 15px 25px;
  margin: 10px;
  letter-spacing: 1px;
}

</style>