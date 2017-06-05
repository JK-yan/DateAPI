# -*- coding: UTF-8 -*-
import json

import requests
import yaml
from lxml import etree

# import requests as re
loginurl = 'http://www.onlinesjtu.com/Index.aspx'
# dianbolist = 'http://www.onlinesjtu.com/learningspace/learning/student/dianbolist.asp?userid=716101520010&realname=&.3420932=.6418535 '
# username = input('用户名： ')
# passward = input('密码： ')
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
header1 = {
    'Connection': 'keep-alive',
    'Host': 'www.onlinesjtu.com',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Upgrade-Insecure-Requests': '1'
}
s = requests.session()
res = s.post(url=loginurl, data=data, headers=header1)
ress = s.get(res.url)
header2 = {
    'Connection': 'keep-alive',
    'Host': 'www.onlinesjtu.com',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Upgrade-Insecure-Requests': '1',
    # 'Cookie': ress.headers['Set-Cookie'].split(';')[0]
    'Cookie': 'ASPSESSIONIDAACRDTSC=LOICMHACBDJAJPCOCEFMOGJF',
    'Cache-Control': 'max-age=0'
}

html = etree.HTML(res.text)
reesult = html.xpath('//*[@name="left"]/@src')
print(reesult)
lefturl = 'http://www.onlinesjtu.com/learningspace/learning/' + reesult[0]
leftres = s.get(url=lefturl)
# print(leftres.url)
# print(leftres.status_code)
print(leftres.headers)
# print(leftres.text)
html1 = etree.HTML(leftres.content)
print(html1)
print(type(html1))
# courselist = html1.xpath('//*[@id="jiaoxue"]/table/tr[2]/td/div/a/@href')
courselist = html1.xpath('//*/a[starts-with(@href,"dianbolist.asp?")]/@href')
# Signinlist = html1.xpath('//*[@id="xueyuanjieshao"]/table/tr[2]/td/div/a/@href')
Signinlist = html1.xpath('//*/a[starts-with(@href,"kaoqin_list.asp?")]/@href')
print(courselist)
print(Signinlist)
courselisturl = 'http://www.onlinesjtu.com/learningspace/learning/student/' + courselist[0]
courselistres = s.get(url=courselisturl, headers=header1)
print(courselistres.headers)
# print(courselistres.content.decode('gb2312'))
print(courselistres.cookies)
print(courselistres.apparent_encoding)

html2 = etree.HTML(courselistres.content.decode('GB2312'))

# aw = open('aa.ymal', mode='wb')
# aw.writelines(courselistres.text)
# aw.close()
a = "/div/[text='毛泽东思想和中国特色社会主义理论体系概论']/parent::*"
b = '/html/body/table[2]/tbody/tr[3]/td[1]/div'
courselist1 = html2.xpath('//*/div[contains(text(),"毛泽东思想和中国特色社会主义理论体系概论")]/../..//*/text()')
courselist2 = html2.xpath('//*/a[starts-with(@href,"downloadlist.asp?")]/@href')
downl = 'http://www.onlinesjtu.com/learningspace/learning/student/' + courselist2[1]
downres = s.get(url=downl)
print(downres.content.decode('GB2312'))
print(downres.apparent_encoding)
xunlei = etree.HTML(downres.content.decode('GB2312'))
xunlei1 = xunlei.xpath('//*/a[contains(text(),"迅雷下载")]/@href')
print(xunlei1)
print(len(xunlei1))
print(json.dumps(xunlei1))
a = json.dumps(xunlei1)
b = yaml.dump(xunlei1)
ww = open("course.json", mode='w+', encoding='utf-8')
qq = open("course.yml", mode='w+', encoding='utf-8')
ww.writelines(a)
ww.close()
qq.writelines(b)
qq.close()


# print(courselist1)
# print(courselist2)
# print(len(courselist2))
# for i in range(0, len(courselist2)):
#     print(courselist2[i])
# cour=[]
# with open('course.json', encoding="utf-8") as f:
#     # cour.append(f.read())
#     data = json.load(f)
# print(data)
# for i in range(0, len(data)):
#     cour.append(data[i]+":"+courselist2[i])
# print(yaml.dump(cour))
# print("苏大")
# /html/body/table[2]/tbody/tr/td/div
# print(ress.url)/html/body/table/tbody[2]/tr[1]
# /html/body/table/tbody[2]/tr[1]/td[1]/div/a[1]
# href="test1.asp?term_identify=2017_1&amp;userid=716101520010&amp;courseid=1767&amp;resourceid=239423&amp;username=&amp;ishd=1"
# href="test1.asp?term_identify=2017_1&amp;userid=716101520010&amp;courseid=1767&amp;resourceid=239424&amp;username=&amp;ishd=1"
def findxpath(htmlbody, xpathload):
    selector = etree.HTML(htmlbody)
    return selector.xpath(xpathload)


def response(method, url, form=None, json=None):
    s = requests.session()
    if method == 'get':
        return s.get(url=url, params=form)
    elif method == 'post':
        return s.post(url=url, data=form, json=json)
