#!/usr/bin/env python

# -*- coding: utf-8 -*- 

"""
@File: bilibili_history.py

Created on 02 08 20:13 2020

@Authr: zhf12341 from Mr.Zhao

"""

import requests
import re
from word_to_cloud import word_cloud,word_split,word_clean



"""缺参数了就加入host和referer，尽量多加入参数吧"""
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
           'Cookie' : "CURRENT_FNVAL=16; _uuid=3646CDB7-35D8-595D-40E2-1307FDD3103030037infoc; buvid3=BD7CE9A8-2751-43FD-9E83-3E3678490758155816infoc; LIVE_BUVID=AUTO3015795099326174; rpdid=|(J|)JkYl~~)0J'ul~ml|mmJk; sid=ia11rrab; DedeUserID=401642617; DedeUserID__ckMd5=329d540d68f2da28; SESSDATA=b23e55e0%2C1582900377%2C7b571111; bili_jct=a0177352c95a53c3a27abfbbcee2102e; im_notify_type_401642617=0; bp_t_offset_401642617=353259574040344877; INTVER=1",
           'Host' : 'api.bilibili.com',
           'referer' : 'http://www.bilibili.com/'
           }

base_url = 'https://api.bilibili.com/x/v2/history?callback=jQuery22407895204370128657_1581168670394&pn={}&ps=100&jsonp=jsonp&_={}'


def get_history(base_url,headers):

    """得到自己的历史记录"""
    bili_history = {}
    for i in range(1,11):
        response = requests.get(base_url.format(i,1581168670394+i),headers = headers).content.decode('utf-8')
        """re不贪婪用？，贪婪用*"""
        title = re.findall('"title":"(.*?)","pubdate"',response)
        kind = re.findall('"tname":"(.*?)","copyright"',response)
        for j in range(len(title)):
            bili_history[title[j]] = kind[j]
    return bili_history


def history_file(bili_history):

    """写入文件"""
    with open("history_name.txt",'w',encoding = 'utf-8') as f:
        f.write("  ".join(bili_history.keys()))
    with open("history_kind.txt",'w',encoding = 'utf-8') as f:
        f.write("  ".join(bili_history.values()))


def get_cloud():

    """生成云图"""
    """历史记录名称"""
    with open("history_name.txt",'r',encoding = 'utf-8') as f:
        name = f.read()
    word_cloud(word_clean(word_split(name,""),""),"history_name.png")

    """历史记录类别"""
    with open("history_kind.txt",'r',encoding = 'utf-8') as f:
        name = f.read()
    word_cloud(word_clean(word_split(name,""),""),"history_kind.png")


def main():

    """主程序"""
    history = get_history(base_url,headers)
    history_file(history)
    get_cloud()


if __name__ == "__main__":
    main()

