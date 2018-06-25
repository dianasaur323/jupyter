import requests
import pandas as pd

url = 'https://api.iextrading.com/1.0/stock/aapl/chart/2y'

response = requests.get(url)
data = response.json()
print(data)
