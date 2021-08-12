import pandas as pd
import re
import matplotlib.pyplot as plt
from konlpy.tag import Okt
from collections import Counter
import nltk
import matplotlib
from matplotlib import font_manager, rc
from wordcloud import WordCloud

# 파일 불러오기
data = pd.read_csv('twiiter.csv')
data.drop_duplicates() # 중복행 제거

# title data 합치기 (제거: '\n')
message = ''
for item in data['text']:
    message = message + re.sub('[^\w]', ' ', item) +''

# 정규화 (제거할 단어)
message = re.sub('뽕숭아학당', '', message)
message = re.sub('아침마당', '', message)
message = re.sub('월간집', '', message)
message = re.sub('백종원의 골목식당', '', message)

# 명사 추출
nlp = Okt()
message_N = nlp.nouns(message)
# message_N

# 단어 빈도 확인
count = Counter(message_N)
word_count = dict()

for tag, counts in count.most_common(50):
    if(len(str(tag))>1):
        word_count[tag] = counts
        print(tag,':',counts)

from matplotlib import font_manager, rc
font_path = 'C:/phm/BMEULJIROTTF.ttf'   #폰트파일의 위치
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

plt.figure(figsize=(23,5))
plt.xlabel('키워드')
plt.ylabel('빈도수')
plt.grid(True)

sorted_Keys = sorted(word_count, key=word_count.get, reverse=True)
sorted_Values = sorted(word_count.values(), reverse=True)

plt.bar(range(len(word_count)), sorted_Values, align='center')
plt.xticks(range(len(word_count)), list(sorted_Keys), rotation='75')

plt.show()

wc = WordCloud(font_path, background_color='ivory', width=800, height=600)
cloud=wc.generate_from_frequencies(word_count)

plt.figure(figsize=(15,8))
plt.imshow(cloud)
plt.axis('off')
plt.show()

# 워드클라우드 png저장
wc.to_file('wordcloud_twitter.png')