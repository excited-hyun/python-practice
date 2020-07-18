import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency
from country_code import get_info_from_web
from trans import transfer_money

country = [];
currency_code = [];

os.system("clear")

print("Welcome to CurrencyConvert PRO 2000")

get_info_from_web(country, currency_code)
n=0

for name in country:
  print('#',n, name)
  n += 1

print("\nWhere are you from? Choose a country by number\n")
while True:
  from_num = input('#: ')
  try:
    from_num = int(from_num)
  except:
    print("That wasn't a number")
    continue

  if from_num >= n: 
    print("Choose a number from the list.")
    continue
  else:
    print(country[from_num])
    break

print("\nNow choose another country\n")
while True:
  to_num = input('#: ')
  try:
    to_num = int(to_num)
  except:
    print("That wasn't a number")
    continue

  if to_num >= n: 
    print("Choose a number from the list.")
    continue
  else:
    print(country[to_num])
    break


while True:
  print(f"\nHow many {currency_code[from_num]} do you want to convert to {currency_code[to_num]}?")
  convert_num = input()
  try:
    convert_num = int(convert_num)
    break
  except:
    print("That wasn't a number")
    continue

amount = transfer_money(currency_code[from_num], currency_code[to_num], convert_num)

"""
Use the 'format_currency' function to format the output of the conversion
format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR" (no need to change this one))
"""

print(format_currency(convert_num, f"{currency_code[from_num]}", locale="ko_KR"),"is",format_currency(amount, f"{currency_code[to_num]}", locale="ko_KR"))