import streamlit as st
import numpy as np
import pandas as pd
import requests
import datetime
import folium
from streamlit_folium import folium_static
'''
# TaxiFareModel front
'''
date = st.date_input('date',value=datetime.datetime(2022,12,10))
time = st.time_input('time',value=datetime.time(10,23))
date_time = f'{date} {time}'

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

import folium

# Make an empty map
m = folium.Map(location=geocode('New York City'),  zoom_start=7)

folium.Marker(
      location=geocode(pickup_location)
   ).add_to(m)
folium.Marker(
      location=geocode(dropoff_location)
   ).add_to(m)

folium_static(m)

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')


params = {'pickup_datetime':date_time,
          'pickup_longitude':pickup_longitude,
          'pickup_latitude':pickup_longitude,
          'dropoff_longitude':dropoff_longitude,
          'dropoff_latitude':dropoff_latitude,
          'passenger_count':passenger_count
          }
response = requests.get(url, params=params).json().get('fare')

st.write(response)
