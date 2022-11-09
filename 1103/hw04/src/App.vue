<template>
  <div id="app">
    <hello-world @click="onClick"></hello-world>
    <hello-world @click.native="onClick"></hello-world>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    HelloWorld
  },
  methods: {
    onClick: function () {
      console.log('Hello!')
    }
  }
}
</script>

<style>

</style>
