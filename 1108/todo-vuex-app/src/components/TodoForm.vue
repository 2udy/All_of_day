<template>
  <div>
    <input 
    type="text"
    v-model="todoTitle"
    >
    <button @click="createTodo">Add</button>
  </div>
</template>

<script>
export default {
  name: 'TodoForm',
  data() {
    return{
      todoTitle: null
    }
  },
  methods: {
    createTodo() {
      if(this.todoTitle){
        this.$store.dispatch('createTodo', this.todoTitle)
      }
      this.todoTitle = null
    }
  },
}
</script>

<style>

</style>