#!/usr/local/anaconda/bin/python
# -*- coding: utf-8 -*-
from MovieTV import Douban
from Email import EmailInfo

douban = Douban("https://movie.douban.com")
douban.get_popmovies()
douban.get_newtv()
douban.get_newmovies()

email = EmailInfo('from_addr@###.com', 'to_addr@###.com', 'smtp.###.com', '###')
email.plaintext = 'Hello word' #email content
email.send()

