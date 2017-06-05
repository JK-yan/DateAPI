# -*- coding:utf-8 -*-
"""
@author: jackieyan
@contact: yanjiankai4618@gmail.com
@file: FileUtil.py
@time: 2016/11/29 17:21
"""
import json
import os
import yaml


def read_Json(file_name):

    """读取json文件"""
    json_object = json.loads(json.dumps(read_file(file_name)))
    # with open(os.path.abspath('../Resources/') + '/' + file, mode='r', encoding='utf-8') as f:
    #     json_object = json.loads(json.dumps(f.readlines()))
    return json_object


def read_Yaml(file):
    """读取yaml文件"""
    # f = open(os.path.abspath('../Resources/') + '/' + file, 'r', encoding='utf-8')
    with open(os.path.abspath('../Resources/') + '/' + file, mode='r', encoding='utf-8') as f:
        yaml_object = yaml.loads(f.readline())

    return yaml_object


def read_file(file):
    """打开文件"""
    with open(os.path.abspath('../Resources/') + '/' + file, mode='r', encoding='utf-8') as f:
        read_file = f.readlines()

    return read_file


if __name__ == '__main__':
    # print(read_file('aaab.json').read())
    # read_file('aaab.json')
    print(read_Json('aaab.json'))

    # print(read_Yaml('yam.yaml'))
    # while True:
    #     a = read_file('aaab.json').read()
    #     if not a:
    #         print(a)
    # print(json.loads((read_file('aaab.json')[1]))["mime"])
    # print(read_file('aaab.json'))
    # for i in read_file('aaab.json'):
    #     print(json.loads(i)['mime'])
    #     print("-------------------------------")
    for i in read_Json('aaab.json'):
        print(json.loads(i))
        print("-------------------------------")


