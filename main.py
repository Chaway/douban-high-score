#!/usr/local/anaconda/bin/python
# -*- coding: utf-8 -*-
from Douban import Douban

douban = Douban("https://movie.douban.com")
douban.get_newmovies()
douban.get_newtv()
douban.get_newmovies()
