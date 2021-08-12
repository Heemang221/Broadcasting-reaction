from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome('C:/Temp/chromedriver')
driver.get('https://www.youtube.com/watch?v=CsI-RXDqHk0')

time.sleep(3)

last_page_height = driver.execute_script("return document.documentElement.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(3.0)
    new_page_height = driver.execute_script("return document.documentElement.scrollHeight")

    if new_page_height == last_page_height:
        break
    last_page_height = new_page_height

html_source = driver.page_source

driver.close()

soup = BeautifulSoup(html_source, 'lxml')

youtube_user_IDs = soup.select('div#header-author > a > span')
youtube_comments = soup.select('yt-formatted-string#content-text')

youtube_comments = soup.select('yt-formatted-string#content-text')

for i in range(len(youtube_user_IDs)):
    str_tmp = str(youtube_user_IDs[i].text)
    str_tmp = str_tmp.replace('\n', '')
    str_tmp = str_tmp.replace('\t', '')
    str_tmp = str_tmp.replace(' ', '')
    str_youtube_userIDs.append(str_tmp)

    str_tmp = str(youtube_comments[i].text)
    str_tmp = str_tmp.replace('\n', '')
    str_tmp = str_tmp.replace('\t', '')
    str_tmp = str_tmp.replace(' ', '')

    str_youtube_comments.append(str_tmp)

for i in range(len(str_youtube_userIDs)):
    print(str_youtube_userIDs[i], str_youtube_comments[i])