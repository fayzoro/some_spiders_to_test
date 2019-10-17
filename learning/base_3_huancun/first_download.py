#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   first_download.py
@Contact :   625711951@qq.com
@License :   (C)Copyright 2019-2020, Zyf-FT

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/10/17 21:22   zyfei      1.0         None
'''
import time
import datetime
import random
import urllib
import urllib.request


class Throttle(object):
    '''
        下载限速
    '''
    def __init__(self, delay):
        '''

        :param delay:
        '''
        self.delay = delay
        self.domains = {}

    def wait(self, url):
        '''

        :param url:
        :return:
        '''
        domain = urllib.request.urlparse(url).netloc
        last_accessed = self.domains.get(domain)
        if self.delay > 0 and last_accessed is not None:
            sleep_secs = self.delay - self.delay - (datetime.datetime.now() - last_accessed).seconds
            if sleep_secs > 0:
                time.sleep(sleep_secs)
        self.domains[domain] = datetime.datetime.now()



class Downloader(object):
    '''

    '''
    def __init__(self, delay=5, user_agent='wswp',
                 proxies=None, num_retries=1, cache=None):
        '''

        :param delay:
        :param user_agent:
        :param proxies:
        :param num_retries:
        :param cache:
        '''
        self.throttle = Throttle(delay)
        self.user_agent = user_agent
        self.proxies = proxies
        self.num_retries = num_retries
        self.cache = cache

    def __call__(self, url):
        '''
            回调函数
        :param url:
        :return:
        '''
        result = None
        if self.cache:
            try:
                result = self.cache[url]
            except KeyError:
                pass
            else:
                if self.num_retries > 0 and \
                    500 <= result['code'] < 600:
                    result = None
        if result is None:
            self.throttle.wait(url)
            proxy = random.choice(self.proxies) if self.proxies else None
            headers = {'User-agent': self.user_agent}
            result = self.download(url, headers, proxy, self.num_retries)
            if self.cache:
                self.cache[url] = result
        return result['html']

    def download(url, user_agent='wswp', proxy=None, num_retries=2):
        '''
        设置用户代理， 下载错误后重试
        :param url: 下载地址
        :param user_agent: 用户
        :param proxy:
        :param num_retries: 重试次数
        :return: 下载的页面
        '''
        headers = {'User-agent': user_agent}
        print('downloading...', url)
        request = urllib.request.Request(url, headers=headers)
        opener = urllib.request.build_opener()
        if proxy:
            proxy_params = {urllib.request.urlparse(url).scheme: proxy}
            opener.add_handler(urllib.request.ProxyHandler(proxy_params))
        try:
            # response = urllib.request.urlopen(request).read()
            html = opener.open(request).read()
            html = html.decode('utf-8')
        except urllib.request.URLError as e:
            print('download error:', e.reason)
            html = None
            if num_retries > 0:
                if hasattr(e, 'code') and 500 <= e.code < 600:
                    # retry download
                    html = download(url, 'wswp', proxy, num_retries-1)
        return {'html': html, 'code': code}


if __name__ == '__main__':
    pass