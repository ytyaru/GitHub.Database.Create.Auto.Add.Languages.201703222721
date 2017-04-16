import urllib.request
import os
import yaml
import requests
import pprint
class LanguageSource(object):
    def __init__(self):
        pass

    """
    def Get(self, is_show=True):
        url_str = "https://raw.githubusercontent.com/github/linguist/master/lib/linguist/languages.yml"
        file_name = os.path.basename(url_str)
        if is_show:
            print(url_str)
            print(file_name)
        if not(os.path.isfile(file_name)):
            r = requests.get(url_str)
            with open(os.path.basename(file_name), mode='wt', encoding='utf-8') as f:
                f.write(r.text)
                if is_show:
                    print(r.text)
        with open(os.path.basename(file_name), mode='r', encoding='utf-8') as f:
            y = yaml.load(f)
            if is_show:
                pprint.pprint(y)
            return y
    """
    
    def Get(self, is_show=True):
#        path_this_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "language/insert")
        path_this_dir = os.path.abspath(os.path.dirname(__file__))
        url_str = "https://raw.githubusercontent.com/github/linguist/master/lib/linguist/languages.yml"
        file_name = os.path.basename(url_str)
        file_path = os.path.join(path_this_dir, file_name)
        if is_show:
            print(url_str)
            print(file_path)
        if not(os.path.isfile(file_path)):
            r = requests.get(url_str)
            with open(file_path, mode='wt', encoding='utf-8') as f:
                f.write(r.text)
                if is_show:
                    print(r.text)
        with open(file_path, mode='r', encoding='utf-8') as f:
            y = yaml.load(f)
            if is_show:
                pprint.pprint(y)
            return y
