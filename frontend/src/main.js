import Vue from 'vue'
import App from './App.vue'

import service from './utils/request'

Vue.prototype.$service = service;
Vue.config.productionTip = false

new Vue({
    render: h => h(App),
}).$mount('#app')
