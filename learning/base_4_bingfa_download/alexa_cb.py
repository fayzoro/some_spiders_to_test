#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   alexa_cb.py    
@Contact :   625711951@qq.com
@License :   (C)Copyright 2019-2020, Zyf-FT

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/10/18 22:03   zyfei      1.0         None
'''

import csv
from zipfile import ZipFile
from StringIO import StringIO
from mongo_cache import MongoCache


class AlexaCallback:
    def __init__(self, max_urls=1000):
        self.max_urls = max_urls
        self.seed_url = 'http://s3.amazonaws.com/alexa-static/top-1m.csv.zip'

    def __call__(self, url, html):
        if url == self.seed_url:
            urls = []
            cache = MongoCache()
            with ZipFile(StringIO(html)) as zf:
                csv_filename = zf.namelist()[0]
                for _, website in csv.reader(zf.open(csv_filename)):
                    if 'http://' + website not in cache:
                        urls.append('http://' + website)
                        if len(urls) == self.max_urls:
                            break
            return urls
