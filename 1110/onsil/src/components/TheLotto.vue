<template>
  <div>
    <h1>로또</h1>
    <button @click="getNumbers">Get Lucky Numbers</button>
    <p>{{ numbers }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'TheLotto',
  data() {
    return{
      numbers: null,
    }
  },
  methods: {
    getNumbers() {
      console.log('click')
      this.numbers = _.sampleSize(_.range(1,46), 6)
      console.log(this.numbers)
    }
  },

}
</script>

<style>

</style>