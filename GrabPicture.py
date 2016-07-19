# -*- coding: utf-8 -*-
import urllib2, os, sys
from bs4 import BeautifulSoup


class GrabPicture:
    def __init__(self):
        self.web_url = [ 'http://tieba.baidu.com/p/2166231880','http://tieba.baidu.com/p/2125228667#!/l/p1']
        self.picture_url = set()
        self.new_folder ='E:\GrabPicture\img3'

    def get_picture(self):
        self.new_folder = self.creat_folder()
        for url in self.web_url:
            self.get_picture_url(url)
        self.save_picture()

    def get_picture_url(self, url):
        res = urllib2.urlopen(url,timeout=1500)
        soup = BeautifulSoup(res.read())
        i = 1
        for picture_url in soup.find_all('img'):#, attrs={'class' : 'BDE_Image'}):
            if i>200 :
                break
            self.picture_url.add(picture_url.get('src'))
            self.get_web_url(soup)
            i += 1

    def get_web_url(self, soup):
        for web_url in soup.find_all('link'):
            url =  web_url.get('href') #, attrs={'class' : 'BDE_Image'}):
            if url.startswith('http:') and url not in self.web_url:
                self.web_url.append(url)


    def creat_folder(self):
        if not os.path.isdir(self.new_folder):
            os.mkdir(self.new_folder)
        return self.new_folder

    def save_picture(self):
        i = 1
        print self.new_folder
        for picture in self.picture_url:
            picture_str = urllib2.urlopen(picture).read()
            with open(os.path.join(self.new_folder, 'pic%s' % i + '.jpg'), 'wb') as  picture_file:
                picture_file.write(picture_str)
            i += 1


p = GrabPicture()
p.get_picture()
