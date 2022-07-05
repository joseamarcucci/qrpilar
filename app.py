
import streamlit as st
st.set_page_config(
page_title="Envios CLAYSS",
page_icon="https://noticias.clayss.org/sites/default/files/favicon.ico.png",
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
st.write(g.latlng)
