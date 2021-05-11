import jieba
import numpy as np
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup

url = 'https://s.weibo.com/top/summary?Refer=top_hot&topnav=1&wvr=6'

if __name__ == '__main__':
    # 微博爬虫
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text, 'html.parser')
    data = soup.find_all('a')
    d_list = []
    for item in data:
        d_list.append(item.text)
    words = d_list[4:-11:]
    # 中文分词
    with open('./data/test.txt', 'w') as f:
        f.write('\n'.join(words))

    text = open("./data/test.txt", encoding='utf8').read()
    text = text.replace('\n', "")
    # 分词，返回结果为词的列表
    text_cut = jieba.lcut(text)
    # 将分好的词用某个符号分割开连成字符串
    text_cut = ' '.join(text_cut)
    # 导入停词
    # 用于去掉文本中类似于'啊'、'你'，'我'之类的词
    # stop_words = open("F:/NLP/chinese corpus/stopwords/stop_words_zh.txt", encoding="utf8").read().split("\n")

    # 使用WordCloud生成词云
    backgroud = np.array(Image.open('./data/fuzi.jpeg'))
    word_cloud = WordCloud(font_path="./msyh.ttf",  # 设置词云字体
                           mask=backgroud,  # 设置蒙层
                           background_color="white",  # 词云图的背景颜色
                           stopwords=[]).generate(text_cut)  # 去掉的停词

    # 运用matplotlib展现结果
    plt.subplots(figsize=(12, 8))
    plt.imshow(word_cloud)
    plt.axis("off")

    word_cloud.to_file("test.png")
