import requests


class OpenWeatherMapAPI:
    """Simple API built upon https://openweathermap.org/forecast5"""

    def __init__(self, app_id):
        self.app_id = app_id

    def get_city_forecast_for_next_5_days(self, city_name):
        """Currently, it supports only brazilian cities."""

        url = f' http://api.openweathermap.org/data/2.5/forecast?q={city_name},br&mode=json&appid={self.app_id}'
        json = requests.get(url).json()

        return ForecastData(json)


class ForecastData:

    def __init__(self, forecast_data):
        self.data = forecast_data

    def found_data(self) -> bool:
        return self.data["cod"] == '200'

    def extract(self) -> list:
        return self.data["list"] if self.found_data() else []
