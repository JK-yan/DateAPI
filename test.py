# -*- coding: UTF-8 -*-
import json
import random
from filecmp import cmp

datetime = '2016-12-%s' % random.randint(20, 22) + \
           ' %s' % random.randint(0, 23) + ':%s' % random.randint(0, 59) + \
           ':%s' % random.randint(0, 59)
businessid = "%s" % random.randrange(100, 1000, 1)
userid = 's'
deviceid = 'q'
openid = 'e'
biztype = 'r'
platform = 't'
modulepage = 'y'
sourcecode = "wqeq"
productcode = "productcode"

tracePoint = '{"datetime": "%s","businessid": "%s","userid": "%s","deviceid": "%s","openid": "%s","biztype": "%s","platform": "%s","modulepage": "%s","sourcecode": "%s","productcode": "YOUKANTOU"}' % \
             (datetime, businessid, userid, deviceid, openid, biztype, platform, modulepage, sourcecode)
tracePointLog = {
    'tracePointLog': tracePoint
}
# print(tracePointLog)
import yaml
f = open('course.json',mode='w',encoding='utf-8')
# b = yaml.load(f)
# f.close()
# c = {}
# c = b
x = json.dumps({'d': {'f': ['g', 'h']}, 'a': {'b': ['c']}}, indent=4)
print(json.dumps({'d': {'f': ['g', 'h']}, 'a': {'b': ['c']}}))
# print(c['d'])
# f = open('course.yml',mode='r',encoding='utf-8')
# b = yaml.load(f)
# print(b)
#
# a = (1,2,3)
# b = (1,2,3,4)
# print(cmp(a,b))
# f = open('course.json', mode='r', encoding='utf-8')
f.write(x)
f = open('course.json', mode='r', encoding='utf-8')
a = json.load(f,encoding='utf-8')
print(a['a'])