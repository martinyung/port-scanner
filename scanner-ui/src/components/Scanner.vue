<template>
  <div>
    <button @click="portScan" class="btn btn-default">Start Scan</button>
    <h3>Scan results:</h3>
    <ul>
      <ol v-for="(result, key) in results">
        <h5>Scan Setting: {{ key }} </h5>
        <p>Results: {{ result }} </p>
      </ol>
    </ul>
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
      this.results = {}
      this.$Progress.start()

      this.$http.get(process.env.API_BASE_URL + '/scan').then(response => {
        this.results = response.body
        console.log(this.results)
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
button {
  border-radius: 0px;
  width: 170px;
  height: 40px;
}

ul, ol {
  list-style: none;
  padding-left: 0px;
}
</style>
