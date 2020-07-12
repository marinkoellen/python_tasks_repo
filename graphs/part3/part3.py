import json
import plotly.express as px

from part1 import convert_f_to_c, convert_date

# You are to write Python code that produces the following graphs:
# A single graph that contains two box plots, one for the minimum temperatures and one for the max.
# A bar graph showing the number of times each “WeatherText” category occurs.

def set_up_file_for_plot(historical_file):
    min_temp_store = []
    max_temp_store = []
    text_store = []
    dates = []

    with open(historical_file) as json_file:
            json_data = json.load(json_file)

    for index in range(len(json_data)):
        min_temp_c = json_data[index]['TemperatureSummary']['Past24HourRange']['Minimum']['Metric']["Value"]
        min_temp_store.append(min_temp_c)
        max_temp_c = json_data[index]['TemperatureSummary']['Past24HourRange']['Maximum']['Metric']["Value"]
        max_temp_store.append(max_temp_c)
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
            "Minimum_Temperature": min_temp_store,
            "Maximum_Temperature": max_temp_store,
    }

    return df_text_count,df_temp, dates


def function_plot_1(df_temp,dates):
    DatePeriod_max = min(dates)
    DatePeriod_min = max(dates)
    fig = px.box(df_temp, x=["Maximum_Temperature","Minimum_Temperature"])
    fig.update_layout(
            title= f"Distribution of Minimum and Maximum Temperature {DatePeriod_min} and {DatePeriod_max}",
            title_x=0.5,
            xaxis_title="Temperature Type",
            yaxis_title="Degrees (Celcius)",
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

# # fig1 = function_plot_1(df_count2,dates)
# # fig1.show()

# fig2 = function_plot_2(df_text_analysis,dates)
# fig2.show()


file_path = "historical_24hours_a"
file_path = "data/"+file_path+".json"

with open(historical_file) as json_file:
            json_data = json.load(json_file)

    for index in range(len(json_data)):
        min_temp_c = json_data[index]['TemperatureSummary']['Past24HourRange']['Minimum']['Metric']["Value"]
        min_temp_store.append(min_temp_c)

