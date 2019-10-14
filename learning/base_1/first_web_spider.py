#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import urllib.request
import random
from .settings import user_agent


def download(url):
    '''
    下载访问页面
    :param url: 访问地址
    :return: 页面对应的文档
    '''
    response = urllib.request.urlopen(url).read()
    html = response.decode('utf-8')
    return html


def download_2(url):
    '''
    下载王文页面，下载失败返回提示
    :param url: 访问地址
    :return: 页面内容
    '''
    print('downloading...')
    try:
        html = urllib.request.urlopen(url).read().decode('utf-8')
    except urllib.request.URLError as e:
        print('download error:', e.reason)
        html = None
    return html


def download_3(url, num_retries=2):
    '''
    下载失败重新下载
    :param url: 下载地址
    :param num_retries: 重新下载次数
    :return: 下载网页
    '''
    print('downloading...')
    try:
        response = urllib.request.urlopen(url).read()
        html = response.decode('utf-8')
    except urllib.request.URLError as e:
        print('download error:', e)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 < e.code < 600:
                # 如果网页回应码 5xx 则重试
                return download_3(url, num_retries-1)
    return html


def download_4(url, user_agent='wswp', num_retries=2):
    '''

    :param url:
    :param user_agent:
    :param num_retries:
    :return:
    '''
    print('downloading...', url)
    headers = {
        'User-agent': user_agent,
    }
    request = urllib.request.Request(url,headers=headers)
    try:
        response = urllib.request.urlopen(request).read()
        html = response.decode('utf-8')
    except urllib.request.URLError as e:
        print('download error:', e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # retry 5xx http error
                return download_3(url, user_agent, num_retries-1)
    return html




def main():
    url = 'http://www.umei.cc/p/gaoqing/cn/202000.htm'
    # html = download(url)
    # print(html)
    # html_2 = download_2(url)
    # print(html_2)
    # html_3 = download_3(url)
    # print(html_3)
    html_4 = download_4(url, user_agent=random.choice(user_agent))
    print(html_4)


if __name__ == '__main__':
    main()