import json
import random

import requests
import time

platform = ['ios', 'android', 'h5']
sourcecode = ['null', 'WEI_XIN_WBY', 'YAN_JIAN_KAI']
datetime = '2016-12-%s' % random.randint(20, 22) + ' %s' % random.randint(0, 23) + \
           ':%s' % random.randint(0, 59) + \
           ':%s' % random.randint(0, 59)
businessid = "%s" % random.randrange(100, 1000, 1)
userid = []
deviceid = "%s" % random.randrange(100, 1000, 1)
openid = []
biztype = ['INFO_APP', 'ACTIVITY_APP']
modulepage = {'tab': ['', ''], 'detail': []}
productcode = "YOUKANTOU"


def timestamp(format_time='%Y-%m-%d %H:%M:%S'):
    """
    获取当前时间
    :return:
    """
    return time.strftime(format_time, time.localtime(time.time()))


uri = []


def ip_userid():
    ip = '%s.%s.%s.%s' % (
        random.randint(1, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    userid = '%s' % random.randrange(10000000000000000, 1000000000000000000, 1000000000000000)
    return ip, userid


def send_request(i=0, number=int, ):
    while i < number:
        datetime = '2016-12-%s' % random.randint(20, 22) +\
                   ' %s' % random.randint(0, 23) + ':%s' % random.randint(0,59) + \
                   ':%s' % random.randint(0, 59)
        businessid = "%s" % random.randrange(100, 1000, 1)
        userid = ''
        deviceid = ''
        openid = ''
        biztype = ''
        platform = ''
        modulepage = ''
        sourcecode = "%s" % sourcecode[random.randint(0, len(sourcecode) - 1)]
        productcode = productcode

        if uri not in modulepage:
            tracePoint = '{"datetime": "%s",' \
                         '"businessid": "%s",' \
                         '"userid": "%s",' \
                         '"deviceid": "%s",' \
                         '"openid": "%s",' \
                         '"biztype": "%s",' \
                         '"platform": "%s",' \
                         '"modulepage": "%s",' \
                         '"sourcecode": "%s",' \
                         '"productcode": "YOUKANTOU"}'\
                         % (datetime, businessid, userid,
                            deviceid, openid, biztype,
                            platform, modulepage, sourcecode)
            tracePointLog = {
                'tracePointLog': 'tracePoint'
            }
        else:
            tracePoint = '{"datetime": "%s",' \
                         '"businessid": "%s",' \
                         '"userid": "%s",' \
                         '"deviceid": "%s",' \
                         '"openid": "%s",' \
                         '"biztype": "%s",' \
                         '"platform": "%s",' \
                         '"modulepage": "%s",' \
                         '"sourcecode": "%s",' \
                         '"productcode": "YOUKANT OU"}' \
                         % (datetime, businessid, userid,
                            deviceid, openid, biztype,
                            platform, modulepage, sourcecode)
            tracePointLog = {
                'tracePointLog': 'tracePoint'
            }
        # s = requests.Session()
        # json={"phone":"1862517%s"%random.randrange(1001, 9999),"vcode":"0000","latitude":"","longitude":""}
        # s.post('http://webapp.fulihui.com/v2/api/commons/auth/quickLogin ',json=json)
        # res = s.get(url='http://webapp.fulihui.com/v2/api/tracepoint/markPoint', params=tracePointLog)

        i += 1


if __name__ == '__main__':
    # print(tracePointLog)
    # aa=json.loads(json.dumps(tracePointLog))
    # number = input()
    # start = time.clock()
    # send_request(number=int(number))
    # end = time.clock()
    # print("The function run time is : %.03f seconds" % (end - start))
    print(datetime)
