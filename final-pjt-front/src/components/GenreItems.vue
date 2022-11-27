<template>
  <div class="btn-wrapper">
    <button @click="selectGenre" :class="{'btn-item btnPush':!isSelected, 'btn-item':isSelected}">{{ genre.name }}</button>
  </div>
</template>

<script>
export default {
  props: ['genre','selectedGenre'],
  computed:{
    isSelected() {
      return this.selectedGenre.includes(this.genre.id)
    }
  },
  methods: {
    selectGenre() {
      return this.$emit('selectGenre', this.genre.id)
    }
  }
}
</script>

<style scoped>
.btn-wrapper{
  margin:10px;
}

.btn-item {
  background: #00AE68;
  display: block;
  position: relative;
  float: left;
  width: 120px;
  padding: 0;
  margin: 10px 20px 10px 0;
  font-weight: 600;
  text-align: center;
  line-height: 50px;
  color: #FFF;
  border-radius: 5px;
  transition: all 0.2s ;
}

.btnPush {
  box-shadow: 0px 5px 0px 0px #007144;
}

.btnPush:hover {
  margin-top: 15px;
  margin-bottom: 5px;
}

.btnPush:hover {
  box-shadow: 0px 0px 0px 0px #007144;
}

</style>