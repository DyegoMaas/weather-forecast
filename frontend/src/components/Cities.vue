<template>
  <div>
    <span v-if="noCities">Você ainda não consultou nenhuma cidade. Tente! Não dói.</span>
    <div>
      <input type="text" v-model="citySearched" /> <a v-on:click="getForecastForeCity()"> Search </a>
    </div>
    <ul>
      <li v-for="(city, index) in cities" :key="index">
        {{ city }}
      </li>
    </ul>

    <br/>

    <h2>Histórico de buscas:</h2>
    <ol>
      <li v-for="(city, index) in searchHistory" :key="index">
        {{ city.name }} - {{ city.found ? "Encontrada" : "Não encontrada" }}
      </li>
    </ol>
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
        found: this.forecast.length
      });
    },
  },
  created() {
    this.refreshCitiesList();
  },
};
</script>

<style>
</style>
