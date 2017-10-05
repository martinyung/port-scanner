<template>
  <div>
    <h1>nmap scanner</h1>
    <button @click="portScan">Scan</button>
    <h4>Scan results:</h4>
    <li v-for="result in results">
      {{ result }}
    </li>
  </div>
</template>

<script>
export default {
  name: 'progress',

  data () {
    return {
      results: []
    }
  },

  methods: {
    portScan () {
      this.$http.get('http://localhost:5000/scan').then(response => {
        this.results = response.body
        console.log(response.body)
      }, response => {
        console.log('fail')
        return response
      })
    }
  }
}
</script>

<style scoped>
</style>
