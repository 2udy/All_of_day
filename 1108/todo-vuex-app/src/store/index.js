import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ], 
  state: {
    todos: []
  },
  getters: {
    allTodosCount(state){
      return state.todos.length
    },
    completedTodosCount(state){
      const completedTodos = state.todos.filter((todo) => {
        return todo.isCompleted === true
      })
      return completedTodos.length
    },
    unCompletedTodosCount(state, getters){
      return getters.allTodosCount - getters.completedTodosCount
    } 
  },
  mutations: {
    DELETE_TODO(state, todoItem) {
      const index = state.todos.indexOf(todoItem)
      state.todos.splice(index, 1)
    },
    CREATE_TODO(state, todoItem){
      state.todos.push(todoItem)
    },
    UPDATE_TODO_STATUS(state, todoItem){
      state.todos = state.todos.map((todo) => {
        if (todo === todoItem){
          todo.isCompleted = !todo.isCompleted
        }
        return todo
      })
    }
  },
  actions: {
    deleteTodo(context, todoItem) {
      context.commit('DELETE_TODO', todoItem)
    },
    createTodo(context, todoTitle){
      const todoItem = {
        title: todoTitle,
        isCompleted: false,
      }
      context.commit('CREATE_TODO', todoItem)
    },
    updateTodoStatus(context, todoItem) {
      context.commit('UPDATE_TODO_STATUS', todoItem)
    }
  },
  modules: {
  }
})
