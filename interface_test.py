# -*- coding: utf-8 -*-

import urllib2, urllib
import time


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

    def get_type(self):
        return self.type

    def get_url(self):
         return self.url

    def get_expect_result(self):
        return self.expect

    def get_data(self):
        return self.data

    def get_run_result(self):
        return self.result

    def set_run_result(self, result):
        self.result = result

    def tostring(self):
        if self.get_run_result() == 'Successfully':
            return  '##############################\n' + self.get_name() + ' : ' + \
                self.get_url() + '\n' + self.get_run_result() + '\n'

        return  '##############################\n' + self.get_name() + ' : ' + self.get_url() + '\n' \
                + 'Error ! run result : \n' + self.get_run_result() + '\n' + 'expect result : \n' \
                + self.get_expect_result() + '\n'

class InterfaceTest:

    def __init__(self):
        self.url = []
        self.read()

    def get_test(self, object):
        response = urllib2.urlopen(object.get_url()).read().replace('\n', '')
        if response == object.get_expect_result():
            object.set_run_result('Successfully')
        else:
            object.set_run_result(response)

    def post_test(self, object):
        data = urllib.urlencode(object.get_data())
        response = urllib2.urlopen(object.get_url(), data).read().replace('\n', '')
        if  response == object.get_expect_result():
            object.set_run_result('Successfully')
        else:
            object.set_run_result(response)

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
                    if type == 'post':
                        while True:
                            e = file.readline()[0: -1]
                            if e == '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@':
                                break
                            data[e.split(' ')[0]] = e.split(' ')[1]
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
        for object in self.url:
            if object.get_type() == 'get':
                self.get_test(object)
            else:
                self.post_test(object)
        self.print_result()
        self.write()

interface = InterfaceTest()
interface.run_test()
