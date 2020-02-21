#!/usr/bin/env python
# _*_ coding:utf-8 _*_

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
    pattern_1 = '<li><a href="(.*?)" title="'
    webpage_regex = re.compile(pattern=pattern_1)
    return webpage_regex.findall(html)


def main():
    url = 'http://www.umei.cc/p/gaoqing/cn/202000.htm'
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
    # htmls = download(url, user_agent=user_agent)
    # print(htmls)
    link_crawler(url, link_regex=r"http://www.umei.cc/p/gaoqing/cn/(.*?).htm")

if __name__ == '__main__':
    main()