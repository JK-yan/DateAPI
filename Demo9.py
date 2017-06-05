import random

import requests
import time

orgurl = 'http://fulihui.udesk.cn/'
sign_inurl = 'http://fulihui.udesk.cn/users/sign_in'
sign_indate = {
    'utf8': '✓',
    'authenticity_token': 'j16K918V/5eJSZxXroyFmfyihS6ChtGekEHDl9s7HQQ=',
    'user[email]': 'syahong@fulihui.com',
    'user[company_id]': '19574',
    'user[password]': 'syh123456',
    'user[remember_me]': 0,
    'commit': '登 录'
}
sign_injsons = {"utf8"}
# head = {
#     'Cookie':'aliyungf_tc=AQAAADT4NkGvFAoAoq1fZVYAAJ5zWzrD; _helpdesksysteem_session=Yi9yWTdCUjllQlRhVko4QkthYWM2dkRSWDBzU1MvS3Vad08zQThWbDhxbm0vQUxxVy9IdE1ST3J2emdYWC9POVRRbVU4eGxKb0NTKzRFd09Nb3MrSENjdmh3Q0w3R3pPZVRXckZUQjZFRmRSYWYyY1V3VVpyWkxFN1lTanVmbVJjMmU1cU9DK3E3YUMxTXBLNjhScUJsai9wVSt5eUd4UGtFR0gvWE5iSlp4RS95YWJWUWk5Sm4vT3duS0cxSWJFZzhNQkJWK1NhL0dPbkVHUmVYakRjeFpBanlsVlRCR0MydmRCbUxOc1Njb1kraXQzeTlCQmExSXY4bnM4MUtnZXRWUHd6RnhTNjBGWXVHbHhveTFBNFpmUVhCeE1NVzVkVWptTk1za0dQbjBlY0JhL2diTWJGTFovTHJMT21PT0MtLU9oYmpZeUU0Q1Q1Y3hWODRHeExDblE9PQ%3D%3D--fd2c65202d703e47ae7e41c426a486c98c99ee8b; Hm_lvt_04a130f55f93916ac7fabec664481931=1495780718; Hm_lpvt_04a130f55f93916ac7fabec664481931=1495780718'
# }
s =requests.session()

a = s.get(url=orgurl)
# time.sleep(5)
# print(a.cookies)
# print(a.status_code)
# print(requests.utils.dict_from_cookiejar(a.cookies))
b=s.get(url=sign_inurl)
# time.sleep(5)
# print(str(requests.utils.dict_from_cookiejar(b.cookies))[0:-1])
s.cookies=b.cookies
ress =s.post(url=sign_inurl,data=sign_indate,json=sign_injsons)
print(ress.headers)
print(ress.status_code)
print(ress.request)
print(ress.request.headers)


jsons = {
    "filter_id": "204793",
    "order": "",
    "column": "",
    "page": 1,
    "page_size": 100,
    "sort_by": [
        [
            "created_at",
            "desc"
        ]
    ],
    "all_conditions": [
        {
            "field_name": "status",
            "operation": "is",
            "value": "open"
        },
        {
            "field_name": "assignee_id",
            "operation": "is",
            "value": "current_user"
        }
    ],
    "any_conditions": [],
    "group_name": "null"
}
res = s.post(url='http://fulihui.udesk.cn/spa1/tickets/list',  json=jsons)
print(res.json())
print(res.reason)
print(res.headers)
print('...................')
print(res.request.headers)