#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   hui_diao_def.py    
@Contact :   625711951@qq.com
@License :   (C)Copyright 2019-2020, Zyf-FT

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/10/17 20:59   zyfei      1.0         None
'''
import re
import lxml
import urllib.parse
import urllib.request
import random
import re


def download(url, user_agent='wswp', num_retries=2):
    '''
    设置用户代理， 下载错误后重试
    :param url: 下载地址
    :param user_agent: 用户
    :param num_retries: 重试次数
    :return: 下载的页面
    '''
    headers = {'User-agent': user_agent}
    print('downloading...', url)
    request = urllib.request.Request(url, headers=headers)
    try:
        response = urllib.request.urlopen(request).read()
        html = response.decode('utf-8')
    except urllib.request.URLError as e:
        print('download error:', e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # retry download
                download(url, user_agent='wswp', num_retries=num_retries-1)
    return html


def link_crawler(seed_url, link_regex):
    '''

    :param seed_url:
    :param link_regex:
    :return:
    '''
    crawl_queue = [seed_url]
    seen = set(crawl_queue)
    while crawl_queue:
        url = crawl_queue.pop()
        print('downloading...', url)
        html = download(url)
        link_list = get_links(html)
        print('link_list =', link_list)
        for link in link_list:
            link = urllib.parse.urljoin(seed_url, link)
            # 判断link是否已经被执行过
            if link in seen:
                continue
            if re.match(link_regex, link):
                seen.add(link)
                crawl_queue.append(link)
                print('crawl_queue =', crawl_queue)


def get_links(html):
    '''

    :param html:
    :return:
    '''
    webpage_regex = re.compile('<a[^> + href=["\'](.*?)["\']', re.IGNORECASE)
    return webpage_regex.findall(html)
    # pattern_1 = '<li><a href="(.*?)" title="'
    # webpage_regex = re.compile(pattern=pattern_1)
    # return webpage_regex.findall(htmls)


# def scrape_callback(url, htmls):
#     '''
#
#     :param url:
#     :param htmls:
#     :return:
#     '''
#     if re.search('/view/', url):
#         tree = lxml.htmls.fromstring(htmls)
#         row = [tree.cssselect('table > tr#places_%s_row > td.w2p_fw' % field)[0].text_content() for field in FIELDS]
#         print(url, row)
#     pass

if __name__ == '__main__':
    pass
    link_crawler('http://example.webscraping.com', '/(index|view)')