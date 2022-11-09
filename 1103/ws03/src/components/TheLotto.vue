<template>
  <div>
    <h1>{{ menu }} 먹고 로또</h1>
    <button @click="getNumbers">Get Lucky Numbers</button>
    <p>{{ numbers }}</p>

  </div>
</template>

<script>
import _ from 'lodash'
export default {
  name: 'TheLotto',
  props: {
    menu: String,
  },
  data() {
    return{
      numbers: [],
    }
  },
  methods: {
    getNumbers: function () {
      this.numbers = _.sampleSize(_.range(1, 45), 6)
    }
  }
}
</script>

<style>

</style>