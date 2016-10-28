"""This module implements the weather CLI interface."""

import weather_request
from format_forecast import draw_forecast
import click
from settings import APP_ID as APP_ID

WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "http://api.openweathermap.org/data/2.5/forecast"


class Config(object):
    """Creates the pass_config object."""

    def __init__(self):
        """Initialize config object."""
        self.city = ""

pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group()
@click.option('--city', default="Washington, DC",
              help="Set forecast city here.")
@pass_config
def cli(config, city):
    """Main cli function.

    Arguments: config = pass_config object
    city = text, the name of the city of desired forecast
    """
    config.city = city


@cli.command()
@pass_config
def current_weather(config):
    """Display the current weather conditions."""
    weather = weather_request.NewForecast(config.city, WEATHER_URL, APP_ID)
    forecast = weather.get_weather()
    click.echo("Current Conditions for %s" % config.city)
    click.echo("Temp: %s F" % int(round(forecast["main"]["temp"], 0)))
    click.echo("Condition: %s" % forecast["weather"][0]["main"])


@cli.command()
@pass_config
def five_days(config):
    """Display the five day forecast."""
    weather = weather_request.NewForecast(config.city, FORECAST_URL, APP_ID)
    forecast = weather.get_weather()
    click.echo("Five Day Forecase for %s" % config.city)
    table = draw_forecast(forecast)
    click.echo(table.draw())
