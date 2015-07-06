# -*- coding: utf-8 -*-
import urllib2, os, sys
from bs4 import BeautifulSoup
class GrabCnblogPost():
    def __init__(self, name):
        self.url = 'http://www.cnblogs.com/catch/p/'+ name

    def __open_into_soup__(self):
        resporn = urllib2.urlopen(self.url, timeout=1500)
        soup = BeautifulSoup(resporn.read())
        post_html = soup.find(id='cnblogs_post_body')
        return post_html

    def __get_string__(self, post_html):
        for post_child in post_html.children:
            if post_child.string != None:
                print post_child.string
            else:
                for post_child_child in post_child.strings:
                    return self.__get_string__(post_child_child)






print '33333333333333333333333**********************************************'



