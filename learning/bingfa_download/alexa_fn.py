#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   alexa_fn.py    
@Contact :   625711951@qq.com
@License :   (C)Copyright 2019-2020, Zyf-FT

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/10/18 22:03   zyfei      1.0         None
'''

import csv
from zipfile import ZipFile
from StringIO import StringIO
from downloader import Downloader


def alexa():
    D = Downloader()
    zipped_data = D('http://s3.amazonaws.com/alexa-static/top-1m.csv.zip')
    urls = [] # top 1 million URL's will be stored in this list
    with ZipFile(StringIO(zipped_data)) as zf:
        csv_filename = zf.namelist()[0]
        for _, website in csv.reader(zf.open(csv_filename)):
            urls.append('http://' + website)
    return urls


if __name__ == '__main__':
    print(len(alexa()))
