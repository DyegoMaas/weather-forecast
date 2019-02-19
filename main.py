from flask import Flask
from flask_injector import FlaskInjector
from injector import inject, singleton
from repositories.repositories import CitiesRepository
from services.cities_service import CitiesService
from web_apis.forecasts import OpenWeatherMapAPI
from repositories.entities import City
import json


def create_app(config=None, environment=None):
    new_app = Flask(__name__)

    new_app.config.from_object('config_module.DevelopmentConfig')
    new_app.config.update(config or {})

    return new_app


app = create_app()


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

    result = forecast.extract() if forecast.found_data() else []
    return json.dumps(result)


def configure(binder):
    open_weather_api_key = app.config['OPEN_WEATHER_APP_ID']
    binder.bind(
        OpenWeatherMapAPI,
        to=OpenWeatherMapAPI(open_weather_api_key),
        scope=singleton
    )

    binder.bind(
        CitiesRepository,
        to=CitiesRepository,
        scope=singleton
    )

    binder.bind(
        CitiesService,
        to=CitiesService,
        scope=singleton
    )


FlaskInjector(app=app, modules=[configure])


@app.errorhandler(Exception)
def handle_global_error(exception):
    print(exception)
    return "An error has occured. Please try again later."


app.run()
