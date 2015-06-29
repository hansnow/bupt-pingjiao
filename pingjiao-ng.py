#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import urllib
import urllib2
import cookielib
import requests as rq
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf8')
print '\n\nPowered by xiaohan HOME <http://yunbo.li>\n\n'
# cookie = cookielib.CookieJar()
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# urllib2.install_opener(opener)
# username = raw_input("请输入学号：")
# password = raw_input("请输入教务系统密码：")
comment = raw_input("请输入评语：")
# key = urllib.urlencode({
#     "type":"sso",
#     "zjh":username,
#     "mm":password
# })
# req = urllib2.Request("http://jwxt.bupt.edu.cn/jwLoginAction.do",key)
# login_page = BeautifulSoup(urllib2.urlopen(url="http://jwxt.bupt.edu.cn/jwLoginAction.do",data=key).read().decode('gbk'))
cookies = dict(JSESSIONID="abcFJ-ZlWUOLleBKzo-4u")
login_page = BeautifulSoup(rq.get("http://jwxt.bupt.edu.cn/jxpgXsAction.do?oper=listWj",cookies=cookies).text)
if login_page.title.text.strip() == '学生评估问卷列表':
    print '[+] 登录成功，准备开始评教...'
else:
    print '[!] 登录失败，请检查用户名密码并重新运行本程序'
    exit()
soup = BeautifulSoup(rq.get("http://jwxt.bupt.edu.cn/jxpgXsAction.do?oper=listWj", cookies=cookies).text)
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
    pre_post_data = {
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
        'pageNo':''}
    rq.post('http://jwxt.bupt.edu.cn/jxpgXsAction.do',data=pre_post_data, cookies=cookies)

    post_data = {
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
        'zgpj':comment.encode('gbk')
    }
    
	# 有些实验课老师的表单和理论课老师的不一样
    post_data2 = {
        'wjbm':i['wjbm'],
        'bpr':i['bpr'],
        'pgnr':i['pgnr'],
        '0000000001':'10_0.95',
        '0000000012':'8_0.95',
        '0000000004':'10_0.95',
        '0000000015':'10_0.95',
        '0000000013':'12_0.95',
        '0000000016':'12_0.95',
        '0000000017':'12_0.95',
        '0000000018':'8_0.95',
        '0000000019':'10_0.95',
        '0000000020':'8_0.95',
        'zgpj':comment.encode('gbk')
    }
 
    res = rq.post('http://jwxt.bupt.edu.cn/jxpgXsAction.do?oper=wjpg', data=post_data, cookies=cookies).text
	# 对于实验课老师的一个ugly补丁
    res = rq.post('http://jwxt.bupt.edu.cn/jxpgXsAction.do?oper=wjpg', data=post_data2, cookies=cookies).text
    if str(res).find('成功'):
        print "[+] 已给〔"+i['bprm']+"〕老师评教！"
    else:
        print "[!] 对〔"+i['bprm']+"〕老师评教失败！"
print '[+] 共评价'+str(len(data))+'位老师，感谢使用！'
print '\n\nPowered by xiaohan HOME <http://yunbo.li>\n\n'
final = raw_input('按任意键退出...')
