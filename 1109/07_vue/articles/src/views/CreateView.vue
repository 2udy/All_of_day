<template>
  <div>
    <h1>CREATE</h1>
    <form @submit.prevent="createArticle">
      <input type="text" v-model.trim="title">
      <br>
      <textarea v-model.trim="content"></textarea>
      <input type="submit">
    </form>
    <router-link :to="{ name: 'index' }">back</router-link>
  </div>
</template>

<script>
export default {
  name: 'CreateView',
  data() {
    return {
      title: null,
      content: null,
    }
  },
  methods: {
    createArticle() {
      const title = this.title
      const content = this.content
      const payload = {
        title, content
      }
      this.$store.dispatch('createArticle', payload)
      this.$router.push({ name: 'index' })
    }
  }
}
</script>

<style>

</style>