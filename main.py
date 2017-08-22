#!/usr/local/anaconda/bin/python2.7
# -*- coding: utf-8 -*-

import requests
import json
from bs4 import BeautifulSoup

def filter_data_title(tag):
    return tag.has_attr("data-title")

url = 'https://movie.douban.com'
html = requests.get(url).text
soup = BeautifulSoup(html, "lxml")
li = soup.find_all("li", class_="ui-slide-item")
li = soup.find_all(filter_data_title)

li = sorted(li, key=lambda movie: movie["data-rate"], reverse=1)

for el in li:
    print u"片名：" + el["data-title"]
    if el.has_attr("data-actors") and el["data-actors"] is not "":
        print u"主演：" + el["data-actors"]
    else:
        print "无演员信息"
    if el.has_attr("data-director") and el["data-director"] is not "":
        print u"导演：" + el["data-director"]
    else:
        print "无导演信息"
    if el.has_attr("data-rate") and el["data-rate"] is not "":
        print u"评分：" + el["data-rate"]
    else:
        print "尚未评分"
    # print el("li", class_="rating")
    print
    # print el

para = {'type': 'movie', 'tag': u'热门', 'page_limit': '40', 'page_start': '0'}
url1 = "https://movie.douban.com/j/search_subjects?"
movie = requests.get(url1, params=para)
movie = movie.json()

for i in movie['subjects']:
    print 'Name:'+i['title']+'; '+'rate:'+i['rate']


para = {'type': 'tv', 'tag': u'热门', 'page_limit': '40', 'page_start': '0'}
url1 = "https://movie.douban.com/j/search_subjects?"
tv = requests.get(url1, params=para)


tv = tv.json()

print '\n'

for i in tv['subjects']:
    print 'Name:'+i['title']+'; '+'rate:'+i['rate']

# print tv.text
