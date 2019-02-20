<template>
  <div>
    <span v-if="noCities">Você ainda não consultou nenhuma cidade. Tente! Não dói.</span>
    <div>
      <input type="text" v-model="citySearched" placeholder="Nome da Cidade" />
      <button type="button" v-on:click="getForecastForeCity()" class="btn btn-sm btn-primary search-button">Buscar</button>
    </div>

    <div class="page-header">
      <h2>Histórico de buscas</h2>
    </div>
    <div class="row">
      <div class="col-md-4">
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
      <div class="col-md-8"></div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Cities',
  data() {
    return {
      cities: [],
      citySearched: '',
      forecast: {},
      searchHistory: [],
    };
  },
  computed: {
    noCities() {
      return this.cities.length === 0;
    },
    notFound() {
      return this.searchHistory.filter(search => !search.found)
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
    getForecastForeCity() {
      const vm = this;

      const url = 'http://localhost:8003/api/forecast/' + vm.citySearched;
      axios.post(url)
        .then((res) => {
          vm.forecast = res.data;

          vm.updateSearchHistory()
          vm.refreshCitiesList()
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
          vm.forecast = res.data;
          // TODO show details
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
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
