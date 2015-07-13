# -*- coding: utf-8 -*-
import urllib2, os, sys
from bs4 import BeautifulSoup
import bs4


class GrabCnblogPost():
    def __init__(self, name):
        self.url = 'http://www.cnblogs.com/' + name
        self.url_list = []

    def __creat_folder__(self, output_path, title):
        new_folder = os.path.join(output_path, title)
        if not os.path.isdir(new_folder):
            os.mkdir(new_folder)
        return new_folder

    def __get_url__(self, url):
        resporn = urllib2.urlopen(url, timeout=1500)
        soup = BeautifulSoup(resporn.read())
        for a in soup.find_all('a', attrs={'class' : 'postTitle2'}):
            self.url_list.append(a.get('href'))
        next_page = soup.find(id = 'nav_next_page')
        if next_page:
            next_page = next_page.find('a').get('href')
            self.__get_url__(next_page)
        else:
            pager = soup.find('div', attrs= {'class' : 'pager'})
            if not pager:
                return
            pages = pager.find_all('a')
            for page in pages:
                if page.get_text() == u'下一页':
                    next_page = page.get('href')
                    break
            if next_page:
                self.__get_url__(next_page)

    def __get_blog__(self, output_path, url_list):
        for url in url_list:
            resporn = urllib2.urlopen(url, timeout=1500)
            soup = BeautifulSoup(resporn.read())
            title = soup.find(id='cb_post_title_url').string
            post = soup.find(id='cnblogs_post_body')
            if not post:
                return

            post_string = self.__get_post__(post)
            new_folder = self.__creat_folder__(output_path,title)
            with open(os.path.join(new_folder, title.string + '.txt'), 'wb') as  blogfile:
                blogfile.write(post_string.encode('utf-8'))
        return

    def __get_post__(self, post_html):
        str = ""
        for post_child in post_html.children:
            if post_child.string != None and type(post_child) == bs4.element.NavigableString:
                if post_child.string != '\n':
                    str += post_child.string
                continue

            elif post_child.string != None and type(post_child) == bs4.element.Tag:
                if post_child.name == 'a':
                    str += post_child.string
                    str += '[' + post_child['href'] +']'
                elif post_child.name == 'td':
                    str += post_child.string + '||'
                else:
                    str += post_child.string

            elif post_child.string == None:
                try:
                    str += self.__get_post__(post_child)
                    if post_child.name == 'img':
                        str += '['+ post_child['src'] + ']\n '
                except:
                    print "error"

            if post_child.name == 'tr'or  post_child.name == 'br' or post_child.name == 'p' \
                    or post_child.name == 'h1' or post_child.name == 'h2' or post_child.name == 'h3'\
                    or post_child.name == 'h4':
                str += '\n'


        return  str

    def __extract_file_name__(self, link):
        for s in range(1, len(link)+ 1):
            if link[-s] == '/':
                return link[-s + 1:]

    def set_name(self, name):
        self.url = 'http://www.cnblogs.com/' + name
        self.url_list = []

    def get_all_post(self, output_path):
        self.__get_url__(self.url)
        self.__get_blog__(output_path, self.url_list)

grab = GrabCnblogPost('catch')
grab.get_all_post(r'D:\blog')








