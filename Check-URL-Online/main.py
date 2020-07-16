import os
import requests

def  check_up(url):
  try:
    r = requests.get(url)
  except :
    r = "error"
  if r == "error":
    print(url, "is down!")
  elif r.status_code == 200:
    print(url, "is up!")

def check_http(url):
  if "http://" not in url:
    url = "http://" + url
  return url

def start(): 
  os.system('clear')
  print("Welcome to IsItDown,py!")
  print("Please write a URL or URLs you want to check. (deparated by comma)")

  input_url = input().split(",")
  for in_url in input_url:
    
    in_url = in_url.strip()
    url = in_url.lower()
    if "." not in url:
      print(url,"is not a valid URL.")
      continue
    
    url = check_http(url)
    check_up(url)

start()

while True:
  s_ans = input("Do you want to start over? y/n ")

  if(s_ans == 'y'):
    start()
  elif(s_ans == 'n'):
    print("ok. bye!")
    break
  else:
    print("That's not a valid answer")