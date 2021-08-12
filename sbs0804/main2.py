from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import re
import csv
import pandas as pd


# 18일 예능(V)
keywords = ['미운우리새끼', '1박2일시즌4', '동물농장', '전국노래자랑', '복면가왕', '사장님귀는당나귀귀',
            '슈퍼맨이돌아왔다', '구해줘홈즈', '뭉쳐야쏜다', '1호가될순없어', '런닝맨', '집사부일체',
            '신비한TV서프라이즈', '출발비디오여행', '선을넘는녀석들', '이제만나러갑니다', '대탈출4',
            '돌싱글즈', '코미디빅리그', '방구석1열']


driver = webdriver.Chrome('C:/Temp/chromedriver')
blogcount = []

for idx, keyword in enumerate(keywords):

    print(f'idx: {idx}_{keyword}')
    url = 'https://tv.naver.com/search/clip?query=' + str(keyword) + '&isTag=false'
    driver.get(url)
    time.sleep(2)

    txt = []

    blognodes = driver.find_elements_by_css_selector('div > div > dl > dd > time')

    for i in blognodes:
        txt.append(i.text)

    if '돌싱글즈' in keyword:
        print('pause')

    find = False
    if '1주 전' in txt:
        for i in range(1, 21):
            blognode = driver.find_element_by_css_selector('div:nth-child(' + str(i) + ') > div > div > dl > dd > time')

            if blognode.text == '1주 전':
                find = True
                node = driver.find_element_by_css_selector(
                    'div:nth-child(' + str(i) + ') > div > div > dl > dd > span.cds_ifc.cnp')
                tv_count = re.findall('\d+', node.text)
                tv_count = ''.join(tv_count)
                tmp_dict = {'name': keyword, 'tvcount': tv_count}
                print(tmp_dict)
                blogcount.append(tmp_dict)
                break

    if find == False:
        print('일주전이 없음')
        tmp_dict = {'name': keyword, 'tvcount': '0'}
        print(tmp_dict)
        blogcount.append(tmp_dict)

for count, b in enumerate(blogcount):
    print(f'idx:{count} {b}')

keywords = [b['name'] for b in blogcount]
tvcount  = [b['tvcount'] for b in blogcount]

df = pd.DataFrame({'name': keywords,
                   'tvcount': tvcount})
print(df)
df.to_csv('Vtv18.csv')
