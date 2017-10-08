<template>
  <div>
    <button @click="portScan">Scan</button>
    <h4>Scan results:</h4>
    <p v-for="(result, key) in results">
      Scan Setting: {{ key }} 
      <br>
      Scan Result: {{ result }}
    </p>
  </div>
</template>

<script>
export default {
  name: 'scanner',

  data () {
    return {
      results: {}
    }
  },

  methods: {
    portScan () {
      this.$Progress.start()

      this.$http.get(process.env.API_BASE_URL + '/scan').then(response => {
        this.results = response.body
        console.log(response.body)
        this.$Progress.finish()
      }, response => {
        this.$Progress.fail()
        console.log('fail')
        return response
      })
    }
  }
}
</script>

<style scoped>
</style>
