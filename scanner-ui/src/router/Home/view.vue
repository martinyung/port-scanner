<template>
  <div class="home row">
    <div class="col-md-8 col-md-offset-2">
      <div class="header">
        <h2>{{ pageName }}</h2>
      </div>
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
