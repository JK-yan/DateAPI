# -*- coding: UTF-8 -*-

import requests
import yaml
from lxml import etree

# userid = input("用户名： ")
# password = input("密码： ")
loginurl = 'http://www.onlinesjtu.com/Index.aspx'
leftlisturl = 'http://www.onlinesjtu.com/learningspace/learning/'
orgurl = 'http://www.onlinesjtu.com/learningspace/learning/student/'
dianboxpath = '//*/a[starts-with(@href,"dianbolist.asp?")]/@href'
leftxpath = '//*[@name="left"]/@src'
kaoqinxpath = '//*/a[starts-with(@href,"kaoqin_list.asp?")]/@href'
xunleixpath = '//*/a[contains(text(),"迅雷下载")]/@href'
downcoursexpath = '//*/a[starts-with(@href,"downloadlist.asp?")]/@href'
# coursenamexpath = '//*/div[contains(text(),"毛泽东思想和中国特色社会主义理论体系概论")]/../../..//*//a/text()'

data = {
    '__VIEWSTATE': '/wEPDwUKMTExOTI5NDk3OWQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgEFImN0bDAwJENvbnRlbnRQbGFjZUhvbGRlcjEkaWJ0TG9naW7UcgS82I2VmoQMeY9GdU2K8I+8zQ==',
    '__VIEWSTATEGENERATOR': '90059987',
    '__EVENTVALIDATION': '/wEWCAKHwK2XDAKP6repDwL59L30DgLs64TUCQLz64TUCQLy64TUCQL8hK66BQKflO50CfaHMVnqLBIAhLgyEgQIbayqmQw=',
    'ctl00$ContentPlaceHolder1$tbuserid': 716101520010,
    'ctl00$ContentPlaceHolder1$tbpassword': 'yanjiankai',
    'ctl00$ContentPlaceHolder1$rblusertype': 0,
    'ctl00$ContentPlaceHolder1$ibtLogin.x': 36,
    'ctl00$ContentPlaceHolder1$ibtLogin.y': 18
}


def response(method, url, form=None, json=None):
    s = requests.session()
    if method == 'get':
        a = s.get(url=url, params=form)
        return a
    elif method == 'post':
        a = s.post(url=url, data=form, json=json)
        return a


def findxpath(htmlbody, xpathload):
    selector = etree.HTML(htmlbody)
    return selector.xpath(xpathload)


res = requests.session()

def login():
    homepage = res.post(url=loginurl, data=data)
    return homepage




def get_Source_Url():
    login = res.post(url=loginurl, data=data)
    lefturl = leftlisturl + findxpath(htmlbody=login.content.decode(encoding=login.apparent_encoding),
                                      xpathload=leftxpath)[0]
    print('获取导航连接并请求: ' + lefturl)
    lefttree = res.get(url=lefturl)
    dianbourl = orgurl + findxpath(lefttree.content.decode(encoding=lefttree.apparent_encoding), dianboxpath)[0]
    print('获取点播url路径: ' + dianbourl)
    kaoqingurl = orgurl + findxpath(lefttree.content.decode(encoding=lefttree.apparent_encoding), kaoqinxpath)[0]
    print('获取考勤url路径: ' + kaoqingurl)
    return dianbourl, kaoqingurl


# dianbourl = get_Source_Url()[0]
# kaoqingurl = get_Source_Url()[1]


def get_Course_Down_UrlList():
    downlist = []
    dow = res.get(dianbourl)
    print('获取到点播下载页面，并获取对应课程现在页面连接')
    coursedowlist = findxpath(dow.content.decode(encoding=dow.apparent_encoding), downcoursexpath)
    for i in range(0, len(coursedowlist)):
        downlist.append(orgurl + coursedowlist[i])
    return downlist


def get_Course_XunLei_UrlList():
    d = {}
    print('获取每个课程下的迅雷下载链接')
    for i in range(0, len(get_Course_Down_UrlList())):
        dow = res.get(get_Course_Down_UrlList()[i])
        xunleiurllist = findxpath(dow.content.decode(encoding=dow.apparent_encoding), xunleixpath)
        d[get_Course_Down_UrlList()[i]] = xunleiurllist
    return d


if __name__ == '__main__':
    print(get_Source_Url())

    print(dianbourl + "ss")
    # print(get_Course_Down_UrlList())

    # print(a.content.decode('GB2312'))
