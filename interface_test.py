# -*- coding: utf-8 -*-
import urllib2

class Interface:
    def __init__(self, n, t, u, e, r = u'未测试'):
        self.name = n
        self.type = t
        self.url = u
        self.expect = e
        self.result = r

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

        return  '##############################\n' + self.get_name() + ' : ' + \
                self.get_url() + '\n' + self.get_run_result() + '\n' + self.get_expect_result()

class InterfaceTest:

    def __init__(self):
        self.url = []
        self.read()

    def get_test(self):
        for i in self.url:
            response = urllib2.urlopen(i.get_url()).read()

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
        with open('test_data.txt', 'rb') as file:
            while True:
                line = file.readline()[0: -1]
                if line == '##############################':
                    name = file.readline()[0: -1]
                    type = file.readline()[0: -1]
                    url = file.readline()[0: -1]
                    expect = ''
                    while True:
                        e = file.readline()
                        if e == '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n':
                            break
                        expect += e
                    self.url.append(Interface(name, type, url, expect))
                if line == '':
                    break

    def write(self):
        string = ''
        for i in self.url:
            string += i.tostring()
        with open('run_result.txt', 'wb') as file:
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
