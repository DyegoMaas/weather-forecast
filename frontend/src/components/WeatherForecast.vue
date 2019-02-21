<template>
  <div>
    <div class="page-header">
      <h1>Previsão do Tempo</h1>
    </div>
    
    <div>
      <input type="text" v-model="citySearched" placeholder="Nome da Cidade" />
      <button type="button" v-on:click="getForecastForCity()" class="btn btn-sm btn-primary search-button">Buscar</button>
      <span v-if="noCities" class="label label-warning" style="margin-right: 10px">Você ainda não consultou nenhuma cidade. Tente! Não dói.</span>
    </div>

    <div class="page-header">
      <h2>Histórico de buscas</h2>
    </div>
    <div class="row">
      <div class=" col-lg-4 col-md-12">
        <table class="table table-striped">
          <tr>
            <th>#</th>
            <th>Cidade</th>
            <th></th>
          </tr>
          <tr v-for="(city, index) in allFound" :key="index">
            <td>
              <span style="margin-right: 10px">{{ index }}</span>
            </td>
            <td>
              <span>{{ city }}</span>
            </td>
            <td>
              <button type="button" v-on:click="getDetails(city)" class="btn btn-sm btn-info details-button">Detalhes</button>
            </td>
          </tr>
          <tr v-for="(city, index) in allNotFound" :key="index+1000">
            <td>-</td>
            <td>
              <span>{{ city }}</span>
            </td>
            <td>
              <span class="label label-danger details-button">Não encontrado</span>
            </td>
          </tr>
        </table>
      </div>
      <div class="col-lg-12 col-md-8"></div>
    </div>
    
    <template v-if="mustShowDetails">
      <city-forecast :current-city="currentCity" :forecast="forecast"></city-forecast>
    </template>
  </div>
</template>

<script>
import CityForecast from './CityForecast';

export default {
  name: 'WeatherForecast',
  components: {
    'city-forecast': CityForecast,
  },
  data() {
    return {
      citySearched: '',
      forecast: [],
      searchHistory: [],
      selectedCity: ''
    };
  },
  computed: {
    currentCity() {
      if (this.selectedCity)
        return this.selectedCity;
      
      const defaultCity = this.allFound.length > 0
        ? this.allFound[0]
        : '';
      return defaultCity;
    },
    noCities() {
      return this.allFound.length === 0;
    },
    allFound() {
      return this.searchHistory
        .filter(search => search.found)
        .map(x => x.name);
    },
    allNotFound() {
      return this.searchHistory
        .filter(search => !search.found)
        .map(x => x.name);
    },
    mustShowDetails() {
      return this.currentCity !== '';
    },
  },
  methods: {
    refreshCitiesList() {
      const vm = this;

      this.$axios.get('/cities')
        .then((res) => {
          const cities = res.data;

          cities.forEach(city => {
            vm.updateSearchHistoryWith(city, true);
          });
        })
        .then(() => {
          vm.getDetails(vm.currentCity);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    getForecastForCity() {
      const vm = this;

      this.$axios.post(`/forecast/${vm.citySearched}`)
        .then((res) => { 
          vm.forecast = res.data;

          const foundAny = vm.forecast.length > 0;
          vm.updateSearchHistoryWith(vm.citySearched, foundAny);
          
          if (foundAny) {
            vm.selectCity(vm.citySearched);
          }
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    getDetails(city) {
      const vm = this;

      vm.selectCity(city);

      this.$axios.post(`/forecast/${city}`)
        .then((res) => {
          vm.forecast = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    updateSearchHistoryWith(city, found) {
       this.searchHistory.push({
          name: city,
          found: found
        });
    },
    selectCity(city) {
       this.selectedCity = city;
    }
  },
  created() {
    this.refreshCitiesList();
  },  
};
</script>

<style>
.search-button {
  margin-left: 10px
}
.details-button {
  margin-bottom: 5px;
  margin-left: 50px;
}
</style>
