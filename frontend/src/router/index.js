import { HTTP } from '@/common/http-common';
import _ from 'lodash';
import Vue from 'vue';
import Router from 'vue-router';
import WeatherForecast from '@/components/WeatherForecast';

Vue.prototype.$axios = HTTP;
Object.defineProperty(Vue.prototype, '$_', { value: _ });
Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'WeatherForecast',
      component: WeatherForecast,
    },
  ],
});
