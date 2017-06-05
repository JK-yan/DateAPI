from wsgiref import headers

import requests
from requests import cookies

url ='http://authcenter.fulihui.org/api/auth/quickLogin?wxConfigCode='

jsons = {"loginId":"17717518626","smsCode":"0","smsCodeNamespace":"QUICKSMSCODE","latitude":"","longitude":"","machine":"","machineNo":""}
# heards ={
#     'Cookie':'JSESSIONID=EC2B84A7BD0A8E403B7871E99DAD8B9A; FULIHUI_WECHAT=gtGpr6YsOJwxZ9A1KjPQHzyhi6uN9hQLyHxITVgQFxi3dSJM6IafIGH7hWHYLGHTzFoAFQJWU+s+ixE9L2ZyXv8aYR9z0M0F0Mg0LDiu7TYmZExn5qobpF392pY/sX+gx2D9MkfiU3PukLblUKJdApZr96d/k0Nfe2v+KIt3enRNgXsVFmRZOi9L05qb5FgjuphJ9UqvyTre6vEemxV+Fu3WQzsXhH8OuSWl6tlK/5UgzkynIsHXimiNIjncsT+x; UM_distinctid=15b3c9ac74569-02694830e4b833-62451363-38400-15b3c9ac75324; FULIHUI_OAUTH_TOKEN_KEY=d11a0de158b9fc0daa593d9fe663f64ff79be91320bf97828e33609d046bafa2; CNZZDATA1260091673=1638084487-1491368801-%7C1491368801'
# }
s = requests.session()
res = s.post(url=url, json=jsons)
# res = requests.post(url=url, json=jsons)
print(res.json())
print(res.cookies)
# print(res.cookies.add_cookie_header())

prizurl = 'http://webapp.fulihui.org/v2/api/scancode/prize'
jso = {
    "showErrorToast":False
}
heade = {
    'Cookie':str(res.cookies)
}

aa = s.post(url=prizurl,  json=jso)
# aa = requests.post(url=prizurl,  json=jso, cookies=res.cookies.add_cookie_header('FULIHUI_OAUTH_TOKEN_KEY'))
print(aa.json())

choujurl = 'http://webapp.fulihui.org/v2/api/scancode/turntable '

aw = s.post(url=choujurl, json=jso)
# aw = requests.post(url=choujurl,json=jso)
print(aw.json())