# -*- coding: utf-8 -*-

import urllib2
import time
from bs4 import BeautifulSoup



class InterfaceAttribute:
    def __init__(self, n, t, u, e, d):
        self.name = n
        self.type = t
        self.url = u
        self.expect = e
        self.data = d
        self.result = u'未测试'

    def get_name(self):
        return self.name

    def get_url(self):
         return self.url

    def get_expect_result(self):
        return self.expect

    def get_run_result(self):
        return self.result

    def get_type(self):
        return self.type

    def set_run_result(self, result):
        self.result = result

    def tostring(self):
        if self.get_run_result() == 'Successfully':
            return  '##############################\n' + self.get_name() + ' : ' + \
                self.get_url() + '\n' + self.get_run_result() + '\n'

        return  '##############################\n' + self.get_name() + ' : ' + self.get_url() + '\n' \
                + 'Error ! run result : \n' + self.get_run_result() + '\n' + 'expect result : \n' \
                + self.get_expect_result()

class InterfaceTest:

    def __init__(self):
        self.url = []
        self.read()

    def get_test(self):
        for i in self.url:
            response = BeautifulSoup(urllib2.urlopen(i.get_url()).read(), "html.parser").find('body')\
                .get_text().replace('\n', '').encode('utf-8')
            if response == i.get_expect_result():
                i.set_run_result('Successfully')
            else:
                i.set_run_result(response)

    def post_test(self):
        pass

    def print_result(self):
        for i in self.url:
            print i.tostring()

    def read(self):
        with open('test_data.txt') as file:
            while True:
                line = file.readline()[0: -1]
                if line == '##############################':
                    name = file.readline()[0: -1]
                    type = file.readline()[0: -1]
                    url = file.readline()[0: -1]
                    expect = ''
                    while True:
                        e = file.readline()[0: -1]
                        if e == '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@':
                            break
                        expect += e
                    data = {}
                    #POST 参数
                    self.url.append(InterfaceAttribute(name, type, url, expect, data))
                if line == '':
                    break

    def write(self):
        string = ''
        ISOTIMEFORMAT='%Y-%m-%d %X'
        string += '\n\n' + time.strftime( ISOTIMEFORMAT, time.localtime(time.time())) + '\n\n'
        for i in self.url:
            string += i.tostring()
        with open('run_result.txt', 'ab') as file:
            file.write(string)

    def run_test(self):
        for i in self.url:
            if i.get_type() == 'get':
                self.get_test()
            else:
                self.post_test()
        self.print_result()
        self.write()

interface = InterfaceTest()
interface.run_test()
