<template>
  <div>
    <h1>nmap scanner</h1>
    <button @click="portScan">Scan</button>
    <h4>Scan results:</h4>
    <p v-for="result in results">
      {{ result }}
    </p>
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
      this.$http.get(process.env.API_BASE_URL + '/scan').then(response => {
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
