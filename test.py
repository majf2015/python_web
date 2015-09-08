# -*- coding: utf-8 -*-

class Basic:
    def __init__(self, n, d):
        self.name = n
        self.dic = d

    def get_name(self):
        pass

    def get_dic(self):
        pass

    def set_name(self, n):
        pass

    def set_dic(self, k, v):
        pass

    def delete_dic(self, k):
        pass

class Main:
    def __init__(self):
        self.count = 0
        self.object = []

    def read(self):
        with open('test.txt') as file:
            line = file.readline()[0: -1]
            if line == '' or line == 0:
                return
            else:
                self.count = int(line)
                while True:


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

