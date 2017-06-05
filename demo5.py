# -*- coding: utf-8 -*-
import token

import requests
import time
read = "http://toutiao.fulihui.org/api/contentcounter/incrReadForApp"
jsonread = {
    "userId":"39024679217909760",
    "contentId":107454736487157760
}
start = "http://toutiao.fulihui.org/api/content/star"
startjson = {
    "contentId":108816273177055232
}
share = "http://toutiao.fulihui.org/api/contentcounter/incrSharedApp"
sharejson = {
    "userId":"39024679217909760",
    "contentId":107454736487157760
}
registered = "http://openapi.fulihui.org/rest/userAuthService/registered"
registeredJson = {
    "access_token": "6b847aac6acf9fa4dad06bc6138b13a6",
    "datas": {
        "request": {
            "loginId": "18625172685"
        }
    }
}
quickLogin = "http://openapi.fulihui.org/rest/userAuthService/quickLogin"
quickLoginJson = {
    "access_token": "6b847aac6acf9fa4dad06bc6138b13a6",
    "datas": {
        "request": {
            "vcode": "0",
            "vcodeNamespace": "MOBILE_QUICK_LOGIN_VCODE",
            "registerType": "MOBILE_QUICK",
            "loginId": "18625172683",
            "registerSource": "INFORMATION_APP",
            "mechineNo": "Aic85HeGddMU3I5AC9pMaaZbBwUJu0hmYSl4-aI3vpdA"
        }
    }
}
#
querySingle = "http://openapi.fulihui.org/rest/userService/querySingle"

def function():
    readres = requests.post(url=read, json=jsonread)
    shareres = requests.post(url=start, json=startjson)
    print(readres.status_code)
    print(".......")
    print(shareres.status_code)
def star():
    # s = requests.Session()
    headers = {
        'Connection': 'Keep-Alive',
    }
    registeredres = requests.post(url=registered, json=registeredJson, headers=headers)
    print(registeredres.status_code)
    print(registeredres.cookies)
    print(registeredres.headers)
    print(registeredres.text)
    quickLoginres = requests.post(url=quickLogin, json=quickLoginJson, headers=headers)
    print(quickLoginres.status_code)
    print(quickLoginres.cookies)
    print(quickLoginres.headers)
    print('....................')
    print(quickLoginres.json())
    print(quickLoginres.json()['value']['token'])
    FULIHUI_OAUTH_TOKEN_KEY=quickLoginres.json()['value']['token']
    JSESSIONID=quickLoginres.json()['value']['userId']
    head = {
        'Connection': 'Keep-Alive',
        'Cookie': 'FULIHUI_OAUTH_TOKEN_KEY=%s;JSESSIONID=%s'% (FULIHUI_OAUTH_TOKEN_KEY, JSESSIONID),
        # 'Cookie':'JSESSIONID=%s'%(JSESSIONID)
    }
    querySingleJosn = {
        "access_token": "6b847aac6acf9fa4dad06bc6138b13a6",
        "datas": {
            "request": {
                "userId": JSESSIONID
            }
        }
    }
    querySingleres = requests.post(url=querySingle, json=querySingleJosn, headers=head)
    print(querySingleres.status_code)
    print(querySingleres.cookies)
    print(querySingleres.headers)
    print(querySingleres.json())
    print(querySingleres)
    startres = requests.post(url=start, json=startjson, headers=head)
    print(startres.status_code)
    print(startres.cookies)
    print(startres.headers)

    print('............................')

    # print(loginres3.text)
if __name__ == '__main__':
    star()

    # count=100
    # print(count)
    # while count>=0:
    #     function()
    #     count=count-1
    #     time.sleep(1)