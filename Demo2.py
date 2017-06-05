import json
import random

import requests
import time

platform = ['wechat', 'app']
sourcecode = ['null', 'WEI_XIN_WBY', 'YAN_JIAN_KAI']
url = ['webapp.fulihui.org/home/fuli/0', 'webapp.fulihui.org/home/fuli/1','webapp.fulihui.org/home/coupon/detail/', 'webapp.fulihui.org/home/live/index',
       'webapp.fulihui.org/home/index/', 'webapp.fulihui.org/home/live/detail/','webapp.fulihui.org/home/task/detail/']
detail = ['webapp.fulihui.org/home/coupon/detail/', 'webapp.fulihui.org/home/live/detail/','webapp.fulihui.org/home/task/detail/']
# businessid = ['']
openid = ['']



def timestamp(format_time='%Y-%m-%d %H:%M:%S'):
    """
    获取当前时间
    :return:
    """
    return time.strftime(format_time, time.localtime(time.time()))


# tracePointLog = {'tracePointLog':'{"platform": "wechat",
#                      "sourcecode": "%s" % sourcecode[random.randint(0, 3)],
#                      "url": "%s" %url[2],
#                      "businessid": "%s" % businessid[random.randint(0, len(businessid))],
#                      "datetime": "%s" %timestamp(),
#                      "openid": ""}'
#                 }

# aa = '"platform": "wechat","sourcecode": "WEI_XIN_WBY","url": "webapp.fulihui.org/home/index/","businessid": "","datetime": "2016-12-15 13:55:19","openid": ""'+da
# tracePointLog = {
#     'tracePointLog': '{"platform": "wechat","sourcecode": "%s"' % sourcecode[
#         random.randint(0, len(sourcecode) - 1)] + ',"url": "%s"' % url[
#         random.randint(0, len(url) - 1)] + ',"businessid": "%s"' % businessid[
#         random.randint(0, len(businessid) - 1)] + ',"datetime":"%s"' % timestamp() + ',"openid": ""}'
# }

# tracePointLog={'tracePointLog':'{"platform":"wechat","sourcecode":"WEI_XIN_WBY","url":"webapp.fulihui.org/home/index/","businessid":"","datetime":"2016-12-15 13:55:19","openid":""}'}
uri = []

def ip_userid():

    ip = '%s.%s.%s.%s' % (random.randint(1, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    userid = '%s' % random.randrange(10000000000000000, 1000000000000000000, 1000000000000000)
    return ip, userid

def send_request(i=0, number=int,):
    while i < number:
        date = '2016-12-%s' % random.randint(20, 22) + ' %s' % random.randint(0, 23) + ':%s' % random.randint(0, 59) + ':%s' % random.randint(0, 59)
        uri = "%s" % url[random.randint(0, len(url) - 1)]
        code = "%s" % sourcecode[random.randint(0, len(sourcecode) - 1)]
        businessid = "%s" % random.randrange(100, 1000, 1)
        if uri not in detail:
            tracePointLog = {
                'tracePointLog': '{"platform": "%s"'%platform[random.randint(0, 1)]+',"sourcecode": "%s"' % code + ',"url": "%s"' % uri + ',"businessid": " ","datetime":"%s"' % date + ',"openid": ""}'
            }
        else:
            tracePointLog = {
                'tracePointLog': '{"platform": "%s"' % platform[random.randint(0, 1)] + ',"sourcecode": "%s"' % code + ',"url": "%s"' % uri + ',"businessid": "%s"' % businessid + ',"datetime":"%s"' % date + ',"openid": ""}'
            }
        # s = requests.Session()
        # json={"phone":"1862517%s"%random.randrange(1001, 9999),"vcode":"0000","latitude":"","longitude":""}
        # s.post('http://webapp.fulihui.com/v2/api/commons/auth/quickLogin ',json=json)
        res = s.get(url='http://webapp.fulihui.com/v2/api/tracepoint/markPoint', params=tracePointLog)

        i += 1

        # print(i)
    #     aaa = json.loads(tracePointLog['tracePointLog'])
    #     if res.status_code != 200:
    #         print(res.status_code)
    #         print(res.url)
    #         print(aaa)
    #         print('.............分割线...............')
    #         break
    #     elif not aaa['sourcecode']:
    #         urli = aaa['url'] + aaa['businessid']
    #         uri.append(urli)
    #     else:
    #         urli = aaa['url'] + aaa['businessid'] + '?LC=' + aaa['sourcecode']
    #
    #         uri.append(urli)
    # print(set(uri))
    # for tc in set(uri):
    #     print(tc+'的PV一共：'+str(uri.count(tc))+'次')
    #     # print(uri.count(i))
    # print(i)


if __name__ == '__main__':
    # print(tracePointLog)
    # aa=json.loads(json.dumps(tracePointLog))
    number = input()
    start = time.clock()
    send_request(number=int(number))
    end = time.clock()
    print("The function run time is : %.03f seconds" % (end - start))
