# -*- coding: utf-8 -*-
import re
from functools import wraps
import time


class Basic:
    def __init__(self, n):
        self.name = n
        self.dic = {}

    def get_name(self):
        return self.name

    def get_dic(self):
        return self.dic

    def set_name(self, n):
        self.name = n

    def set_dic(self, k, v):
        self.dic[k] = v

    def delete_dic(self, k):
        pass

class Main:
    def __init__(self, hellow):
        self.count = 0
        self.object = []
        self.read()
        self.print_file()
        self.hellow = hellow

    def __call__(self, *args, **kwargs):
        self.hellow()
        print "hellow my decorator"

    def read(self):
        with open('test.txt') as file:
            line = file.readline()[0 : -1]
            if line == '' or line == 0:
                return
            else:
                self.count = int(line)
                self.read_area(file)
                for i in range(self.count):
                    begin = file.readline()[0 : -1]
                    while begin == '':
                        begin = file.readline()[0 : -1]

                    #匹配begin
                    while re.search('\s*begin', begin) == None:
                        begin = file.readline()[0 : -1]

                    #begin
                    name = re.compile('\s+').split(begin)[0]
                    try:
                        self.read_area_key(file, name)
                    except:
                        print "area end lock "
                        break

    def read_area(self,file):
        for i in range(self.count):
            name = file.readline()[0 : -1]
            while name == '':
                name = file.readline()[0 : -1]
            name = Basic(name)
            self.object.append(name)

    def read_area_key(self, file, name):
        for i in self.object:
            if i.get_name() == name:
                line = file.readline()[0 : -1]
                while re.search('\s*end', line) == None:
                    while line == '':
                        line = file.readline()[0 : -1]
                    if re.search('\s*begin', line) != None:
                        raise 001
                    key = re.compile('\s*=\s*').split(line)
                    i.set_dic(key[0], self.value_type(key[1]))
                    line = file.readline()[0 : -1]
                break

    def print_file(self):
        print self.count
        for i in self.object:
            print i.get_name()
            print i.get_dic()

    def logs(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            times = time.time()
            #time.sleep(1)
            result = func(*args, **kwargs)
            timee = time.time()
            print "function      = {0}".format(func.__name__)
            print "    arguments = {0} {1}".format(args, kwargs)
            print "    return    = {0}".format(result)
            print "    time      = %.6f sec" % (timee - times)
            return result
        return wrapper

    @logs
    def value_type(self, value):
        try:
            type_value = eval(value)
            return type_value
        except:
            return value

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

@ Main
def hellow():
    print "Decorator"


#APP = Main()
hellow()