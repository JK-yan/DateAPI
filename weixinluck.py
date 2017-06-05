# -*- coding: UTF-8 -*-
import json

import requests


def re():
    url = 'http://webapp.fulihui.org/v2/api/scancode/turntable '
    APPurl = 'http://toutiao.fulihui.org/api/informationActivity/turntable'
    
    jsons = {
        "accessToken":"0d541a75dfc776b76db8e3fb5063d0bb","sigal":"e3de3749ce049574b021da73278052443462b167","exchangeType":"2"
    }
    heard = {
        'Cookie': 'JSESSIONID=8376BE8B49B6D78DB3BA2D9AB606FF22; FULIHUI_OAUTH_TOKEN_KEY=63e4f25aed416a99dd93d2a4c936a2167c58e85d0adae96cd35874a8369f7cfa'
    }
    res = requests.post(url=APPurl, json=jsons, headers=heard)
    print(res.json())
    return res.json()


# print(res.status_code)
# print(res.json())
# print(res.text)
# print(res.json()['info']['prizeName'])
a = '1111'
aa = 0
b = '现金红包，100'
bb = 0
c = '新用户专享，1元红包'
cc =0
d = '流量红包，新100M'
dd = 0
e = '现金红包，10元'
ee = 0
f = '流量红包，5M'
ff = 0
g = '手机'
gg = 0
h = '谢谢参与'
hh = 0
error = ""
er = 0
count = 0
count1v = ''
count2v = ''
count3v = ''
if __name__ == '__main__':
    # print(re())
    while count <= 10:
        w = re()['info']['prizeName']
        print(w)
        if w == a:
            aa += 1
        elif w == b:
            bb += 1
            count3v = count3v + ':' + str(count)
        elif w == c:
            cc += 1
        elif w == d:
            dd += 1
            count2v = count2v + ':' + str(count)
        elif w == e:
            ee += 1
        elif w == f:
            ff += 1
        elif w == g:
            gg += 1
            count1v = count1v+':'+str(count)
        elif w == h:
            hh += 1
        else:
            er += 1
        count += 1
print(a+":"+str(aa))
print(b+":"+str(bb))
print(c+":"+str(cc))
print(d+":"+str(dd))
print(e+":"+str(ee))
print(f+":"+str(ff))
print(g+":"+str(gg))
print(h+":"+str(hh))
print("error:"+str(er))
print('手机'+count1v)
print('流量红包，新100M'+count2v)
print('现金红包，100'+count3v)