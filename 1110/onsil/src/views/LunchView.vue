<template>
  <div class="lunch">
    <TheLunch/>
  </div>
</template>

<script>
// @ is an alias to /src
import TheLunch from '@/components/TheLunch'

export default {
  name: 'LunchView',
  components: {
    TheLunch,
  }
}
</script>
