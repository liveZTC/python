# -*- coding:utf-8 -*-

#基础爬虫开发第一步

import requests as rs
import json,os
from bs4 import BeautifulSoup as bs

#临时文件夹
file_path = os.path.join('d:\\','temp')
file_path = os.path.join(file_path,u'爬虫开发临时文件夹')
if not os.path.isdir(file_path):
    os.makedirs(file_path)

# 1.抓取电影列表数据
r = rs.get('https://movie.douban.com/nowplaying/hangzhou/')
# print r.text
html = r.text.encode('utf-8')

soup = bs(html,"html.parser")

nowplaying_movie = soup.find_all('div', id='nowplaying')

nowplaying_movie_list = nowplaying_movie[0].find_all('li', class_='list-item')

nowplaying_list  = []

for item in nowplaying_movie_list:
    film_info = {}
    film_info['id'], film_info['name'] = item['data-subject'], item['data-title']
    nowplaying_list.append(film_info)

# print nowplaying_list

# 2.对短评页面进行分析

requrl = 'https://movie.douban.com/subject/'+nowplaying_list[0]['id']+'/comments?start=0&limit=20'

r = rs.get(requrl)

html = r.text.encode('utf-8')

soup = bs(html,"html.parser")

comment_list_html = soup.find_all('div', class = 'comment')

for item in comment_list:
    comment_info
    comment_info = 



