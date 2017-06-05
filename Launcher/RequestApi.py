# -*- coding:utf-8 -*-
"""
@author: jackieyan
@contact: yanjiankai4618@gmail.com
@file: RequestApi.py
@time: 2016/11/30 16:42
"""
import random
import threading

from DoRequest import sendRequest
from Utils import FileUtil


def requrl(filename):
    sendRequest.SendRequest(filename).request()

threads = []
t1 = threading.Thread(target=requrl, args=u'爱情买卖')
threads.append(t1)
t2 = threading.Thread(target=move,args=(u'阿凡达',))
threads.append(t2)


if __name__ == '__main__':
    i = 0
    while i < 100:
        filename = FileUtil.read_Yaml("API.yaml")[random.randint(1, 4)]
        print(filename)
        print(i)
        i += 1 