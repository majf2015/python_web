# -*- coding: utf-8 -*-
import urllib2, os, sys
from bs4 import BeautifulSoup


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
            img_links = post.find_all('img')
            new_folder = self.__creat_folder__(output_path,title)
            for img_link in img_links:
                img_url = img_link.get('src')
                img = urllib2.urlopen(img_url).read()
                with open(os.path.join(new_folder, self.__extract_file_name__(img_url)), 'wb') as picture:
                    picture.write(img)

            with open(os.path.join(new_folder, title.string), 'wb') as  blogfile:
                blogfile.write(post.get_text().encode('utf-8'))

        return

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
grab.get_all_post(r'D:\python\python_practice\web\blog')

grab.set_name("good")
grab.get_all_post(r'D:\python\python_practice\web\blog1')




