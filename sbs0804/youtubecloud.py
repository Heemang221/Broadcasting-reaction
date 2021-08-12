## 네이버 블로그 크롤링

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import re
import csv

## 워드클라우드

from selenium import webdriver
import time
import re
import csv

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import konlpy
from konlpy.tag import Okt
from collections import Counter
import nltk
import matplotlib
from matplotlib import font_manager, rc
from wordcloud111 import WordCloud

f = open('youtube_jyp.csv', 'r', encoding='UTF-8')
lines = f.readlines()

# title data 합치기
message = ''
for line in lines:
    message = message + re.sub('[^\w]', ' ', line) +''
#message = re.sub('펜트하우스', '', message)
#message = re.sub('우울', '', message)

# 명사 추출
nlp = Okt()
message_N = nlp.nouns(message)

# 단어 빈도 확인
count = Counter(message_N)
word_count = dict()

for tag, counts in count.most_common(50):
    if(len(str(tag))>1):
        word_count[tag] = counts
#         print("%s : %d" % (tag, counts))
        print(tag,':',counts)

from matplotlib import font_manager, rc
font_path = "C:/phm/PYDATAexam/Annyeong/data/THEdog.ttf"   #폰트파일의 위치 C:/phm/PYDATAexam/bucheon/THEdog.ttf
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)
plt.rcParams['font.family'] = 'Malgun Gothic'

plt.figure(figsize=(23,5))
plt.xlabel('키워드')
plt.ylabel('빈도수')
plt.grid(True)

sorted_Keys = sorted(word_count, key=word_count.get, reverse=True)
sorted_Values = sorted(word_count.values(), reverse=True)

plt.bar(range(len(word_count)), sorted_Values, align='center')
plt.xticks(range(len(word_count)), list(sorted_Keys), rotation='75')

plt.show()

font_path = 'C:/phm/BMEULJIROTTF.ttf'
wc = WordCloud(font_path, background_color='ivory', width=800, height=600)
cloud = wc.generate_from_frequencies(word_count)

plt.figure(figsize=(15,8))
plt.imshow(cloud)
plt.axis('off')
plt.show()

# 워드클라우드 png저장
wc.to_file('youtube_jyp.png')