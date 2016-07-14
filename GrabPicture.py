# -*- coding: utf-8 -*-
import urllib2, os, sys
from bs4 import BeautifulSoup


class GrabPicture:
    def __init__(self):
        self.web_url = 'http://tieba.baidu.com/p/2166231880'
        self.picture_url = []
        self.new_folder ='E:\GrabPicture'

    def get_picture(self):
        self.new_folder = self.creat_folder()
        self.get_picture_url()
        self.save_picture()

    def get_picture_url(self):
        res = urllib2.urlopen(self.web_url,timeout=1500)
        soup = BeautifulSoup(res.read())
        for picture_url in soup.find_all('img', attrs={'class' : 'BDE_Image'}):
            self.picture_url.append(picture_url.get('src'))

        print len(self.picture_url)
        print self.picture_url

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
