#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   process_test.py    
@Contact :   625711951@qq.com
@License :   (C)Copyright 2019-2020, Zyf-FT

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/10/18 22:04   zyfei      1.0         None
'''

import sys
from process_crawler import process_crawler
from mongo_cache import MongoCache
from alexa_cb import AlexaCallback


def main(max_threads):
    scrape_callback = AlexaCallback()
    cache = MongoCache()
    cache.clear()
    process_crawler(scrape_callback.seed_url, scrape_callback=scrape_callback, cache=cache, max_threads=max_threads, timeout=10)


if __name__ == '__main__':
    max_threads = int(sys.argv[1])
    main(max_threads)
