import requests
import yaml

loginjson = {
    "phone": "17717518326",
    "vcode": "0",
    "latitude": "",
    "longitude": "",
    "registerSource": "GIFTPACKAGE_MOBILE_QUICK_LOGIN"
}
f = open(file='zhenanqr.yml',mode='r',encoding='utf-8')
qrul = yaml.load(f.read())
f.close()
signDataUrl = 'http://webapp.fulihui.org/v2/api/commons/wechat/signData'
signDatajson = {"url": "http://webapp.fulihui.org/giftPackage/home/southTea/southTeaV1"}
getMobileUrl = 'http://webapp.fulihui.org/v2/api/activity/giftpackage/getMobile'
getMobilejson = {}
queryChanceUrl = 'http://webapp.fulihui.org/v2/api/activity/giftpackage/queryChance'
queryChancejson = {}
openZheNanUrl = 'http://webapp.fulihui.org/v2/api/activity/giftpackage/openZheNan'
quickLoginUrl = 'http://webapp.fulihui.org/v2/api/commons/auth/quickLogin'
head = {'Cookie':'UM_distinctid=15bf0589dc4b5-06432e6ca9c623-61340e5e-49a10-15bf0589dc8b7; FULIHUI_WECHAT=gtGpr6YsOJwxZ9A1KjPQH4dyT8Gwl+oUDvd5UOwNuRJqruIFD9C4HKXlHnv4laVa9CWXUatCZWKfW3XP9kcF7UwIfcQwfXONg7mq4hZ8RvFnmH5ii5dYRwVGCkvC698YFHeKW5x79CwI0S3b4Ib+jMAqf1m9DAPJGmlFwkbgBGlecssJPmlxOjVOanFUAEdmKCDIyUOJr8zsmmWEwOTzZXVacEVVEkBjToWevpAJDklq/ss6MOFqtQWDA9FymKvq'}
s = requests.session()
loginres = s.post(url="http://authcenter.fulihui.org/api/auth/quickLogin?wxConfigCode=FULIHUI_WECHAT",headers=head,json={
    "loginId": "17717518326",
    "smsCode": "0",
    "smsCodeNamespace": "QUICKSMSCODE",
    "latitude": "",
    "longitude": "",
    "machine": "",
    "machineNo": ""
})
print(loginres.json())
head = {"Cookie": loginres.cookies.get(name='FULIHUI_OAUTH_TOKEN_KEY')}
for i in qrul:
    # qrrs = s.get(url=i)
    # print(qrrs.status_code)

    res = s.post(url=signDataUrl,json=signDatajson)
    print(res.json())
    login = s.post(url=getMobileUrl, json=getMobilejson)
    print(login.json())
    queryChanceRes = s.post(url=queryChanceUrl, json=queryChancejson)
    print(queryChanceRes.json())

    # quickLoginRes = s.post(url=quickLoginUrl, json=loginjson)
    # print(quickLoginRes.json())
    #
    # luckres = s.post(url=openZheNanUrl, json={})
    # print(luckres.json())
    # if luckres.status_code==200:
    #     # print(luckres.json()['success'])
    #     print(luckres.json())
    # elif luckres.status_code==401:
    #     print('此二维码已被使用')
    # else:
    #     print(luckres.json())
# print(loginres.json())
# print(qrul)

