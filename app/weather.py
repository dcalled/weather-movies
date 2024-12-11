#https://archive-api.open-meteo.com/v1/archive?latitude=6.2518&longitude=-75.5636&start_date=2024-11-25&end_date=2024-11-25&daily=temperature_2m_max,temperature_2m_min,temperature_2m_mean&timezone=America%2FNew_York

import urllib.parse
import requests
import os
import urllib

def getTemperature(date):
  url = f"https://archive-api.open-meteo.com/v1/archive?latitude=6.2518&longitude=-75.5636&start_date={date}&end_date={date}&daily=temperature_2m_max,temperature_2m_min,temperature_2m_mean&timezone=America%2FNew_York"
  print(url)
  response = requests.get(url)
  return response.json()