## 네이버 뉴스 크롤링

from selenium import webdriver
import time
import re
import csv

driver = webdriver.Chrome('C:/Temp/chromedriver')

newsname = []
pageNum = 1

url = 'https://program.naver.com/p/18146209/talk'
driver.get(url)
time.sleep(2)

while True:
    newsnode = driver.find_elements_by_css_selector('div.u_cbox_text_wrap > span')

    for i in newsnode:
        newsname.append(i.text)

    try:
        next = driver.find_element_by_css_selector('span > span.u_cbox_ico_more')
        pageNum += 1
        next.click()
    except:
        print("데이터 수집 완료")
        break

    '''if pageNum > 20:
        break
    else:
        next.click()
        time.sleep(3)'''

with open('SBS0809_POLICE1.csv', 'w', newline='', encoding='UTF-8') as f:
    f.write('newsname\n')
    for i in range(len(newsname)):
        f.write(newsname[i] + '\n')