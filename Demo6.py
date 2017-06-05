# -*- coding: utf-8 -*-
import yaml
from lxml import etree
import requests

res = requests.get("http://www.python-requests.org/en/master/")

Selector = etree.HTML('readxpth.html')
# print(type(Selector))
context = Selector.xpath('//*[@href="dianbolist.asp?userid=716101520010&realname=&.7336337=.4047319"]/text()')
contexts = Selector.xpath('/html/body[@id="jiaoxue"]/table/@bordercolor')

# for i in range(0, len(contexts)):
#     print(contexts[i])


# for i in contexts:
#     print(i)

x = 'readxpth.html'
y = '/html/body[@id="jiaoxue"]/table/@bordercolor'
a = lambda x, y: etree.HTML(x).xpath(y)

with open('course.yml', encoding="utf-8") as f:
    data = yaml.load(f)


# print(data)
def findxpath(html, xpathload):
    Selector = etree.HTML(html)
    return Selector.xpath(xpathload)


def response(method, url, form=None, json=None):
    s = requests.session()
    if method == 'get':
        a = s.get(url=url, params=form)
        return a
    elif method == 'post':
        a = s.post(url=url, data=form, json=json)
        return a

response()