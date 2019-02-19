from flask import Flask
from flask_injector import FlaskInjector
from injector import inject, singleton
from repositories.repositories import CitiesRepository
from services.cities_service import CitiesService
from web_apis.forecasts import OpenWeatherMapAPI
from repositories.entities import City
import json


app = Flask(__name__)


@inject
@app.route('/', methods=['GET'])
def hello() -> str:
    return "Let's forecast!"


@inject
@app.route('/cities', methods=['GET'])
def list_cities(cities_repository: CitiesRepository):
    all_cities = cities_repository.get_all()
    stored_cities = [city.name for city in all_cities]
    return json.dumps(stored_cities)


@inject
@app.route('/forecast/<city_name>', methods=['POST'])
def add_city(city_name, city_service: CitiesService):
    city = City(city_name)
    forecast = city_service.get_forecast_for(city)

    if not forecast.found_data():
        return []

    # TODO transform response
    return forecast


def configure(binder):
    binder.bind(
        OpenWeatherMapAPI,
        to=OpenWeatherMapAPI(),
        scope=singleton
    )

    binder.bind(
        CitiesRepository,
        to=CitiesRepository,
        scope=singleton  # TODO request
    )

    binder.bind(
        CitiesService,
        to=CitiesService,
        scope=singleton
    )


FlaskInjector(app=app, modules=[configure])


app.run()
