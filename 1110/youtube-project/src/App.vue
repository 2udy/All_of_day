<template>
  <div id="app">
    <h1>나만의 유튜브 프로젝트</h1>
    <header>

    <TheSearchBar 
    @input-change="onInputChange"
    :video-length="videos.length"
    />
    </header>
    <section>
    <VideoDetail :video="selectedVideo"/>
    <VideoList :videos="videos" @select-video="selectVideo"/>
    </section>
      
  </div>
</template>

<script>
import axios from 'axios'
import TheSearchBar from '@/components/TheSearchBar'
import VideoList from '@/components/VideoList'
import VideoDetail from '@/components/VideoDetail'

const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'App',
  components: {
    TheSearchBar,
    VideoList,
    VideoDetail,
  },
  data() {
    return {
      inputData: null,
      videos: [],
      selectedVideo: null,
    }
  },
  methods: {
    selectVideo(video) {
      this.selectedVideo = video
    },
    onInputChange(inputData) {
      this.inputData = inputData
      
      const params = {
        key: API_KEY,
        part: 'snippet',
        type: 'video',
        q: this.inputData,
      }

      axios({
        method: 'get',
        url: API_URL,
        params: params,
      })
        .then((response) => {
          this.videos = response.data.items
          this.selectedVideo = response.data.items[0]
        })
        .catch((error) => {
          console.log(error)
        })
    },

  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

section,
header {
  /* 전체 너비의 80% */
  width: 80%;      
  /* 양 옆 margin을 균등하게 배분 */
  margin: 0 auto;   
  /* 위, 아래 padding */
  padding: 1rem 0;  
}

section {
  /* Detail, List를 가로 배치 */
  display: flex; 
}
</style>
