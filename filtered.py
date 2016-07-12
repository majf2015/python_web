# coding: utf-8
import re


class Filtered:
    def __init__(self):
        self.words = [u'深圳','love']
        self.strings = u'深圳人都说深圳是个好城市,好有love'

    def filtered_one(self):
        self.string_change = self.strings
        for word in self.words:
            if word in self.strings:
                self.string_change = self.string_change.replace(word, '*'* len(word))

        print 'filtered_one: ',self.string_change

    def filtered_two(self):
        self.string_change = self.strings
        for word in self.words:
            word_compile = re.compile(word)
            if word_compile.match(self.strings):
                self.string_change = word_compile.sub('*'* len(word), self.string_change)
        print 'filtered_two: ',self.string_change

word = Filtered()
word.filtered_one()
word.filtered_two()
