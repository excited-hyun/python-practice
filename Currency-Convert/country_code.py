import os
import requests
from bs4 import BeautifulSoup

url = "https://www.iban.com/currency-codes"

def get_info_from_web(country, currency_code):
  result = requests.get(url)

  soup = BeautifulSoup(result.text, "html.parser")

  table_info = soup.find("table")
  tr_info = table_info.find_all("tr")

  for info in tr_info[1:]:
    temp = {}
    temp['country'] = info.find_next("td").string
    temp['currency'] = info.find_next("td").find_next("td").string
    temp['code'] =  info.find_next("td").find_next("td").find_next("td").string
    temp['number'] = info.find_next("td").find_next("td").find_next("td").find_next("td").string
    if temp['code'] != None:
      country.append(temp['country'].lower().capitalize())
      currency_code.append(temp['code'])
