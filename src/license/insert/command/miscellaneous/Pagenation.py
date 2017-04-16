#!python3
#encoding
import requests
import furl
import time
class Pagenation:
    def __init__(self):
        pass
    def get_next(self, r):
        return self.__get_page(r, 'next')
    def get_prev(self, r):
        return self.__get_page(r, 'prev')
    def get_first(self, r):
        return self.__get_page(r, 'first')
    def get_last(self, r):
        return self.__get_page(r, 'last')
    def __get_page(self, r, rel='next'):
        if None is r:
            return None
        print(r.links)
        if rel in r.links.keys():
            f = furl(r.links[rel]['url'])
            print(f.query['page'])
            return f.query['page']
        else:
            return None
