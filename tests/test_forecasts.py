from web_apis.forecasts import ForecastData
import pytest
import json


class TestForecastDataExtraction:

    @pytest.fixture()
    def valid_forecast_data(self):
        with open('valid_forecast.json') as file:
            file_content = file.read()
            return json.loads(file_content)

    @pytest.fixture()
    def invalid_forecast_data(self):
        return json.loads('{"cod":"404","message":"city not found"}')

    def test_forecast_was_found(self, valid_forecast_data):
        forecast = ForecastData(valid_forecast_data)

        assert forecast.found_data() is True

    def test_forecast_was_not_found_for_some_city(self, invalid_forecast_data):
        forecast = ForecastData(invalid_forecast_data)

        assert forecast.found_data() is False

    def test_extracts_nothing_from_an_invalid_response(self, invalid_forecast_data):
        forecast_data = ForecastData(invalid_forecast_data)

        forecast_list = forecast_data.extract()

        assert len(forecast_list) == 0

    def test_extracts_list_from_a_valid_response(self, valid_forecast_data):
        forecast_data = ForecastData(valid_forecast_data)

        forecast_list = forecast_data.extract()

        assert len(forecast_list) == 40
