import Vue from 'vue'
import App from './App'
import router from './router'
import VueResource from 'vue-resource'
import VueProgressBar from 'vue-progressbar'
import 'bootstrap/dist/css/bootstrap.min.css'

const options = {
  color: 'rgb(143, 255, 199)',
  failedColor: 'red',
  thickness: '3px'
}

Vue.config.productionTip = false
Vue.use(VueResource)
Vue.use(VueProgressBar, options)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})
