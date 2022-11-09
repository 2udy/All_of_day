<template>
  <div id="app">
    <h1>App</h1>
    <input type="text" @input="getAppData">
    <p>parentData: {{ parentData }} </p>
    <p>childData: {{ childData }} </p>
    <AppParent :app-data="appData" @parent-input="parentInput" @child-input="childInput"/>
  </div>
</template>

<script>
import AppParent from './components/AppParent.vue'
export default {
  name: 'App',
  components: {
    AppParent
  },
  data(){
    return{
      appData: '',
      parentData: '',
      childData: '',
    }
  },
  methods: {
    getAppData: function (event) {
      this.appData = event.target.value
    },
    parentInput: function(input){
      this.parentData = input
    },
    childInput: function(input){
      this.childData =input
    }
  }
}
</script>

<style>
#app {
  border: solid black 1px;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
