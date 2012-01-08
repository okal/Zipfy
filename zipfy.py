import re

from requests import get
from BeautifulSoup import BeautifulSoup
from HTMLParser import HTMLParser

class Corpus:
    def __init__(self, words):
        self.words = words
        self.word_list = self.words.split()
        self.word_set = set(self.word_list)
        self.freq_list = []

        for word in self.word_set:
            self.freq_list.append((word, self.word_list.count(word)))

        self.freq_list = sorted(self.freq_list, key=lambda tup: tup[1])
        self.freq_list.reverse()
 
class WebCorpus(Corpus):
    def __init__(self, url):
        self.url = url
        site = get(url)
        self.is_html = False
        self.is_plaintext = False

        if 'text/html' in site.headers['content-type']:
            self.is_html = True
            h = HTMLParser()
            page = BeautifulSoup(site.content, convertEntities=True)
            body = page.body
            text = ' '.join(body.findAll(text=True)).strip()
            text = ' '.join(h.unescape(text).split()).lower()
            self.words = re.sub('[^A-Za-z\'\s\-]+', '', text).__str__()

        elif 'text/plain' in site.headers['content-type']:
            self.is_plaintext = True
            text = site.content.strip()
            text = ' '.join(text.split()).lower()
            self.words = re.sub('[^A-Za-z\'\s\-]+', '', text).__str__()

        else:
            raise Exception('Unsupported data type')

        Corpus.__init__(self, self.words)
