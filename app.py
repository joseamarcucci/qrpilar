
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

import os
import plotly.express as px
from datetime import date
st.markdown("""

<style>
.css-wmn9kq{
    font-size: 0.8rem;
    font-family: "Oswald";
    text-align: left;
    padding: 0.5rem;
    line-height: 1.3;
}
.css-adptcx {display:none}
.st-dv {
    padding-left: 2px;
    font-family: 'Oswald';
}
.st-dx {
    padding-left: 8px;
    font-family: 'Oswald';
}
.st-em {
    vertical-align: middle;
    font-family: 'Oswald';
}
.css-y37zgl {
    font-size: 0.8rem;
    font-family: "Oswald";
    text-align: left;
    padding: 0.5rem;
    line-height: 1.3;
}

</style>
""", unsafe_allow_html=True)

import pytz
utc = pytz.utc
utc.zone
argentina = pytz.timezone('America/Argentina/Buenos_Aires')
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
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
       
footer {visibility: hidden;}
header {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
st.image("https://entendiste.ar/mail/logousaltr.png")
st.markdown('<link href="https://fonts.googleapis.com/css2?family=Oswald" rel="stylesheet"><style>.st-bg,.css-177yq5e, .st-bo,.st-bf,.st-b4,.st-b7,.st-be,.st-bi,.st-dq {font-family: Oswald, Arial, sans-serif;font-size:16px;}.css-1ekf893 {margin-bottom: -1rem;font-family: Oswald;}.css-1v0mbdj {margin-top: -60px;}body{font-family: "Oswald", Arial, sans-serif;}</style>', unsafe_allow_html=True)
from datetime import timezone, datetime, timedelta
dia=datetime.now(argentina).strftime('%A %d-%m-%Y %H:%M')
dia=dia.replace('Monday','Lunes')
dia=dia.replace('Tuesday','Martes')
dia=dia.replace('Wednesday','Miércoles')
dia=dia.replace('Thursday','Jueves')
dia=dia.replace('Friday','Vierneses')
dia=dia.replace('Saturday','Sábado')

st.markdown('<div style="text-align:left; border-bottom:1px solid #008357;border-top:1px solid #008357;font-family: Oswald">CAMPUS NUESTRA SEÑORA DEL PILAR</div>', unsafe_allow_html=True)

st.markdown('<div style="text-align:left; font-size:18px;font-family: Oswald">USAL Dirección de Logística y Servicios</div><br>', unsafe_allow_html=True)
st.markdown('<div style="text-align:left; font-size:24px;border-bottom:1px solid #008357;font-family: Oswald"><b>CONTROL DE ACCESO DOCENTES</b></div><br>', unsafe_allow_html=True)
st.markdown('<div style="text-align:left; font-size:14px;font-family: Oswald;color:#e65100"><b>'+dia+'</b></div><br>', unsafe_allow_html=True)
#st.write('<style>div.row-widget.stRadio> div{flex-direction:row;}</style>', unsafe_allow_html=True)




dni=st.text_input("Ingresar DNI:")
if dni:
    try:
      cell = sheet2.find(dni) 
      row_number = cell.row

      nombre=sheet2.acell('C'+str(row_number)).value
      apellido=sheet2.acell('D'+str(row_number)).value
      dni=sheet2.acell('E'+str(row_number)).value
      celu=sheet2.acell('F'+str(row_number)).value 
      mail= sheet2.acell('G'+str(row_number)).value 
      send_url = "http://api.ipstack.com/200.41.127.18?access_key=c4db03018a0162547aaabccbd952b16f"
      geo_req = requests.get(send_url)
      geo_json = json.loads(geo_req.text)
      latitude = geo_json['latitude']
      longitude = geo_json['longitude']
      city = geo_json['city']
      #st.write(geo_json)
      import numpy as np

      g = geocoder.ip('me')
      lat_ad=g.latlng[0]
      lon_ad=g.latlng[1]

      #df=pd.DataFrame(g.latlng)
      #st.table(df)
      #st.write(latitude)
      #st.write(longitude) 

      ubi=[-34.4351289,-58.9266003]

      sheet3.append_row([datetime.now(argentina).strftime('%d-%m-%Y %H:%M'),nombre,apellido,dni,celu,mail])
      st.warning(nombre+' '+apellido+ 'su acceso ha sido registrado, gracias')
    except gspread.exceptions.CellNotFound:

      st.warning('Verificar DNI')
