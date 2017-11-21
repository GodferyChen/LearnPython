import nltk
from bs4 import BeautifulSoup
import urllib.request

from nltk.corpus import stopwords

response = urllib.request.urlopen('http://php.net/')
html = response.read()
soup = BeautifulSoup(html, 'html5lib')
# 通过BeautifulSoup模块来清洗这样的文字
text = soup.get_text(strip=True)
# 将文本转换成tokens
tokens = text.split()
# 清除一些无效的token
clean_tokens = list()
sr = stopwords.words('english')
for token in tokens:
    if not token in sr:
        clean_tokens.append(token)
# 统计词频
freq = nltk.FreqDist(clean_tokens)
for key, val in freq.items():
    print(str(key) + ':' + str(val))

# 做出频率分布图
freq.plot(20, cumulative=False)
