import Vue from 'vue';
import App from './App.vue';
import defaultClient from './apolloClient';
import VueCompositionApi from '@vue/composition-api';
import { provide } from '@vue/composition-api';
import { DefaultApolloClient } from '@vue/apollo-composable';

Vue.config.productionTip = false;
Vue.use(VueCompositionApi);

new Vue({
  render: (h) => h(App),
  setup() {
    provide(DefaultApolloClient, defaultClient);
  },
}).$mount('#app');
