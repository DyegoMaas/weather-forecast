<template>
  <div>
    <div class="page-header">
      <h2>Previsão do tempo para {{ currentCity }}</h2>
    </div>
    <div class="row">
      <div v-for="(button, index) in dayOfWeekButtonsDetails" :key="index" class="col-sm-2 dayButton">
        <p>
          <img src="../assets/021-tornado.png" alt="..." class="weatherIcon">
        </p>
        <p class="text-center">{{ button.dayOfWeek }}</p>
        <p class="text-center">{{ button.minTemperature }}º {{ button.maxTemperature }}º</p>
      </div>
    </div>
  </div>
</template>

<script>

import ForecastDetail from './ForecastDetail';

export default {
  name: 'CityForecast',
  props: ['currentCity', 'forecast'],
  components: {
    'forecastDetail': ForecastDetail
  },
  data() {
    return {
    };
  },
  computed: {
    forecastDetails() {
      const days = ['Dom','Seg','Ter','Qua','Qui','Sex','Sab'];

      const detailsList = this.forecast.map(item => {
        const datetime = new Date(item.dt * 1000);
        return {
          date: datetime.getDate(),
          datetime: datetime,
          dayOfWeek: days[datetime.getDay()],
          temperature: {
            average: item.main.temp,
            min: item.main.temp_min,
            max: item.main.temp_max
          },
        };
      });
      return detailsList;
    },
    dayOfWeekButtonsDetails() {
      const fullDetails = this.forecastDetails;

      const resume = this.$_
        .chain(fullDetails)
        .groupBy(details => details.date)
        .map(dailyDataList => {
          return {
            dayOfWeek: dailyDataList[0].dayOfWeek,
            minTemperature: Math.round(Math.min(...dailyDataList.map(x => x.temperature.min))),
            maxTemperature: Math.round(Math.max(...dailyDataList.map(x => x.temperature.max)))
          };          
        })
      return resume;
    }
  },
}
</script>

<style>
.dayButton {
  background-color: #FEFFD7;
  margin-left: 5px;
  margin-right: 5px;
  width: 100px;
  height: 140px;
  cursor: pointer
}
.weatherIcon {
  max-width: 100%;
  max-height: 100%;
  margin-top: 5px;
}
</style>
