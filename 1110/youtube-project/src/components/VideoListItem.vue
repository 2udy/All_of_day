<template>
  <div>
    <li @click="selectVideo" class="list-group-item ">
      {{ video.snippet.title|stringUnescape }}
      <br>
      <img :src="thumbnailsUrl" alt="#">
    </li>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'VideoListItem',
  props: {
    video: Object,
  },
  computed: {
    thumbnailsUrl() {
      return this.video.snippet.thumbnails.high.url
    } 
  },
  filters: {
    stringUnescape(rawText) {
      return _.unescape(rawText)
    }
  },
  methods: {
    selectVideo() {
      this.$emit('select-video', this.video)
    }
  }

}
</script>

<style>
.list-group-item {
  display: flex;        /* 가로 배치 및 flex의 CSS 적용 */
  cursor: pointer;      /* 마우스를 포인터로 변경 */
}

.list-group-item:hover {
  background: #eee;
}

.list-group-item img {
  height: fit-content;   /* 텍스트가 길어져도 이미지는 늘어나지 않게 설정 */
  margin-right: 0.5rem;  /* 이미지와 텍스트 사이의 여백 */
}
</style>