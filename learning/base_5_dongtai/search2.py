#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   search2.py    
@Contact :   625711951@qq.com
@License :   (C)Copyright 2019-2020, Zyf-FT

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/10/19 16:45   zyfei      1.0         None
'''

import json
import csv
import downloader


def main():
    writer = csv.writer(open('countries.csv', 'w'))
    D = downloader.Downloader()
    html = D('http://example.webscraping.com/ajax/search.json?page=0&page_size=1000&search_term=.')
    ajax = json.loads(html)
    for record in ajax['records']:
        writer.writerow([record['country']])


if __name__ == '__main__':
    main()
