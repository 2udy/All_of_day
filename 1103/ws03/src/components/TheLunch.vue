<template>
  <div>
    <h1>점심메뉴</h1>
    <button @click="selectMenu">Pick one</button>
    <p>{{ menu }}</p>
    <hr>
  </div>
</template>


<script>
import _ from 'lodash'
export default {
  name: 'TheLunch',
  data() {
    return{
      menus: ['국밥', '짜장면', '햄버거'],
      menu: '',
    }
  },
  methods: {
    selectMenu: function () {
      this.menu = _.sample(this.menus)
      this.$emit('select-menu', this.menu)
    }
  }
}
</script>

<style>

</style>