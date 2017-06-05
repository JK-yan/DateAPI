# -*- coding:utf-8 -*-
"""
@author: jackieyan
@contact: yanjiankai4618@gmail.com
@file: CreateData.py
@time: 2016/12/1 15:03
"""
import random

from DoRequest import sendRequest

c = {}
import socket

localIP = socket.gethostbyname(socket.gethostname())  # 这个得到本地ip


class CreateData:
    def __init__(self, file):
        from Utils.FileUtil import read_Yaml
        self.url = read_Yaml(file)[random.randint(1, 4)]
        self.url = read_Yaml(file)['loin']

    def count_IP(self,T):
        pv = []
        fail = []
        i = 0
        while i < T:
            req = sendRequest.SendRequest.request(self.url)
            if req.status_code == 200:
                pv.append((localIP, self.url))
            # uv.add()
            else:
                fail.append((localIP, self.url))
        return pv, fail

    def count_User(self,T):
        pv = []
        fail = []
        i = 0
        while i < T:
            sendRequest.SendRequest.request_session(self.loin)
            req = sendRequest.SendRequest.request_session(self.url)
            if req.status_code == 200:
                pv.append((localIP, self.url))
            # uv.add()
            else:
                fail.append((localIP, self.url))
        return pv, fail

    def count_IP_data(self):
        """未登录数据去重，统计PV,UV"""
        data = set(self.count_IP[0])
        for i in data:
            frequency = data.count(i)
            print(str(i) + '未登录一共请求:' + str(frequency) + '次')
            # return set(c)

    def count_User_data(self):
        """登录数据去重，统计PV,UV"""
        #通过set集合没有重复数据的特性去重
        data = set(self.count_User[0])
        for i in data:
            frequency = data.count(i)
            print(str(i) + '登录后一共请求:' + str(frequency) + '次')


if __name__ == '__main__':
