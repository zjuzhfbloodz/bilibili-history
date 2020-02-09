#!/usr/bin/env python


# -*- coding: utf-8 -*- 

"""
@File: jieba.py

Created on 02 07 18:37 2020

@Authr: zhf12341 from Mr.Zhao

"""

import jieba
from wordcloud import WordCloud
import string
import zhon.hanzi
import jieba.posseg as pseg
import imageio



"""分词 jieba分词github：https://github.com/fxsjy/jieba"""
def word_split(content, txt):
    #通过词性筛选掉一些无用词
    jieba.add_word('郭老师',tag = 'n')
    anword = [x.word for x in pseg.cut(content) if (x.flag.startswith('a') or x.flag.startswith('n')) and x.word not in txt]
    return(str(anword))


"""词云"""
def word_cloud(wordlist,pic):#pic是图片名称
    #读取图片
    ground = imageio.imread("1.jpg")

    """生成词云，prefer_horizontal是水平词比例，font_path在C:\Windows\Fonts里是字体，
    colormap在 https://blog.csdn.net/python798/article/details/82810104 里面
    https://www.cnblogs.com/delav/articles/7837975.html参数"""

    wc = WordCloud(width = 1600,height = 800,background_color = "white",max_words = 50,mask = ground,
                   scale = 10,max_font_size = 500,random_state = 42,font_path = "方正粗黑宋简体.ttf",font_step = 2,
                   prefer_horizontal = 1,mode = 'RGBA',colormap = 'Accent')
    wc.generate(wordlist)
    wc.to_file(pic)


"""数据清洗"""
def word_clean(wl,txt):
    wl = wl.split()
    for i in wl:
        if i.isdigit() or i in txt or i in zhon.hanzi.punctuation or i in string.punctuation:
            wl.remove(i)
    wl = str(wl).replace("'","")
    wl = wl.replace(",","")
    return wl