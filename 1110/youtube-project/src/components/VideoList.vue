<template>
  <div>
    <h3>VideoList</h3>
    <ul class="list-group">
      <VideoListItem 
        v-for="video in extraVideos" 
        :key="video.id.videoId"
        :video="video"
        @select-video="selectVideo"
      />
    </ul>
  </div>
</template>

<script>
import VideoListItem from '@/components/VideoListItem'

export default {
  name: "VideoList",
  components: {
    VideoListItem,
  },
  props: {
    videos: Array,
  },
  methods: {
    selectVideo(video) {
      this.$emit('select-video', video)
    }
  },
  computed: {
    extraVideos() {
      return this.videos.slice(1)
    }
  }
}
</script>

<style>

</style>