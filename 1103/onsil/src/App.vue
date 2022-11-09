<template>
  <div id="app">
    <h1>버튼 박스 제작</h1>
    <div id="box">
      <h2>예약 페이지</h2>
      <h3>시간 선택</h3>
      <div>
        <button
        class="btn-off"
        v-for="time in times" :key="`${time}time`" 
        @click="selectTime"
        >
        {{ time }}</button>
      </div>
      <hr class="hr">
      <p id="selected-time">
         선택시간: 
        <span v-for="selectedtime in selectedTimes" :key="selectedtime">{{ selectedtime}}  </span>
         </p>
    </div>
  </div>
</template>

<script>

export default {
  name: 'App',
  data() {
    return{
      times: [ "09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30","14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30","19:00","19:30","20:00","20:30","21:00","21:30","22:00","22:30","23:00","23:30",],
      selectedTimes: [],
    }
  },
  methods: {
    selectTime: function (event) {
      const selectedTime = event.target.innerText
      if (this.selectedTimes.includes(selectedTime)){
        this.selectedTimes.pop(selectedTime)
        event.target.classList.remove('btn-on')
        event.target.classList.add('btn-off')
      } else if (this.selectedTimes.length<5) {
        this.selectedTimes.push(selectedTime)
        event.target.classList.remove('btn-off')
        event.target.classList.add('btn-on')
      } else{
        alert('5타임까지만 신청할 수 있습니다.')
      }
      console.log(event.target.classList)
      console.log(this.selectedTimes)
    }
  }
}
</script>

<style>
#app {
  text-align: center;
  color: #424242;
  font-family: "Noto Sans Korean";
}

#box {
  border: solid black;
  width: 535px;
  margin: auto;
}

#selected-time {
  font-weight: bold;
}

.hr{
  width:80%;
  height: 2px;
  background-color: #0F4C81;
  border: white ;
}

.btn-off {
  margin: 3px;
  border: white ;
  background: white;
  color: #84898C;
}

.btn-on {
  margin: 3px;
  border: white ;
  background: #658dc63d;
  color: #0F4C81;
}

</style>
