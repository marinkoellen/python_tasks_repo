import json
from datetime import datetime


def format_temperature(temp):
    temp = str(temp)
    DEGREE_SYBMOL = u'\N{DEGREE SIGN}'
    
    """Takes a temperature and returns it in string format with the degrees and celcius symbols.
    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and 'degrees celcius.'
    """
    return f"{temp}{DEGREE_SYBMOL}C"

def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.
    
    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year
    """
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime('%H:%M %A %d %B %Y')


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius

    Args:
        temp_in_farenheit: integer representing a temperature.
    Returns:
        An integer representing a temperature in degrees celcius.
    """
    celcius_temp = round(float((temp_in_farenheit) - 32)*(5/9),1)
    return(celcius_temp)


def calculate_mean(total, num_items):
    """Calculates the mean.
    Args:
        total: integer representing the sum of the numbers.
        num_items: integer representing the number of items counted.
    Returns:
        An integer representing the mean of the numbers.
    """
    mean_items = (total)/(num_items)
    mean_items = round(mean_items,1)
    return((mean_items))


def process_weather(forecast_file):
    """Converts raw weather data into meaningful text.
    Args:
        forecast_file: A string representing the file path to a file
            containing raw weather data.
    Returns:
        A string containing the processed and formatted weather data.
    """
    with open(forecast_file) as json_file:
        json_data = json.load(json_file)

    min_temp_store = {}
    max_temp_store = {}
    weather_results = str()
    header_results = str()

    for day_in_forecast in json_data['DailyForecasts']:
        day_date = day_in_forecast['Date']
        min_temp = day_in_forecast['Temperature']['Minimum']["Value"]
        min_temp_c = convert_f_to_c(min_temp)
        min_temp_store[day_date] = min_temp_c
        max_temp = day_in_forecast['Temperature']['Maximum']["Value"]
        max_temp_c = convert_f_to_c(max_temp)
        max_temp_store[day_date] = max_temp_c

        day_time_phrase = day_in_forecast['Day']['LongPhrase']
        rain_chance_day = day_in_forecast['Day']['RainProbability']
        night_time_phrase = day_in_forecast['Night']['LongPhrase']
        rain_chance_night = day_in_forecast['Night']['RainProbability']
        weather_results = weather_results + (f"-------- {convert_date(day_date)} --------\nMinimum Temperature: {format_temperature(round(min_temp_c,1))}\nMaximum Temperature: {format_temperature(round(max_temp_c,1))}\nDaytime: {day_time_phrase}\n    Chance of rain:  {rain_chance_day}%\nNighttime: {night_time_phrase}\n    Chance of rain:  {rain_chance_night}%\n")+ "\n"


    max_day = max(max_temp_store, key=max_temp_store.get)
    max_value = max_temp_store[max_day]
    min_day = min(min_temp_store, key=min_temp_store.get)
    min_value = min_temp_store[min_day]
    max_totals = (sum(max_temp_store.values()))
    min_totals = (sum(min_temp_store.values()))
    num_items = len(min_temp_store)
    mean_min = round(calculate_mean(min_totals,num_items),1)
    mean_max = round(calculate_mean(max_totals,num_items),1)

    save_header =  (f"{len(json_data['DailyForecasts'])} Day Overview\n    The lowest temperature will be {format_temperature(round((min_value),1))}, and will occur on {convert_date(min_day)}.\n    The highest temperature will be {format_temperature(round((max_value),1))}, and will occur on {convert_date(max_day)}.\n    The average low this week is {format_temperature(mean_min)}.\n    The average high this week is {format_temperature(mean_max)}.\n")

    header_results = save_header + "\n"+ weather_results
    
    return(header_results)


if __name__ == "__main__":
    print(process_weather("data/forecast_5days_a.json"))


