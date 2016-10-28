# Weather CLI

This is a simple CLI app for retrieving current conditions and a five day forecast from the [OpenWeatherMap API](http://openweathermap.org/)

## Install

- Obtain an API key from [OpenWeatherMap](http://openweathermap.org/)
- Copy you key into `settings.py`
- In `weather.py` change `DEFAULT_CITY` to your city
- `sudo pip install .`

## Usage

### Current Weather

`weather current_weather` returns the temperature in Fahrenheit and current conditions for your default city.

`weather --city="ANOTHER CITY" current_weather` returns the weather for an alternate city.

### Five Day Forecast

TODO: I used a pretty lazy method for setting the five day forecast. I'll eventually come up with a better solution.

`weather five_days` returns the five day forecast for your default city.

`weather --city="ANOTHER CITY" five_days` returns the five day forecast for an alternate city.

