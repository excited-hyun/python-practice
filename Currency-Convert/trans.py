import requests
from bs4 import BeautifulSoup

def transfer_money(from_c, to_c, c_num):
  url = f"https://transferwise.com/gb/currency-converter/{from_c}-to-{to_c}-rate?amount={c_num}"

  result = requests.get(url)
  soup = BeautifulSoup(result.text, "html.parser")
  rate = soup.find("span", {"class": "text-success"}).string
  amount = c_num * float(rate)
  return amount