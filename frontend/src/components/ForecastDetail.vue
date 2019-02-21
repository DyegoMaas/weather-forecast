<template>
  <div>
    <p>{{ temperature.average }}</p>
    <p>{{ temperature.min }}</p>
    <p>{{ temperature.max }}</p>
    <div class="card" style="width: 18rem;">
    <img src="https://ssl.gstatic.com/onebox/weather/64/partly_cloudy.png" class="card-img-top" alt="...">
    <div class="card-body">
      <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
    </div>
  </div>
  </div>
</template>
    
<script>
export default {
  name: 'ForecastDetail',
  props: ['details'],
  data() {
    return {

    };
  },
  computed: {
    temperature() {
      return this.details.temperature;
    }
  },
}
</script>

<style>
</style>
