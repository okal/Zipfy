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
