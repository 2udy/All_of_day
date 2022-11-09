<template>
  <div>
    <input 
    type="text"
    @keyup.enter="createTodo"
    v-model="todoTitle"
    >
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
      if (this.todoTitle) {
        this.$store.dispatch('createTodo', this.todoTitle)
      }
      this.todoTitle =null
    }
  }
}
</script>

<style>

</style>