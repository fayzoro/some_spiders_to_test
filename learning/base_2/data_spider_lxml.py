#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from bs4 import BeautifulSoup
import lxml.html


# 有缺失的页面
broken_html = '<html><body><ul><li id="ss" class="word" href="www.baidu.com">hello<span class="dd">li里面的span</span></li><li>world</li><li ttclass="word">take</html>'
# 对缺失的标签进行添加
soup = BeautifulSoup(broken_html, 'html.parser')
fixed_html = soup.prettify()

# css 选择器
tree = lxml.html.fromstring(fixed_html)
li = tree.cssselect('li#ss > span.dd')
# 查找id为ss的li标签 下面 class 为dd的span标签
area = li.text_content()
print(area)
lis = tree.cssselect('li[class=word]')
# 查找class为word的所有li标签