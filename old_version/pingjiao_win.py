#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import urllib
import urllib2
import cookielib
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf-8')
cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
urllib2.install_opener(opener)
username = raw_input("请输入学号：".encode('gbk'))
password = raw_input("请输入教务系统密码：".encode('gbk'))
comment = raw_input("请输入评语：".encode('gbk'))
key = urllib.urlencode({
    "type":"sso",
    "zjh":username,
    "mm":password
})
req = urllib2.Request("http://10.3.240.72/jwLoginAction.do",key)
login_page = BeautifulSoup(urllib2.urlopen(url="http://10.3.240.72/jwLoginAction.do",data=key).read().decode('gbk'))
if login_page.title.text == '学分制综合教务':
    print '[+] 登录成功，准备开始评教...'.encode('gbk')
else:
    print '[!] 登录失败，请检查用户名密码并重新运行本程序'.encode('gbk')
    exit()
soup = BeautifulSoup(urllib2.urlopen("http://10.3.240.72/jxpgXsAction.do?oper=listWj").read().decode('gbk'))
data_init = soup.find_all(title='评估')
data = []
for i in data_init:
    data.append({'wjbm':i['name'].split('#@')[0],
        'bpr':i['name'].split('#@')[1],
        'pgnr':i['name'].split('#@')[5],
        'wjmc':i['name'].split('#@')[3],
        'bprm':i['name'].split('#@')[2],
        'pgnrm':i['name'].split('#@')[4],})
for i in data:
    pre_post_data = urllib.urlencode({
        'wjbm':i['wjbm'],
        'bpr':i['bpr'],
        'pgnr':i['pgnr'],
        'oper':'wjShow',
        'wjmc':i['wjmc'],
        'bprm':i['bprm'],
        'pgnrm':i['pgnrm'],
        'pageSize':'20',
        'page':'1',
        'currentPage':'1',
        'pageNo':''})
    urllib2.urlopen(url='http://10.3.240.72/jxpgXsAction.do',data=pre_post_data)

    post_data = urllib.urlencode({
        'wjbm':i['wjbm'],
        'bpr':i['bpr'],
        'pgnr':i['pgnr'],
        '0000000021':'10_0.95',
        '0000000022':'10_0.95',
        '0000000023':'5_0.95',
        '0000000024':'20_0.95',
        '0000000025':'10_0.95',
        '0000000026':'5_0.95',
        '0000000027':'5_0.95',
        '0000000028':'20_0.95',
        '0000000029':'10_0.95',
        '0000000030':'5_0.95',
        'zgpj':comment
    });
    req = urllib2.Request('http://10.3.240.72/jxpgXsAction.do?oper=wjpg',post_data)
    res = urllib2.urlopen(req).read().decode('gbk')
    if str(res).find('成功'):
        print ("[+] 已给〔"+i['bprm']+"〕老师评教！").encode('gbk')
    else:
        print ("[!] 对〔"+i['bprm']+"〕老师评教失败！").encode('gbk')
print ('[+] 共评价'+str(len(data))+'位老师，感谢使用！').encode('gbk')
print 'Powered by xiaohan HOME <http://yunbo.li>'
final = raw_input('按任意键退出...'.encode('gbk'))



