import schedule
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import re
import csv
import pandas as pd
from selenium.webdriver.common.keys import Keys
from tqdm import tqdm

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

### 0. 수요일 프라임 시간 예능
WED_program = ["골목식당", "골때리는그녀들", "라디오스타", "표리부동", "랜선장터", "유퀴즈", "뽕숭아학당"]

### 1. 시청률 수집

WED = []
for i in WED_program:
    WED.append(i + ' 시청률')

driver = webdriver.Chrome('C:/Temp/chromedriver')
url = "http://www.naver.com"

rating = []

for pro in WED:
    driver.get(url)
    time.sleep(2)
    selector = '#query'

    # 검색 키워드 넣는 곳 클릭
    search = driver.find_element_by_css_selector(selector)
    search.click()

    # 검색 키워드 입력
    elem = driver.find_element_by_css_selector(selector)
    elem.send_keys(pro)
    elem.send_keys(Keys.ENTER)
    time.sleep(2)

    node = driver.find_element_by_css_selector('div > strong > span')
    rating.append(node.text)

print(rating)

### 2-1. 네이버톡

WED_ntalk = ["유퀴즈", "뽕숭아학당"]

ntalk = []

for pro_n in WED_ntalk:
    driver.get(url)
    time.sleep(2)
    selector = '#query'

    # 검색 키워드 넣는 곳 클릭
    search = driver.find_element_by_css_selector(selector)
    search.click()

    # 검색 키워드 입력
    elem = driver.find_element_by_css_selector(selector)
    elem.send_keys(pro_n)
    elem.send_keys(Keys.ENTER)
    time.sleep(2)

    node = driver.find_element_by_css_selector('div.talk_area > span')
    ntalk.append(node.text)

print(ntalk)

### 2-2. 다음톡

WED_dtalk = ["골목식당", "라디오스타", "랜선장터"]
durl = "https://entertain.daum.net/tv/list/talk"

dtalk = []

for pro_d in WED_dtalk:
    driver.get(durl)
    time.sleep(2)
    selector = '#searchKeyword'

    # 검색 키워드 넣는 곳 클릭
    search = driver.find_element_by_css_selector(selector)
    search.click()

    # 검색 키워드 입력
    elem = driver.find_element_by_css_selector(selector)
    elem.send_keys(pro_d)
    elem.send_keys(Keys.ENTER)
    time.sleep(2)

    node_c = driver.find_element_by_css_selector('#programListWrap > li > div > strong.emph_g.talk_program > span')
    dtalk.append(node_c.text)

print(dtalk)

### 3. 네이버TV 조회수

'''def job():
    print("sbs 화이팅")

schedule.every().day.at("08:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)'''