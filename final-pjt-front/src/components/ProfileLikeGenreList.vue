<template>
  <div>
    <span v-for="genre in genreList" :key="genre.id">
        <ProfileLikeGenreItem
          :genre='genre'
          v-if='userInform.like_genres.includes(genre.id)'/>
    </span>
  </div>
</template>

<script>
import ProfileLikeGenreItem from '@/components/ProfileLikeGenreItem'
export default {
  components:{ProfileLikeGenreItem},
  props: ['genreList','userInform'],
}
</script>

<style scoped>

</style>