import json
import plotly.express as px

from part1 import convert_f_to_c, convert_date

# You are to a Python script that produces the following graphs:
# A single time series graph that contains both the minimum and maximum temperatures for each day.
# A single time series graph that contains the minimum, minimum “real feel”, and minimum “real feel
# shade” temperatures.
# forecast_file = "data/forecast_10days.json"


def set_up_file_for_plot(forecast_file):
    with open(forecast_file) as json_file:
        json_data = json.load(json_file)

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
    return df


def plot_function_1(df):
    length_forecast = len(df)
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
    return fig


def plot_function_2(df):
    length_forecast = len(df)
    fig = px.line(df, y = ["Minimum_Temperature","Real_Feel_Minimum_Temperature","Maximum_Temperature","Real_Feel_Maximum_Temperature"], x = "Date")
    fig.update_layout(
        title= f"{length_forecast} Day Forecast of Daily Minimum and Maximum Temperature + Real Feel Temperature",
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
    return fig

file_path = str(input("Please enter file name, (data must be in data sub folder)"))
file_path = "data/"+file_path
dataframe_input = set_up_file_for_plot(file_path)
# fig_1 = plot_function_1(dataframe_input)
fig_2 = plot_function_2(dataframe_input)

# fig_1.show()
fig_2.show()



