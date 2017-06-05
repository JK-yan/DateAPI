# -*- coding:utf-8 -*-
"""
@author: jackieyan
@contact: yanjiankai4618@gmail.com
@file: Demo1.py
@time: 2016/12/1 15:56
"""
import re, requests


class Get_public_ip:
    def getip(self):
        try:
            myip = self.visit("http://www.baidu.com/")
        except:
            try:
                myip = self.visit("http://www.baidu.com/")
            except:
                myip = "So sorry!!!"
        return myip

    def visit(self, url):
        opener = requests.get(url)
        if url == opener.geturl():
            str = opener.read()
        return re.search('d+.d+.d+.d+', str).group(0)


if __name__ == "__main__":
    getmyip = Get_public_ip()
    print(getmyip.getip())
