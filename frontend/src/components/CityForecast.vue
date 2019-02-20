<template>
  <div>
    <div class="page-header">
      <h2>Previsão do tempo para {{ currentCity }}</h2>
    </div>
    <ul>
      <li></li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'CityForecast',
  props: ['currentCity', 'forecast'],
  data() {
    return {
    };
  },
  computed: {
    processedForecasts() {
      const vm = this;
      function Process(){
        const newForecasts = []
        vm.forecast.forEach(hourlyForecast => {
          newForecasts.push({
            x: 1
          });
        });
      }
      return Process();
    }
  },
}
</script>

<style>

</style>
