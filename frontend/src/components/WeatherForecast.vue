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
            <tr v-for="(city, index) in cities" :key="index">
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
            <tr v-for="(city, index) in notFound" :key="index">
              <td>-</td>
              <td>
                <span>{{ city.name }}</span>
              </td>
              <td>
                <span class="label label-danger details-button">Não encontrado</span>
              </td>
            </tr>
          </table>
        </div>
        <div class="col-lg-12 col-md-8"></div>
      </div>
      <div class="col-lg-8 col-md-12">
        <template v-if="mustShowDetails">
          <div class="page-header">
            <h2>Previsão do tempo para {{ currentCity }}</h2>
          </div>
        </template>
      </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'WeatherForecast',
  data() {
    return {
      cities: [],
      citySearched: '',
      currentCity: '',
      forecast: {},
      searchHistory: [],
    };
  },
  computed: {
    noCities() {
      return this.cities.length === 0;
    },
    notFound() {
      return this.searchHistory.filter(search => !search.found);
    },
    mustShowDetails() {
      return this.currentCity !== '';
    },
  },
  methods: {
    refreshCitiesList() {
      const vm = this;
      axios.get('http://localhost:8003/api/cities')
        .then((res) => {
          vm.cities = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    getForecastForCity() {
      const vm = this;

      const url = 'http://localhost:8003/api/forecast/' + vm.citySearched;
      axios.post(url)
        .then((res) => {
          vm.forecast = res.data;

          vm.updateSearchHistory();
          vm.refreshCitiesList();
          vm.showDetails(vm.citySearched);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    updateSearchHistory() {
      this.searchHistory.push({
        name: this.citySearched,
        found: this.forecast.length > 0
      });
    },
    getDetails(city) {
      const vm = this;

      const url = 'http://localhost:8003/api/forecast/' + city;
      axios.post(url)
        .then((res) => {
          vm.currentCity = city;
          vm.forecast = res.data;
          vm.showDetails(city);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    showDetails(city) {
      this.currentCity = this.forecast.length > 0 ? city : '';
    },
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
