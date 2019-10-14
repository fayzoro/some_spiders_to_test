#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# urllib.request 是一个独立的包
import urllib.request

def download_html():
    url = 'http://www.umei.cc/p/gaoqing/cn/202000.htm'
    html = urllib.request.urlopen(url).read().decode('utf-8')
    # print(html)
    filename = 'test_file/' + url[-10:-4] + '.html'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
        print('下载成功')


if __name__ == '__main__':
    download_html()