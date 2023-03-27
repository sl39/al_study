from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas as pd
import re
from time import sleep
import requests

ls = []


url = "https://www.diningcode.com/list.dc?query=부산%20" + "부전동"

driver = webdriver.Chrome('chromedriver')
driver.implicitly_wait(3)
driver.get(url)
button = driver.find_element('xpath' ,'//*[@id="map"]/button[2]')
while True:
  try:
    button.click()
    sleep(1)
  except:
    break

hreflist = []
i = 1
while True:
  try:
    href = driver.find_element("xpath",f'//*[@id="root"]/div/div[1]/div[3]/ol/li[{i}]')
    href = href.find_elements(By.CSS_SELECTOR,'a')[0]
    href = href.get_attribute('href')
    hreflist.append(href)
    i+= 1
  except:
    break
driver.close()
for resto in hreflist:
  driver = webdriver.Chrome('chromedriver')
  driver.implicitly_wait(3)
  driver.get(resto)

  try:
    title = driver.find_element('xpath' , '//*[@id="div_profile"]/div[1]/div[1]/p').text #title
  except:
    title = ""

  try:
    tag = driver.find_element('xpath' , '//*[@id="div_profile"]/div[1]/div[2]').text 
    tag = tag.split('|')
    tag = tag[1]
    tag = tag.split(',')
    for i in range(len(tag)):
      tag[i] = tag[i].strip()   # 태그
  except:
    tag = []

  try:
    grade = driver.find_element('xpath' , '//*[@id="div_profile"]/div[1]/div[3]/p/strong').text[:-1] # grade
  except:
    grade = ""
  try:
    point = driver.find_element('xpath' , '//*[@id="div_profile"]/div[1]/div[3]/p/span[1]').text
    point = point.split()
    people = point[0]
    point = point[2]
    people = people[:-2] # people
    point = point[:-1] # point
  except:
    people = ""
    point = ""
  
  try:
    location = driver.find_element('xpath' , '//*[@id="div_profile"]/div[2]/ul')
    location = location.find_elements(By.CSS_SELECTOR,'li')[0].text # location
  except:
    location = ""
  try:
    menu = driver.find_element('xpath' , '//*[@id="div_detail"]/div[2]/ul')
    menu = menu.find_elements(By.CSS_SELECTOR,'li')
    menus = []
    button = driver.find_element('xpath' ,'//*[@id="div_detail"]/div[2]/p[2]/a').click()
    lenth = len(menu)
    for i in menu:
      mm = i.text
      mm = mm.split('\n')
      menus.append(mm) ## menu
  except:
    menus= []
  ls.append([title,tag,grade,people,point,location,menus,resto])
  driver.close()


col = ['title','tag','grade','people','point','location','menus','url']
df =pd.DataFrame(ls,columns=col)

df.to_csv('test.csv',index=False, encoding='UTF-8')


# 좌표가져오는거
driver = webdriver.Chrome('chromedriver')
driver.implicitly_wait(3)
driver.get('https://address.dawul.co.kr/#')
search_box = driver.find_element('xpath' , '//*[@id="input_juso"]')
search_button = driver.find_element('xpath' , '//*[@id="btnSch"]')
search_box.send_keys(location)
search_button.click()
loc = driver.find_element('xpath' , '//*[@id="insert_data_5"]')
loc.text