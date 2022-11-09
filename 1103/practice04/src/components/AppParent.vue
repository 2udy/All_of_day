<template>
  <div id="app-parent">
    <h1>AppParent</h1>
    <input type="text" @input="getParentData">
    <p>appData: {{ appData }} </p>
    <p>childData: {{ childData  }} </p>
    <AppChild :parent-data="parentData" :app-data="appData" @child-input="getChildData"/>
  </div>
</template>

<script>
import AppChild from './AppChild.vue'
export default {
  name: 'AppParent',
  data(){
    return{
      parentData : '',
      childData: '',
    }
  },
  props: {
    appData: String
  },
  components: {
    AppChild,
  },
  methods: {
    getParentData: function (event) {
      this.parentData = event.target.value
      this.$emit('parent-input', this.parentData)
    },
    getChildData: function(input){
      this.childData = input
      this.$emit('child-input',input)
    }
  }
}
</script>

<style>
#app-parent{
  border: solid 1px red;
  margin: 1px;
}

</style>