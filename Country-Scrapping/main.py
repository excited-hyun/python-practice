import os
import requests
from bs4 import BeautifulSoup

country = [];
currency_code = [];

def get_info_from_web():
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


os.system("clear")
url = "https://www.iban.com/currency-codes"

print("Hello! Please choose select a country by number:")

get_info_from_web()

n=0

for name in country:
  print('#',n, name)
  n += 1

while True:
  get_num = input('#: ')
  try:
    get_num = int(get_num)
  except:
    print("That wasn't a number")
    continue

  if get_num >= n: 
    print("Choose a number from the list.")
    continue
  else:
    print("You chose",country[get_num])
    print("The currency code is",currency_code[get_num])
    break
