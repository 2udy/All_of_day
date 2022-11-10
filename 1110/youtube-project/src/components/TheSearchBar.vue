<template>
  <div class="search-bar" :style="{ margin: videoLength ? '0' : '40vh 0'}">
    <input type="text" @keyup.enter="onInputChange">
  </div>
</template>

<script>
export default {
  name: 'TheSearchBar',
  props: {
    videoLength: Number,
  },
  methods: {
    onInputChange() {
      // console.log(event.target.value)
      this.$emit('input-change', event.target.value)
    } 
  },
}
</script>

<style>
.search-bar > input {
  width: 100%;      /* 가로 너비 배치를 화면의 끝과 끝으로 배치 */
  padding: 0.5rem;  /* input 안쪽의 margin을 여유롭게 */
  font-size: 2rem;
}
.search-bar {
  transition-duration: 0.5s;
}
</style>