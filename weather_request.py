"""Module for getting forecasts."""

import requests
import json
import sys


class NewForecast(object):
    """A class for creating new forcasts.

    Arguments: city = name of forecast city
    units = "imperial" or "metric"
    default is imperial
    """

    def __init__(self, city, url, app_id, units="imperial"):
        """Initialize forecast."""
        self.city = city
        self.url = url
        self.app_id = app_id
        self.units = units
        self.forecast = self._forecast_request()

    def _forecast_request(self):
        """Make request to API and returns a parsed JSON object."""
        payload = {'q': self.city,
                   "units": self.units,
                   "appid": self.app_id
                   }
        try:
            forecast = requests.get(self.url, params=payload)
            forecast.raise_for_status()
            return json.loads(forecast.text)
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)

    def get_weather(self):
        """Return main forecast block."""
        return self.forecast
