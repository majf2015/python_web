# -*- coding: utf-8 -*-
import re


class Basic:
    def __init__(self, n, d):
        self.name = n
        self.dic = d

    def get_name(self):
        return self.name

    def get_dic(self):
        return self.dic

    def set_name(self, n):
        return self.name

    def set_dic(self, k, v):
        pass

    def delete_dic(self, k):
        pass

class Main:
    def __init__(self):
        self.count = 0
        self.object = []
        self.read()

    def read(self):
        with open('test.txt') as file:
            line = file.readline()[0 : -1]
            if line == '' or line == 0:
                return
            else:
                self.count = int(line)
                for i in range(self.count):
                    name = file.readline()[0 : -1]
                    while name == '':
                        name = file.readline()[0 : -1]
                    data = {}
                    name = Basic(name, data)
                    self.object.append(name)

                for i in range(self.count):
                    begin = file.readline()[0 : -1]
                    while begin == '':
                        begin = file.readline()[0 : -1]

                    #匹配begin
                    while re.match('\sbegin' ,begin) == None:
                        begin = file.readline()[0 : -1]

                    #begin
                    name = re.compile('\s+').split(begin)[0]
                    print name
                    for i in self.object:
                        if i.get_name == name:
                            line = file.readline()[0 : -1]
                            while re.match('\send', begin) == None:
                                key = re.compile('\s*=\s*').split(line)
                                i.dic[key[0]] = key[1]
                            break
        print self.count
        print self.object
        for i in self.object:
            print i.get_name()
            print i.get_dic()

    def write(self):
        pass

    def query_all_area(self):
        pass

    def query_one_area(self):
        pass

    def add_area(self):
        pass

    def add_key(self):
        pass

    def remove_area(self):
        pass

    def remove_key(self):
        pass

    def modify_area(self):
        pass

    def modify_key(self):
        pass

APP = Main()
