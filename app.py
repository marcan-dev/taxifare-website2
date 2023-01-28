import streamlit as st
import numpy as np
import pandas as pd
import requests
import datetime
'''
# TaxiFareModel front
'''



'''


1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''
date = st.date_input('date',value=datetime.datetime(2022,12,10))
time = st.time_input('time',value=datetime.time(10,23))
date_time = f'{date} {time}'

#pickup_longitude =st.number_input('pickup_longitude',value = 1)
#pickup_latitude =st.number_input('pickup_latitude',value = 1)
#dropoff_longitude =st.number_input('dropoff_longitude',value = 1)
#dropoff_latitude=st.number_input('dropoff_latitude',value = 1)
passenger_count =st.number_input('passenger_count',value = 1)

pickup_location = st.text_input('Your pickup location','Central Park')

dropoff_location = st.text_input('Your dropoff location','Manhattan')
url_map = 'https://nominatim.openstreetmap.org/search'
def geocode(address):
    params = {'q': address,'format':'json'}
    places = requests.get(url_map, params=params).json()
    return places[0]['lat'], places[0]['lon']
pickup_latitude, pickup_longitude = geocode(pickup_location)
dropoff_latitude, dropoff_longitude = geocode(dropoff_location)

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')


'''

2. Let's build a dictionary containing the parameters for our API...
params = {}

3. Let's call our API using the `requests` package...


4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
params = {'pickup_datetime':date_time,
          'pickup_longitude':pickup_longitude,
          'pickup_latitude':pickup_longitude,
          'dropoff_longitude':dropoff_longitude,
          'dropoff_latitude':dropoff_latitude,
          'passenger_count':passenger_count
          }
response = requests.get(url, params=params).json().get('fare')

st.write(response)
