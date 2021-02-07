import Vue from "vue";
import App from "./App.vue";
import VueApollo from "vue-apollo";
import defaultClient from "./apolloClient";
import VueCompositionApi from '@vue/composition-api';


Vue.config.productionTip = false;
Vue.use(VueApollo);
Vue.use(VueCompositionApi)


const apolloProvider = new VueApollo({
  defaultClient,
});

new Vue({
  render: (h) => h(App),
  apolloProvider,
}).$mount("#app");
