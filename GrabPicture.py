# -*- coding: utf-8 -*-
import urllib2, os, sys
from bs4 import BeautifulSoup

class GrabPicture:
    def __init__(self):
        self.web_url = 'http://tieba.baidu.com/p/2166231880'
        self.picture_url = []



    def get_picture_url(self):
        res = urllib2.urlopen(self.web_url,timeout=1500)
        soup = BeautifulSoup(res.read())
        for picture_url in soup.find_all('img', attrs={'class' : 'BDE_Image'}):
            self.picture_url.append(picture_url.get('src'))

        print len(self.picture_url)
        print self.picture_url
    def creat_folder(self):
        pass

    def save_picture(self):
        pass

p = GrabPicture()
p.get_picture_url()
