from flask import Flask
from flask_injector import FlaskInjector
from injector import inject, singleton
from repositories.repositories import CitiesRepository, CitiesRepositoryProxy
from web_apis.forecasts import OpenWeatherMapAPI
from repositories.entities import City
import json

app = Flask(__name__, '/api')


@app.route('/')
class Forecast:

    @inject(open_weather_api=OpenWeatherMapAPI, cities_repository=CitiesRepository)
    def __init__(self, open_weather_api, cities_repository):
        self.weather_api = open_weather_api
        self.cities_repository = cities_repository

    @app.route('/')
    def hello(self) -> str:
        return "Let's forecast!"

    @app.route('/cities', methods=['GET'])
    def list_cities(self):
        all_cities = self.cities_repository.get_all()
        stored_cities = [city.name for city in all_cities]
        return json.dump(stored_cities)

    @app.route('/forecast/{city_name}', methods=['POST'])
    def add_city(self, city_name):
        forecast = self.weather_api.get_city_forecast_for_next_5_days(city_name)

        if forecast.data_was_found():
            city = City(city_name)
            self.cities_repository.add(city)

        # TODO transform response
        return forecast


def configure(binder):
    binder.bind(
        CitiesRepository,
        to=CitiesRepositoryProxy(CitiesRepository()),
        scope=singleton
    )

    binder.bind(
        OpenWeatherMapAPI,
        to=OpenWeatherMapAPI(),
        scope=singleton
    )


FlaskInjector(app=app, modules=[configure])


app.run()
