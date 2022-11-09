<template>
  <div id="app-child">
    <h1>AppChild</h1>
    <input type="text" @input="getChildData">
    <p>appData: {{ appData }} </p>
    <p>parentData: {{ parentData }} </p>
    <p>childData: {{ childData }} </p>    
  </div>
</template>

<script>
export default {
  name: 'AppChild',
  data(){
    return{
      childData : '',
    }
  },
  props: {
    parentData: String,
    appData: String,
  },
  methods: {
    getChildData: function (event) {
      this.childData = event.target.value
      this.$emit('child-input', this.childData)
    }
  }
}
</script>

<style>
#app-child{
  border: solid 1px blue;
  margin: 1px;
}

</style>