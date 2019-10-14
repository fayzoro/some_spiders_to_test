#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# 识别网站构建技术
import builtwith
# 识别网站所有者
import whois

url = 'https://www.baidu.com'

built = builtwith.parse(url)

print(built)

print('-------下面是网站所有者-----')
user = whois.whois(url)

print(user)
