# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr

class Post_object:
    def __init__(self, title, url, summary):
        self.title = title
        self.url = url
        self.summary = summary

    def get_title(self):
        return self.title

    def get_url(self):
        return self.url

    def get_summary(self):
        return self.summary

class Post:
    def __init__(self, url, n):
        self.url = url
        self.number = n
        self.urls = []
        self.open_index()

    def open_index(self):
        assign  = '/pick/'
        self.url += assign
        self.open_assign()

    def open_assign(self):
        open_urls =  BeautifulSoup(urllib2.urlopen(self.url,timeout=1500).read(), "html.parser")
        a = open_urls.find_all('a', attrs= {'class': 'titlelnk'})
        p = open_urls.find_all('p', attrs= {'class': 'post_item_summary'})
        for i in range(len(a)):
            if len(self.urls) < self.number:
                self.urls.append(Post_object(a[i].string, a[i].get('href'), p[i].get_text()))
            else:
                break
        if len(self.urls) < self.number:
            pass

        print self.urls
        self.send(self.urls)

    def send(self,content):
        sender = 'happier<1102103123@qq.com>'
        #receiver =[ 'happier<1102103123@qq.com>']
        receiver =[ '1102103123@qq.com', 'majinfeng@shidou.com', '461148972@qq.com']
        subject = '博客园精品博文，哈哈！'
        smtpserver = 'smtp.qq.com'
        username = '1102103123@qq.com'
        password = '123456'
        content_str = ''
        for k in content:
            content_str += k.get_title() + k.get_url() + '\n' + k.get_summary()  + '\n'
        msg = MIMEText(content_str, 'plain','utf-8')
        msg['Subject'] = Header(subject, 'utf-8')
        msg['From'] = formataddr((Header('happier', 'utf-8').encode(), '1102103123@qq.com'))

        smtp = smtplib.SMTP(smtpserver)
        #smtp.set_debuglevel(1)
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()



url = 'http://www.cnblogs.com'
n = 20
get = Post(url, n)

