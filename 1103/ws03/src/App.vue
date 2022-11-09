<template>
  <div id="app">
    <TheLunch @select-menu="getMenu"/>
    
    <TheLotto v-if="menu != ''" :menu="menu"/>
  </div>
</template>

<script>
import TheLunch from './components/TheLunch.vue'
import TheLotto from './components/TheLotto.vue'

export default {
  name: 'App',
  components: {
    TheLunch,
    TheLotto,
  },
  data() {
    return {
      menu: '',
    }
  },
  methods: {
    getMenu: function(inputData){
      this.menu = inputData
      return this.menu
    }
  },
}
</script>

<style>

</style>
