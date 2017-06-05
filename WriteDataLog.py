# -*- coding:utf-8 -*-
import json
import random
import time



url = ['webapp.fulihui.org/home/fuli/0', 'webapp.fulihui.org/home/fuli/1','webapp.fulihui.org/home/coupon/detail/', 'webapp.fulihui.org/home/live/index',
       'webapp.fulihui.org/home/index/', 'webapp.fulihui.org/home/live/detail/','webapp.fulihui.org/home/task/detail/']
detail = ['webapp.fulihui.org/home/coupon/detail/', 'webapp.fulihui.org/home/live/detail/','webapp.fulihui.org/home/task/detail/']
# businessid = random.randrange(100, 1000, 1)
platform = ['wechat', 'app']
# sourcecode = ['null', 'YAN_JIAN_KAI', 'WEI_XIN_WBY', 'BU_SA', 'LCK_WTA', 'ASD_SADA', 'WAQ_SS', 'DAWAW_SDAW', 'SADQQ_DWW','WWW.BAIDU.COM', 'ASDWQQ_SDAW']
sourcecode = ['null', 'DAWAW_SDAW', 'libaozhong001', 'jinyang', 'WANG_BANG_YU', 'YAN_JIAN_KAI', 'WEI_XIN_WBY']
PV_UV = []
JSON = []

def timestamp(format_time='%Y-%m-%d %H:%M:%S'):
    """
    获取当前时间
    :return:76511736743710720
    """

    return time.strftime(format_time, time.localtime(time.time()))


def ip_userid():

    ip = '%s.%s.%s.%s' % (random.randint(1, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    userid = '%s' % random.randrange(10000000000000000, 1000000000000000000, 1000000000000000)
    return ip, userid


def get_log_adress():
    date = '2016-12-%s' % random.randint(20, 21)+' %s' % random.randint(0, 23) + ':%s' % random.randint(0, 59) + ':%s' % random.randint(0, 59)
    uri = "%s" % url[random.randint(0, len(url) - 1)]
    code = "%s"%sourcecode[random.randint(0, len(sourcecode) - 1)]
    businessid = "%s"%random.randrange(100, 1000, 1)
    # userid = "%s"%ip_userid()[random.randint(0, 1)]
    if random.randint(0, 1) == 1:
        userid = "%s" % ip_userid()[1]
        clientip = "%s" % ip_userid()[0]
    else:
        clientip = userid = "%s" % ip_userid()[0]


    if uri not in detail:
        log = '-TRACE_POINT_LOG-{"datetime":"%s"' % date + ',"openid":"","clientip":"%s"' %clientip + ',"businessid":"","userid":"%s"' %userid + ',"platform":"%s"'%platform[random.randint(0, 1)]+',"url":"%s"' % uri + ',"sourcecode":"%s"'% sourcecode[random.randint(0, len(sourcecode) - 1)]+'}'
        PV_UV.append(uri)
        JSON.append(log[17:])
    else:
        log = '-TRACE_POINT_LOG-{"datetime":"%s"' % date + ',"openid":"","clientip":"%s"' %clientip + ',"businessid":"%s"'%businessid+',"userid":"%s"'  %userid + ',"platform":"%s"' % platform[random.randint(0, 1)] + ',"url":"%s"' % uri + ',"sourcecode":"%s"' % code + '}'
        PV_UV.append(uri+businessid+'?LC='+code)
        JSON.append(log[17:])
    return log, PV_UV, JSON


def write_log(file):
    with open(file, mode='a') as f:
        url = get_log_adress()[0]
        f.write(url+'\n')
        print(url)
        f.close()

def get_pv_uv():
    for i in JSON:
        data = json.loads(i)['url']
        print(data)

if __name__ == '__main__':
    number = int(input())
    file = 'mark-point.log'
    start = time.clock()
    while 0 < number:
        number -= 1
        write_log(file)

    # uv = set(PV_UV)
    end = time.clock()
    print("The function run time is : %.03f seconds" % (end - start))
    print(len(PV_UV))
    get_pv_uv()


    # for i in set(PV_UV):
    #     # print(i+"    [PV一共有："+str(PV_UV.count(i))+"次]")
    #     with open('pv_uv.log',mode='a') as f:
    #         f.write(i+"    [PV一共有："+str(PV_UV.count(i))+"次]"+'\n')
    # print(PV_UV.count('webapp.fulihui.org/home/fuli/'))
    # for i in uv:
    #     print(i+"    [PV一共有："+str(PV_UV.count(i))+"次]")
