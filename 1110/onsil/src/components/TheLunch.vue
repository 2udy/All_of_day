<template>
  <div>
    <h1>점심메뉴</h1>
    <button @click="pickMenu">Pick Lunch</button>
    <p>{{ menu }}</p>
    <br>
    <br>
    <br>
    <h3>로또를 뽑아보자</h3>
    <button @click="pickLotto">Pick Lotto</button>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'TheLunch',
  data() {
    return {
      menus: ['국밥', '짜장면', '피자'],
      menu: null
    }
  },
  methods: {
    pickMenu() {
      this.menu = _.sample(this.menus)
    },
    pickLotto() {
      this.$router.push('lotto')
    }
  },
}
</script>

<style>

</style>