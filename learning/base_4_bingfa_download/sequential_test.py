#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   sequential_test.py    
@Contact :   625711951@qq.com
@License :   (C)Copyright 2019-2020, Zyf-FT

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/10/18 22:04   zyfei      1.0         None
'''

from crawler import crawler
from mongo_cache import MongoCache
from alexa_cb import AlexaCallback


def main():
    scrape_callback = AlexaCallback()
    cache = MongoCache()
    #cache.clear()
    crawler(scrape_callback.seed_url, scrape_callback=scrape_callback, cache=cache, timeout=10, ignore_robots=True)


if __name__ == '__main__':
    main()
