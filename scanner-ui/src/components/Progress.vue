<template>
  <div>
    <h1>Hello</h1>
    <button @click="portScan">Scan</button>
    <p>{{ result }}</p>
  </div>
</template>

<script>
export default {
  name: 'progress',

  data () {
    return {
      result: 'test'
    }
  },

  methods: {
    portScan () {
      this.$http.get('http://localhost:5000/').then(response => {
        this.result = response.body
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
