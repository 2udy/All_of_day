<template>
  <div v-if="video" class="video-detail">
    <div class="video-container">
      <iframe :src="videoUrl" frameborder="0"></iframe>
    </div>
    <div class="detail">
      <h2>{{ video.snippet.title }}</h2>
      <p>{{ video.snippet.desctription }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'VideoDetail',
  props: {
    video: Object,
  },
  computed: {
    videoUrl() {
      const videoId = this.video.id.videoId
      const VIDEO_URL = `https://www.youtube.com/embed/${videoId}`
      return VIDEO_URL
    }
  }
}
</script>

<style>
.video-detail {
  width: 70%;           /* Detail, List를 전체 가로 비율 대비 7:3으로 설정 */
  padding-right: 1rem;  /* Detail과 List 사이의 margin */
}

.video-container {
  position: relative;   /* iframe을 container를 기준으로 위치를 지정 */
  padding-top: 56.25%;  /* 유튜브 비디오 비율을 맞추기 위한 높이 설정 */
}

.video-container > iframe {
  position: absolute;   /* container를 기준으로 위치를 지정*/
  top: 0;               /* container의 가장 위쪽으로 위치를 지정 */
  left: 0;
  width: 100%;
  height: 100%;
}

.detail {
  margin-top: 20px;
  padding: 20px;
  border: solid 1px lightgray;
  border-radius: 10px;
}
</style>