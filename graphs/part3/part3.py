import json
import plotly.express as px

from part1 import convert_f_to_c, convert_date, format_temperature

# You are to write Python code that produces the following graphs:
# A single graph that contains two box plots, one for the minimum temperatures and one for the max.
# A bar graph showing the number of times each “WeatherText” category occurs.

def set_up_file_for_plot(historical_file):
    temp_c_store = []
    temp_feel_c_store = []
    text_store = []
    dates = []

    with open(historical_file) as json_file:
            json_data = json.load(json_file)

    for index in range(len(json_data)):
        temp_c = json_data[index]['Temperature']['Metric']["Value"]
        temp_c_store.append(temp_c)
        temp_feel_c = json_data[index]['RealFeelTemperature']['Metric']["Value"]
        temp_feel_c_store.append(temp_feel_c)
        descript_text = json_data[index]['WeatherText']    
        text_store.append(descript_text)
        date_current = json_data[index]['LocalObservationDateTime']
        date_current = convert_date(date_current)
        dates.append(date_current)

    phrases_unique = list(set(text_store)) 
    phrases_count = []
    for name in phrases_unique:
        count_val = text_store.count(name)
        phrases_count.append(count_val)

    df_text_count = {
        "Weather_Description": phrases_unique,
        "Count": phrases_count
    }

    df_temp = {
            "Temperature_RealFeel": temp_feel_c_store,
            "Temperature": temp_c_store,
    }

    return df_text_count,df_temp, dates


def function_plot_1(df_temp,dates):
    DatePeriod_max = min(dates)
    DatePeriod_min = max(dates)
    fig = px.box(df_temp, x=["Temperature_RealFeel","Temperature"])
    fig.update_layout(
            title= f"Distribution of RealFeel Temperature and Temperature {DatePeriod_min} and {DatePeriod_max}",
            title_x=0.5,
            yaxis_title="Temperature Type",
            xaxis_title="Degrees (Celcius)",
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
    return fig

def function_plot_2(df_text_count,dates):
    fig = px.bar(
        df_text_count,
        x="Count",
        y="Weather_Description",
        color = 'Count'
    )

    DatePeriod_max = min(dates)
    DatePeriod_min = max(dates)

    fig.update_layout(
            title= f"Count of Unique Weather phrases between {DatePeriod_min} and {DatePeriod_max}",
            title_x=0.5,
            xaxis_title="Count",
            yaxis_title="Weather Description",
            legend_title="Count",
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
    return fig

# file_path = str(input("Please enter file name, (data must be in data sub folder)"))
# file_path = "data/"+file_path+".json"
# df_text_analysis, df_count2,dates = set_up_file_for_plot(file_path)

# fig1 = function_plot_1(df_count2,dates)
# fig1.show()

# fig2 = function_plot_2(df_text_analysis,dates)
# fig2.show()


def weather_hourly_summary(file_path_input):
    file_path = "data/"+file_path_input+".json"
    temp_store = {}
    uv_store = {}
    total_rain = 0
    day_time_hours = 0 
    rain_hours = 0
    times =[]
    with open(file_path) as json_file:
            json_data = json.load(json_file)
            for index in range(len(json_data)):
                time_of_entry = json_data[index]['LocalObservationDateTime']
                times.append(time_of_entry) 
                temp_c = json_data[index]['Temperature']['Metric']["Value"]
                temp_store[time_of_entry] = temp_c

                uv = json_data[index]['UVIndex']
                uv_store[time_of_entry] = uv
                total_rain = total_rain + float(json_data[index]['PrecipitationSummary']['PastHour']["Metric"]['Value'])
                
                is_day_time = json_data[index]['IsDayTime']
                if is_day_time:
                    day_time_hours = day_time_hours + 1
                
                has_rain = json_data[index]['HasPrecipitation']

                if has_rain:
                    rain_hours = rain_hours + 1


    #times for summary
    min_time = min(times)
    max_time = max(times)

    print(convert_date(min_time))
    #' Calculate max temp and when it occured
    max_temp_key = max(temp_store, key=temp_store.get)
    max_temp_date = convert_date(max_temp_key)

    #' Calculate min temp and when it occured
    min_temp_key = min(temp_store, key=temp_store.get)
    min_temp_date = convert_date(min_temp_key)

    #' Calculate max UV
    uv_max = max(uv_store.values())
    uv_max_all = [k for k, v in uv_store.items() if v == uv_max]
    [convert_date(item) for item in uv_max_all]
    uv_max_all = list(map(convert_date, uv_max_all))
    uv_max_temp_date1 = ', '.join(uv_max_all[:-1]) + ' & ' + uv_max_all[-1]

    name_file = str(file_path_input + "_output.txt")
    with open(name_file, "w",encoding='utf8') as txt_file:
        txt_file.write(f"Weather summary of hourly data recorded between {convert_date(min_time)} and {convert_date(max_time)}:\n\nThe minimum temperature of {format_temperature(temp_store[min_temp_key])} occured on {min_temp_date}.\nThe maximum temperature of {format_temperature(temp_store[max_temp_key])} occured on {max_temp_date}.\nThe total number of hours that precipitation fell in the last {len(json_data)} hours was {rain_hours}.\nThe total number of daylight hours in the past {len(json_data)} hours was {day_time_hours}.\nThe maximum UV index was {uv_max} and this occured at {uv_max_temp_date1}.\n")



file_path = str(input("Please enter file name, (data must be in data sub folder)"))
weather_hourly_summary(file_path)

