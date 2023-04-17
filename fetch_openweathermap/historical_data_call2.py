import requests, json, datetime, csv
import pandas as pd

# API Key from openweathermap
api_key = '##########################'

# baseURL
base_url = 'https://api.openweathermap.org/data/3.0/onecall/timemachine'

# Read the input data from a CSV file
input_data = pd.read_csv('./input_file.csv')

input_data['date'] = pd.to_datetime(input_data['date'], format='%Y-%m-%d')
input_data['timestamp'] = input_data['date'].apply(lambda x: pd.Timestamp(x).timestamp()).astype(int).astype(str)

# Define a function to call the API and extract the desired weather data
def get_weather_data(latitude, longitude, date):
    # Build the API request URL
    units = 'metric'
    url = f'{base_url}?lat={latitude}&lon={longitude}&dt={date}&units={units}&appid={api_key}'

    # Connect to the API and get the data
    response = requests.get(url)

    # Parse the data and extract the desired weather data
    weather_data = response.json()
    dt = weather_data['data'][0]['dt']
    temp = weather_data['data'][0]['temp']
    humidity = weather_data['data'][0]['humidity']
    pressure = weather_data['data'][0]['pressure']
    clouds = weather_data['data'][0]['clouds']
    wind_speed = weather_data['data'][0]['wind_speed']

    # Convert the UNIX time to a datetime object
    date_time = datetime.datetime.fromtimestamp(dt)

    # Return the weather data as a dictionary
    return {'dt': dt, 'temp': temp, 'humidity': humidity, 'pressure': pressure, 'clouds': clouds, 'wind_speed': wind_speed, 'date_time': date_time}

# Apply the function to each row in the input data and store the resulting weather data in a new DataFrame
weather_df = input_data.apply(lambda row: get_weather_data(row['latitude'], row['longitude'], row['timestamp']), axis=1, result_type='expand')

# Combine the input data with the weather data and store the results in a new CSV file
output_data = pd.concat([input_data, weather_df], axis=1)
output_data.to_csv('output_file.csv', index=False)

