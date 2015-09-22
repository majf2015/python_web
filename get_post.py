# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.header import Header


class Post:
    def __init__(self, url, n):
        self.url = url
        self.number = n
        self.urls = {}
        self.open_index()

    def open_index(self):
        op = urllib2.urlopen(self.url,timeout=1500)
        open_url =  BeautifulSoup(op.read())
        assign  = '/pick/'
        self.url += assign
        self.open_assign()
        print self.urls
        #self.send()

    def open_assign(self):
        open_urls =  BeautifulSoup(urllib2.urlopen(self.url,timeout=1500).read())
        a = open_urls.find_all('a', attrs= {'class': 'titlelnk'})
        for url in a:
            while len(self.urls) < self.number:
                self.urls[url.string.encode('utf-8')] = url.get('href')
            break
        s = 'python email test,python email test'

        self.send(s)

    def send(self, c):
        sender = '1102103123@qq.com'
        receiver = '1102103123@qq.com'
        subject = 'python email test'
        smtpserver = 'smtp.qq.com'
        username = '1102103123@qq.com'
        password = '123456'
        #msg = MIMEText('你好','text','utf-8')
        msg = MIMEText(c,'text','utf-8')

        msg['Subject'] = Header(subject, 'utf-8')

        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()



url = 'http://www.cnblogs.com'
n = 1

get = Post(url, n)

