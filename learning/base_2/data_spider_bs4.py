#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# pip install beautifulsoup4

from bs4 import BeautifulSoup

# 有缺失的页面
broken_html = '<html><body><ul><li class="word" href="www.baidu.com">hello</li><li>world</li><li class="word">take</html>'
# 对缺失的标签进行添加
soup = BeautifulSoup(broken_html, 'html.parser')
fixed_html = soup.prettify()
print(fixed_html)

li = soup.find('li', attrs={'class': 'word'})
print(li)
print(li.text)
print('---------------------------------------------------------')
li = soup.find_all('li', attrs={'class': 'word'})
print(li)