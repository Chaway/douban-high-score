#!/usr/local/anaconda/bin/python2.7
# -*- coding: utf-8 -*-

import requests
import json
from bs4 import BeautifulSoup

class Douban(object):
    def __init__(self, url):
        self.url = url
        self.popular_movies = []
        self.new_movies = {}
        self.new_tv = {}

    def get_popmovies(self):
        html = requests.get(self.url).text
        soup = BeautifulSoup(html, "lxml")
        li = soup.find_all("li", class_="ui-slide-item")
        li = li.find_all(filter_data_title)
        self.new_movies = sorted(li, key=lambda movie: movie["data-rate"], reverse=1)
        for el in self.new_movies:
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

    def get_newmovies(self):
        para = {'type': 'movie', 'tag': u'热门', 'page_limit': '40', 'page_start': '0'}
        url = self.url + "/j/search_subjects?"
        movie = requests.get(url, params=para)
        new_movie_sub = movie.json()
        self.new_movies = new_movie_sub['subjects']
        for i in self.new_movies:
            print 'Name:' + i['title'] + '; ' + 'rate:' + i['rate']

    def get_newtv(self):
        para = {'type': 'tv', 'tag': u'热门', 'page_limit': '40', 'page_start': '0'}
        url = self.url + "/j/search_subjects?"
        tv = requests.get(url, params=para)
        new_tv_sub = tv.json()
        self.new_tv = new_tv_sub['subjects']
        for i in self.new_tv:
            print 'Name:' + i['title'] + '; ' + 'rate:' + i['rate']



def filter_data_title(tag):
    return tag.has_attr("data-title")

# url = 'https://movie.douban.com'
