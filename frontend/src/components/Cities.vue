<template>
  <div>
    <span v-if="noCities">Você ainda não consultou nenhuma cidade. Tente! Não dói.</span>
    <ul>
      <li v-for="(city, index) in cities" :key="index">
        Cidade: {{ city }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Cities',
  data() {
    return {
      cities: [],
    };
  },
  computed: {
    noCities() {
      console.log('cities:', this.cites)
      return this.cities.length === 0;
    },
  },
  methods: {
    refreshCitiesList() {
      axios.get('http://localhost:8003/api/cities')
        .then((res) => {
          console.log('resposta:', res, res.data);
          console.log(this);
          this.cities = res.data;
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
</style>
