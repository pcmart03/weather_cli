"""Function for formatting the forecast table."""
from texttable import Texttable
import datetime

DAYS = ["Mon", "Tues", "Wed", "Thur", "Fri", "Sat"]


def draw_forecast(forecast):
    """Format a text table."""
    forecast_list = forecast["list"]
    days = ["Day"]
    weather = ["Weather"]
    lows = ["Low"]
    highs = ["High"]
    date = 0

    for day in forecast_list[::8]:
        date = datetime.date.fromtimestamp(day["dt"])
        days.append(DAYS[date.weekday()])
        weather.append(day["weather"][0]["main"])
        lows.append(round(day["main"]["temp_min"], 0))
        highs.append(round(day["main"]["temp_max"], 0))

    table = Texttable()
    table.set_deco(Texttable.HEADER)
    table.set_cols_align(['c', 'c', 'c', 'c', 'c'])
    # table.add_row(days)
    table.add_rows([days, weather, lows, highs])
    return table
