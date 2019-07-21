#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Tim
# 正则表达式
'''
#group ---元组
import re
str1 = 'qytang/cisco/python'
re1 = re.match('(.*)/(.*)/(.*)',str1).groups()
print(re1)
re2 = re.match('(\w+)/(\w+)/(\w+)',str1).groups()
print(re2)
'''
# 随机生成ip地址
'''
import random
section1 = random.randint(1,255)
section2 = random.randint(1,255)
section3 = random.randint(1,255)
section4 = random.randint(1,255)
random_ip = str(section1)+'.'+str(section2)+'.'+str(section3)+'.'+str(section4)
print(random_ip)
'''
import random

#匹配字符串
'''
import re
str2 = 'hello qytang world!'
re1 = str2.split()
print(re1)
re2 = re.match('hello\s+([a-z]+)\s+([a-z]+\s*)',str2).groups()
print(re2)
'''
#实现输出格式化并且匹配IP地址和MAC地址
# IP
#方法一：
'''
str1 = 'Interface             IP-Address       OK?  method        Protocol'
str2 = 'Port-channel1.189     192.168.1.1      YES    CONFIG         UP'
ret1 = str1.split()
ret2 = str2.split()
lst = []
# for i in ret1:
dic = {}
for line in range(len(ret1)):
    dic[ret1[line]]=ret2[line]
lst.append(dic)
print(lst)
'''
#方法二：

import re
str1 = 'Port-channel1.189     192.168.189.254  YES   CONFIG  up         up   '
re1 = re.match('(\w.*\d)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+YES\s+CONFIG\s+(\w+)\s+(\w+)\s*',str1).groups()
# print(re1)
# re2 = re.match('(\w+\-\w+\.\d+)\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s+(\w+)\s+(\w+)\s+(\w+)\s+(\w+)\s+',str1).groups()
# print(re2)
print('%-5s : %s'%('接口',re1[0]))
print('%-5s : %s'%('IP地址',re1[1]))
print('%-5s : %s'%('状态',re1[3]))

#mac
'''
import re
str1 = '166    54a2.74f7.0326    DYNAMIC     Gi1/0/11'
re1 = re.match('(\d{1,4})\s+([0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4})\s+DYNAMIC\s+(\w.+\d)',str1).groups()
# print(re1)
print('%-5s : %s'%('VLAN ID',re1[0]))
print('%-5s : %s'%('MAC地址',re1[1]))
print('%-5s : %s'%('接口',re1[2]))
'''
test = [1,2,3]
print(test,end='')