#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test.py    
@Contact :   625711951@qq.com
@License :   (C)Copyright 2019-2020, Zyf-FT

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/9/20 20:30   zyfei      1.0         None
'''

import requests

def download_txt_by_url(url):
    url = url
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',}
    resp = requests.get(url, headers=headers)
    resp.encoding = 'utf-8'
    html = resp.text
    if 'The server is temporarily busy, try again later!' in html:
        print('网页无法打开')
        return None
    with open('../test/test.txt', 'w', encoding='utf-8') as f:
        f.write(html)
        print('下载保存成功')

if __name__ == '__main__':
    url = 'https://www.txt80.com/e/DownSys/doaction.php?enews=DownSoft&classid=7&id=9730&pathid=0&pass=02a271cc4ca63754d7d93980e71c5e22&p=::::::'
    download_txt_by_url(url)
