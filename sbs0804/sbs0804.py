from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import re
import csv
import pandas as pd

keywords = ['인간극장', '아침마당', '조선팝드랍더비트', 'KBS더라이브', 'KBS표리부동', '지구여행자', '모닝와이드',
           '백종원의골목식당', '프리한닥터W', 'TVN더로드', '쏭쏭뮤지엄',
            'JTBC다채로운 아침', 'JTBC뉴체인지', 'JTBC사건반장', '정치부회의', 'JTBC썰전', '월간집', '세레머니클럽',
           '20세기를 움직인 101사건들', '동해수호대', '굿모닝 정보세상', '신통방통', '세계테마기행', '시사쇼 이것이 정치다', '백세누리쇼', '퍼펙트 라이프', '뽕숭아학당',
           '고쳐듀오', '채널A행복한아침', '김진의 돌직구 쇼', '관찰카메라24', '생생 정보마당', '골든타임 씨그날', '나는 자연인이다', 'MBN국제부부']

sDate = '20210804'
eDate = '20210804'

driver = webdriver.Chrome('C:/Temp/chromedriver')
blogcount = []

for keyword in keywords:
    url = 'https://search.zum.com/search.zum?method=news&option=accu&query=' + str(keyword) + '&rd=1&startdate=' + str(
        sDate) + '&enddate=' + str(sDate) + '&datetype=input&scp=0'
    driver.get(url)
    time.sleep(2)

    try:
        blognode = driver.find_element_by_css_selector(
            'div.section.section_sc.news_sc.tab_page.no_border_btm.doc_category_news > div > span')
        blogcount.append(blognode.text)
    except Exception as ex:
        print(ex)
        blogcount.append('/ 0')

blogcount2 = []
korean = re.compile('[\u3131-\u3163\uac00-\ud7a3]+')
for i in blogcount:
    blogcount2.append(re.sub(korean, '', i))

blogcount3 = []
for a in blogcount2:
    blogcount3.append(a[a.find('/') + 2:])

df = pd.DataFrame({'name': keywords,
                   'newscount': blogcount3})
print(df)
df.to_csv('Ezum16.csv')