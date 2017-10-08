<template>
  <div class="home">
    <div class="header">
      <h3>{{ pageName }}</h3>
    </div>
    <div class="content-container">
      <scanner/>
    </div>
  </div>
</template>

<script>
import Scanner from '@/components/Scanner'

export default {
  name: 'home',

  data () {
    return {
      pageName: 'NMAP Scanner'
    }
  },

  components: {
    Scanner
  }
}
</script>

<style scoped>
</style>
