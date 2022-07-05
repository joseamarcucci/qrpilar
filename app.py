
import streamlit as st
st.set_page_config(
page_title="QR para Registro Docentes",
page_icon="https://webinars.usal.edu.ar/sites/default/files/favicon.ico",
layout="wide",
initial_sidebar_state="expanded",)
import argparse 
import httplib2
import smtplib
import ssl
import altair as alt
from altair import *
import streamlit.components.v1 as components
import requests
import re
from bs4 import BeautifulSoup
import urllib.request
import urllib.request as url
import gspread
import pandas as pd
from mailjet_rest import Client
import urllib.request
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
from streamlit_folium import folium_static
import folium
import plotly.express as px
from streamlit_pages.streamlit_pages import MultiPage


import geocoder
from bs4 import BeautifulSoup

from oauth2client.service_account import ServiceAccountCredentials
urllib.request.urlretrieve('https://entendiste.ar/mail/service_account.json',"service_account.json")
from gspread import authorize




scopes = ["https://spreadsheets.google.com/feeds",
                "https://www.googleapis.com/auth/spreadsheets",
                "https://www.googleapis.com/auth/drive",
                "https://www.googleapis.com/auth/drive"] 
cred = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scopes)
from googleapiclient.discovery import build
import requests
import json

send_url = "http://api.ipstack.com/200.41.127.18?access_key=c4db03018a0162547aaabccbd952b16f"
geo_req = requests.get(send_url)
geo_json = json.loads(geo_req.text)
latitude = geo_json['latitude']
longitude = geo_json['longitude']
city = geo_json['city']
st.write(geo_json)
import numpy as np

g = geocoder.ip('me')
lat_ad=g.latlng[0]
lon_ad=g.latlng[1]

df=pd.DataFrame(g.latlng)
st.table(df)
st.write(latitude)
st.write(longitude)
ubi=[latitude,longitude]
m = folium.Map(location=ubi, zoom_start=17,zoom_control=False,                scrollWheelZoom=False,                dragging=False)


#folium.Marker(location=ubi, popup =  'Bco. Francés').add_to(m)
folium.CircleMarker(location=ubi,radius=30, fill_color='green',tooltip=folium.Tooltip('Bco. Francés', permanent=True)).add_to(m) 
