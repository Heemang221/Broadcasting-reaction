import os
from konlpy.tag import Okt
from collections import Counter
from collections import Counter
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
from wordcloud import WordCloud

# Okt 형태소 분석 객체 생성
ok_twitter = Okt()

# 저장된 파일의 위치 탐색 후, file변수에 저장
file = open('SBS0820_2.csv', 'r', encoding='UTF-8')
total_lines = file.readlines() # txt파일을 줄 단위로 읽음
file.close()
my_set = set(total_lines)
my_list = list(my_set)
print(my_list)

# 크롤링 댓글파일 가져와서 reply_text 리스트에 저장
reply_text = []

for line in my_list:
    line = re.sub('아니', '', line)
    line = re.sub('아니라', '', line)
    reply_text.append(line[:-1])

# 형태소 분류하고 확인 하기
sentences_tag = []
for sentence in reply_text:
  morph = ok_twitter.pos(sentence)
  sentences_tag.append(morph)
  print(morph) # 분석된 1건 결과 확인
  print('-' * 30)

# 명사만 출력해 보기
for my_sentence in sentences_tag:
	for word, tag in my_sentence:
		if tag in ['Noun']:
			print(word)

# 필요한 품사만 추출해보기(명사를 bucket list에 담기)
bucket_list = []
for my_sentence in sentences_tag:
    for word, tag in my_sentence:
        if tag in ['Noun']:
            bucket_list.append(word)

print(bucket_list)


# 단어 빈도수 구하기
# 각 원소의 출현 횟수를 계산하는 Counter 모듈을 활용한다.
from collections import Counter
counts = Counter(bucket_list)
print(counts)

# 명사 빈도 순서대로 상위 30개 출력
print(counts.most_common(20))

# 명사와 형용사를 모두 추출하고 상위 50개를 출력
bucket_list_2 = []
for my_sentence in sentences_tag:
  for word, tag in my_sentence:
    if tag in ['Adjective']:
      bucket_list_2.append(word)
counts = Counter(bucket_list_2)
print(counts.most_common(30))

word_count = {}

for tag, count in counts.most_common(50):
    if(len(str(tag))>=2):
        word_count[tag] = count
#         print("%s : %d" % (tag, counts))
        print(tag,':',count)


font_path = 'C:/phm/BMEULJIROTTF.ttf'
wc = WordCloud(font_path, background_color='white', max_words=10, width=800, height=600)
cloud = wc.generate_from_frequencies(word_count)

plt.figure(figsize=(15,8))
plt.imshow(cloud)
plt.axis('off')
plt.show()

# 워드클라우드 png저장
wc.to_file('doctor_2.png')