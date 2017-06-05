import json

import requests
from pyasn1.compat.octets import null


s = requests.session()
sign_inurl = 'http://fulihui.udesk.cn/users/sign_in'
sign_indate = {
    'utf8': '✓',
    'authenticity_token': '/tf9bfoj7HxtZ9YNrTMNuVdW9mfNPVWsUxIarYMiEL4=',
    'user[email]': 'yjianhui@fulihui.com',
    'user[company_id]': '19574',
    'user[password]': 'flh123456',
    'user[remember_me]': 0,
    'user[remember_me]': 1,
    'commit': '登录'
}
sign_injsons = {"utf8"}
head = {
    'Cookie':'aliyungf_tc=AQAAADT4NkGvFAoAoq1fZVYAAJ5zWzrD; _helpdesksysteem_session=Yi9yWTdCUjllQlRhVko4QkthYWM2dkRSWDBzU1MvS3Vad08zQThWbDhxbm0vQUxxVy9IdE1ST3J2emdYWC9POVRRbVU4eGxKb0NTKzRFd09Nb3MrSENjdmh3Q0w3R3pPZVRXckZUQjZFRmRSYWYyY1V3VVpyWkxFN1lTanVmbVJjMmU1cU9DK3E3YUMxTXBLNjhScUJsai9wVSt5eUd4UGtFR0gvWE5iSlp4RS95YWJWUWk5Sm4vT3duS0cxSWJFZzhNQkJWK1NhL0dPbkVHUmVYakRjeFpBanlsVlRCR0MydmRCbUxOc1Njb1kraXQzeTlCQmExSXY4bnM4MUtnZXRWUHd6RnhTNjBGWXVHbHhveTFBNFpmUVhCeE1NVzVkVWptTk1za0dQbjBlY0JhL2diTWJGTFovTHJMT21PT0MtLU9oYmpZeUU0Q1Q1Y3hWODRHeExDblE9PQ%3D%3D--fd2c65202d703e47ae7e41c426a486c98c99ee8b; Hm_lvt_04a130f55f93916ac7fabec664481931=1495780718; Hm_lpvt_04a130f55f93916ac7fabec664481931=1495780718'
}
s.post(url=sign_inurl,headers=head,data=sign_indate,json=sign_injsons)
print("登陆成功")

# head = {
#     # 'Cookie':'aliyungf_tc=AQAAADT4NkGvFAoAoq1fZVYAAJ5zWzrD; remember_user_token=BAhbB1sGaQJVokkiIiQyYSQxMCRyVEJwdS53TGEzM0F6S292OEF6L04uBjoGRVQ%3D--5ac3f9aba428f9da041dd5c1a93667c0ee600805; Hm_lvt_04a130f55f93916ac7fabec664481931=1495780718; Hm_lpvt_04a130f55f93916ac7fabec664481931=1495780746; _ga=GA1.2.369305016.1495780746; _gat=1; _helpdesksysteem_session=elI4MEdHTVdTVmtmQ0FUUTRMNXZhcGFWM0FZODFUMEJtZUNIYTJGMlJvS3pXdWxQYlpJY1p5cDBDazVQa0FUNTZEOHJsdmJHZE45R0NWU0F4UU12cHhqRmZhempTbDZLVEloYndyK0NKOEM2bE9XZjUzKzRKSE9ySmEvMmhQTmJJZHZ0UHlXYXBrQlV1dDhpREtjWkJJQloyTkg2d0VRcXYvSWZOUHlNNklEYUVDRGt2Ry9Hb1Mxd0dFdC96WC81a3F4UldlalB1bmh2QmZhV05QRUpYZ0dUcEtMMHhoKzZxaEUvSGFiTlZwdmVWMFpzRHYzSWgxRTJCVnpMWWdNRVJPZ3RaTVVRWTBRVDdLNVE5MHQ1WlBNczJENGxSQWZ1N0x1YVduUk5sdmU4L0lJTGdET01nWWxqRFpZelR2aVFQaVhRelM4YXdYSWMrWW5TKyszemV3PT0tLWR6RG9qMi94TExPdmY3UFVsOTNEZnc9PQ%3D%3D--d57584e37d34ba8d9e970961427034b7291dac35'
#     'Cookie':'aliyungf_tc='+ress.cookies['aliyungf_tc']
# }
jsons = {
    "filter_id": "204793",
    "order": "",
    "column": "",
    "page": 1,
    "page_size": 2,
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
# res = s.post(url=url, headers=head, json=jsons)

# ['tickets']['ticket']['agent_group_id']
# a = json.dumps(res.json())
a=res.json()["tickets"]
print(a)
b = []
for i in a:
    b.append(i['ticket']['id'])

updateurl = 'http://fulihui.udesk.cn/spa1/tickets/bulk_update/'

date = {
'ticket_ids':str(b)[1:-1],
    'ticket[status_id]':3,
    'comment[content]':'<p>您好，娃哈哈福礼惠。很高兴为您服务！请问有什么可以帮您？</p>',
    'comment[function_type]':'external'
}
sd = {"ticket_ids"}
aa = s.put(url=updateurl,data=date,json=sd)
print(aa.text)
# print(a)
# print(a['tickets']['ticket']['agent_group_id'])