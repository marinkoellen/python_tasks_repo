import json
import plotly.express as px

from part1 import convert_f_to_c, convert_date

# You are to a Python script that produces the following graphs:
# A single time series graph that contains both the minimum and maximum temperatures for each day.
# A single time series graph that contains the minimum, minimum “real feel”, and minimum “real feel
# shade” temperatures.


forecast_file = "data/forecast_10days.json"

with open(forecast_file) as json_file:
    json_data = json.load(json_file)

# print(json_data)

min_temp_store = []
max_temp_store = []
date_store = []
min_feel_temp_store = []
max_feel_temp_store = []

for day_in_forecast in json_data['DailyForecasts']:
    day_date = day_in_forecast['Date']
    date_store.append(convert_date(day_date))
    min_temp = day_in_forecast['Temperature']['Minimum']["Value"]
    min_temp_c = convert_f_to_c(min_temp)
    min_temp_store.append(min_temp_c)
    max_temp = day_in_forecast['Temperature']['Maximum']["Value"]
    max_temp_c = convert_f_to_c(max_temp)
    max_temp_store.append(max_temp_c)    
    min_temp_feel = day_in_forecast['RealFeelTemperature']['Minimum']["Value"]
    min_temp_feel_c = convert_f_to_c(min_temp_feel)
    min_feel_temp_store.append(min_temp_feel_c)
    max_temp_feel = day_in_forecast['RealFeelTemperature']['Maximum']["Value"]
    max_temp_feel_c = convert_f_to_c(max_temp_feel)
    max_feel_temp_store.append(max_temp_feel_c)

df = {
    "Minimum_Temperature": min_temp_store,
    "Maximum_Temperature": max_temp_store,
    "Real_Feel_Minimum_Temperature": min_feel_temp_store,
    "Real_Feel_Maximum_Temperature": max_feel_temp_store,
    "Date": date_store
}
length_forecast = len(date_store)

fig = px.line(df, y = ["Minimum_Temperature","Maximum_Temperature"], x = "Date")
fig.update_layout(
    title= f"{length_forecast} Day Forecast of Daily Minimum and Maximum Temperature",
    title_x=0.5,
    xaxis_title="Forecast Time Period",
    yaxis_title="Temperature (Degrees Celcius)",
    legend_title="Forecast Type",
    font=dict(
        family="Courier New, monospace",
        size=10,
        color="Navy"
    ),
    hoverlabel=dict(
        bgcolor="white", 
        font_size=9, 
        font_family="Courier New, monospace"
    ),
    hovermode="x"
)
fig.update_traces(mode='markers+lines')
fig.show()



