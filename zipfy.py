import re

from requests import get
from BeautifulSoup import BeautifulSoup
from HTMLParser import HTMLParser

class Corpus:
    def __init__(self, url):
        h = HTMLParser()
        self.page = BeautifulSoup(get(url).content, convertEntities=True)
        self.body = self.page.body
        text = ' '.join(self.body.findAll(text=True)).strip()
        self.text = ' '.join(h.unescape(text).split()).lower()
        self.words = re.sub('[^A-Za-z\'\s\-]+','', self.text).__str__()
        self.word_list = self.words.split()
        self.word_set = set(self.word_list)
        self.freq_list = []
        for word in self.word_set:
            self.freq_list.append((word, self.word_list.count(word)))
        self.freq_list = sorted(self.freq_list, key=lambda tup: tup[1])
        self.freq_list.reverse()
