from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
from tqdm import tqdm

driver = webdriver.Chrome('C:/Temp/chromedriver')
driver.implicitly_wait(3)

url = 'https://twitter.com/home'
driver.get(url)

keywords = ['슬의생']
text_list = []

for keyword in keywords:
    # 트위터 접속
    time.sleep(2)
    css_selector = '#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div.css-1dbjc4n.r-aqfbo4.r-zso239.r-1jocfgc > div > div.css-1dbjc4n.r-gtdqiz.r-1jocfgc > div > div > div > div.css-1dbjc4n.r-1awozwy.r-aqfbo4.r-14lw9ot.r-18u37iz.r-1h3ijdo.r-6gpygo.r-15ysp7h.r-1xcajam.r-ipm5af.r-1jocfgc.r-136ojw6 > div > div > div > form > div.css-1dbjc4n.r-1wbh5a2 > div > div > label > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2 > div > input'

    # 검색 키워드 클릭
    src = driver.find_element_by_css_selector(css_selector)
    src.click()

    # 검색 키워드 입력
    elem = driver.find_element_by_css_selector(css_selector)
    elem.send_keys(keyword)
    elem.send_keys(Keys.ENTER)
    time.sleep(2)

    # Latest 클릭
    src = driver.find_element_by_css_selector(
        '#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > div.css-1dbjc4n.r-aqfbo4.r-14lw9ot.r-j5o65s.r-rull8r.r-qklmqi.r-gtdqiz.r-1gn8etr.r-1g40b8q > div.css-1dbjc4n.r-14lw9ot > nav > div > div.css-1dbjc4n.r-1adg3ll.r-16y2uox.r-1wbh5a2.r-1pi2tsx.r-1udh08x > div > div:nth-child(2) > a > div')
    src.click()
    time.sleep(2)

    # 스크롤
    SCROLL_PAUSE_TIME = 4

    # 스크롤 높이
    last_height = driver.execute_script("return document.body.scrollHeight")
    count = 0

    for scroll in range(30):
        count += 1
        # 스크롤 무빙
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # 페이지 로드 대기
        time.sleep(SCROLL_PAUSE_TIME)
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight-50);")  # 맨 마지막까지 스크롤하면 바로 아래 리스트가 뜨지 않는 경우가 있기 때문에 -50 추가
        time.sleep(SCROLL_PAUSE_TIME)

        # 수집
        id_selectors = driver.find_elements_by_css_selector(
            'div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-kzbkwu > div:nth-child(2) > div:nth-child(1) > div')
        for i in id_selectors:
            text_list.append(i.text)
        print(len(id_selectors), len(text_list), count)

        # 스크롤이 더이상 변화가 없으면 스크롤 이동 중단
        new_height = driver.execute_script("return document.body.scrollHeight")
        if last_height == new_height:
            break
        last_height = new_height

    print(keyword, ': 수집완료', len(text_list))
text_set = set(text_list)
print(len(text_set))