# -*- coding:utf-8 -*-
"""
@author: jackieyan
@contact: yanjiankai4618@gmail.com
@file: sendRequest.py
@time: 2016/11/29 17:57
"""
import requests


class SendRequest:
    def __init__(self, filename):
        """初始化请求参数"""
        # from Utils import FileUtil
        # self.method = FileUtil.read_Json(filename)['Method']
        # self.host = FileUtil.read_Json(filename)['Host']
        # self.url = FileUtil.read_Json(filename)['RUL']
        self.method = ''
        self.host = ''
        self.url = ''

    def request(self, **kwargs):
        """选择请求方式"""
        if self.method == 'get':
            try:
                response = requests.get(self.url, params=None, timeout=5, **kwargs)
            except Exception as e:
                print(e)
            finally:
                response.close()
                # return response
        elif self.method == 'post':
            try:
                response = requests.post(self.url, data=None, json=None, timeout=5, **kwargs)
            except Exception as e:
                print(e)
            finally:
                response.close()
                # return response
        return response

    def request_session(self, **kwargs):
        """
        会话对象让你能够跨请求保持某些参数。
        它也会在同一个 Session 实例发出的所有请求之间保持 cookie，
        期间使用 urllib3 的 connection pooling 功能。
        所以如果你向同一主机发送多个请求，底层的 TCP 连接将会被重用，
        从而带来显著的性能提升
         """
        req = requests.Session()
        if self.method == 'get':
            try:
                response = req.get(self.url, params=None, timeout=5, **kwargs)
            except Exception as e:
                print(e)
            finally:
                response.close()
                # return response
        elif self.method == 'post':
            try:
                response = req.post(self.url, data=None, json=None, timeout=5, **kwargs)
            except Exception as e:
                print(e)
            finally:
                response.close()
                # return response
        return response