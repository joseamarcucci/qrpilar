
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
gclient = authorize(cred)
sheet2 = gclient.open('docentesp').worksheet('docentes')
sheet3 = gclient.open('docentesp').worksheet('asistencia')
from googleapiclient.discovery import build
import requests
import json
dni=st.text_input("DNI")
if dni:
    cell = sheet2.find(dni) 
    row_number = cell.row

    nombre=sheet2.acell('C'+str(row_number)).value
    dni=sheet2.acell('E'+str(row_number)).value
    celu=sheet2.acell('F'+str(row_number)).value 
    mail= sheet2.acell('G'+str(row_number)).value 
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
    #st.table(df)
    st.write(latitude)
    st.write(longitude)
    
    ubi=[-34.4351289,-58.9266003]
    m = folium.Map(location=ubi, zoom_start=17,zoom_control=False,                scrollWheelZoom=False,                dragging=False)


    #folium.Marker(location=ubi, popup =  nombre).add_to(m)
    folium.CircleMarker(location=ubi,radius=30, fill_color='green',tooltip=folium.Tooltip(nombre, permanent=True)).add_to(m) 
    folium_static(m)
    sheet3.append_row([nombre,dni,celu,mail,today])
import requests


def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name")
    }
    return location_data


st.write(get_location())
