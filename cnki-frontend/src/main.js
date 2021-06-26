// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import store from './store'
import VCharts from 'v-charts'
Vue.use(VCharts)

Vue.use(ElementUI)
Vue.config.productionTip = false



import Axios from 'axios'
Vue.prototype.$http = Axios
// let getCookie = function (cookie) {
//     let reg = /csrftoken=([\w]+)[;]?/g
//     return reg.exec(cookie)[1]
// }
// Axios.interceptors.request.use(
//   function(config) {
//     // 在post请求前统一添加X-CSRFToken的header信息
//     let cookie = document.cookie;
//     if(cookie && config.method == 'post'){
//       config.headers['X-CSRFToken'] = getCookie(cookie);
//     }
//     return config;
//   },
//   function(error) {
//     // Do something with request error
//     return Promise.reject(error);
//   }
// );





/* eslint-disable no-new */
new Vue({
  el: '#app',
  store,
  router,
  render: h => h(App)
}).$mount("#app")
