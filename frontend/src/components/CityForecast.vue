<template>
  <div class="page-header">
    <h2>Previsão do tempo para {{ currentCity }}</h2>
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
}
</script>

<style>

</style>
