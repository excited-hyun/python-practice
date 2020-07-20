import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")
alba_url = "http://www.alba.co.kr"

def all_csv_delete():
  dir_name = os.path.dirname(os.path.realpath("__file__"))
  test = os.listdir(dir_name)
  for item in test:
    if item.endswith(".csv"):
      os.remove(os.path.join(dir_name, item))

def make_csv(name, jobs): 
  file = open(f"{name}.csv", mode="w")
  writer = csv.writer(file)
  writer.writerow(["place","title","time", "pay", "date"])
  try:
    for job in jobs:
      writer.writerow(list(job.values()))
  except: return


def get_jobs(url):
  try:
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    all_info = soup.find("div", {"id":"NormalInfo"}).find("tbody")
    brand_info = all_info.find_all("tr", {"class":""})
    jobs = []
    for info in brand_info:
      try:
        brand_location = info.find("td", {"class": "local"}).get_text(strip=True)
        brand_title = info.find("td", {"class": "title"}).find("span", {"class": "company"}).get_text(strip=True)
        brand_time = info.find("td", {"class": "data"}).find("span", {"class": "time"}).get_text(strip=True)
        brand_pay1 = info.find("td", {"class": "pay"}).find("span", {"class": "payIcon"}).get_text(strip=True)
        brand_pay2 = info.find("td", {"class": "pay"}).find("span", {"class": "number"}).get_text(strip=True)
        brand_pay = brand_pay1 + brand_pay2
        brand_date = info.find("td", {"class": "regDate last"}).get_text(strip=True)

        jobs.append({"location": brand_location, "title": brand_title, "time": brand_time, "pay": brand_pay,"date": brand_date})
      except: continue
    return jobs
  except: return
  

def get_company_url():
  result = requests.get(alba_url)

  soup = BeautifulSoup(result.text, "html.parser")

  brands = soup.find("div", {"id": "MainSuperBrand"})
  brands_ul = brands.find("ul", {"class": "goodsBox"})
  brands_url = brands_ul.find_all('a', {"class": "goodsBox-info"})
  brand_url = []
  brand_name = []
  for url in brands_url:
    try:
      brand_url.append(url["href"])
      brand_name.append(url.find("span", {"class": "company"}).get_text(strip=True))
    except: continue
  n=0
  for url in brand_url:
    jobs = get_jobs(f"{url}job/brand/")
    make_csv(brand_name[n], jobs)
    n+=1

all_csv_delete()
get_company_url()
