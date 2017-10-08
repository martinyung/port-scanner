<template>
  <div>
    <button class="btn btn-default" :disabled="scanning" @click="portScan">
      <icon v-if="scanning" name="refresh" :spin="scanning"></icon>
      <span>{{ scanning ? 'Scan in progress' : 'Start Scan'}}</span>
    </button>
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
      results: {},
      scanning: false
    }
  },

  methods: {
    portScan () {
      this.results = {}
      this.$Progress.start()
      this.scanning = true

      this.$http.get(process.env.API_BASE_URL + '/scan').then(response => {
        this.results = response.body
        console.log('success')
        this.$Progress.finish()
        this.scanning = false
      }, response => {
        this.$Progress.fail()
        console.log('fail')
        this.scanning = false
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
  height: 50px;
}

ul, ol {
  list-style: none;
  padding-left: 0px;
}
</style>
