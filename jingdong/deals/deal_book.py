#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
from queue import Queue
import time
import random
import requests
from bs4 import BeautifulSoup
import lxml.html


class JingDongBookSpider(object):
    '''
    京东书籍爬虫
    '''
    def __init__(self, msg, start, end, total, base_path):
        '''
        初始化函数
        :param msg: 查询内容
        :param start: 起始页码
        :param end: 结束页码
        :param total: 查询总量
        :param base_path: 绝对根路径
        '''
        self.msg = msg
        self.start = start
        self.end = end
        self.total = total
        self.base_path = base_path
        self.urls_queue = Queue()
        self.htmls_queue = Queue()
        self.msg_li_queue = Queue()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
        }
        print(self.msg, self.start, self.end, self.total, self.base_path)
        print('初始化函数')
        pass

    def make_urls_queue(self):
        '''
        创建访问路径列表
        :return: None
        '''
        base_url = 'https://search.jd.com/Search?keyword=python&enc=utf-8&qrst=1&rt=1&stop=1&spm=2.1.1&vt=2&page=%d&click=0'
        for i in range(self.start, self.end):
            page_num = i
            url = base_url % page_num
            pass
            url_name = self.msg + str(page_num)
            self.urls_queue.put((url, url_name))


    def get_htmls_queue(self):
        '''
        访问页面并得到页面队列
        :return: None
        '''
        while True:
            if self.urls_queue.empty():
                break
            url, url_name = self.urls_queue.get()
            print('开始访问页面', url)
            resp = requests.get(url=url, headers=self.headers)
            resp.encoding = 'utf-8'
            html_info = resp.text
            # 对缺失的标签进行添加
            soup = BeautifulSoup(html_info, 'html.parser')
            fixed_html = soup.prettify()
            html_name = url_name
            self.htmls_queue.put((fixed_html, html_name))
            self.urls_queue.task_done()
            time.sleep(3 + random.random())

    def get_msg_li_queue(self):
        '''
        获得页面信息队列
        :return: None
        '''
        while True:
            if self.htmls_queue.empty() and self.urls_queue.empty():
                break
            html, html_name = self.htmls_queue.get()
            file_name = self.base_path + '/htmls/' + html_name + '.html'
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write(html)
                print(html_name, '保存完毕.')
            # css 选择器
            tree = lxml.html.fromstring(html)
            # 查找id为ss的li标签 下面 class 为dd的span标签
            li_list = tree.cssselect('li[class=gl-item]')
            li_list_name = html_name
            print('查找到序列元素如下：')
            print(len(li_list), li_list_name)
            self.msg_li_queue.put([li_list, li_list_name])
            self.htmls_queue.task_done()
            
    def deal_msg_li_queue(self):
        '''
        处理 列表信息队列
        :return: 
        '''
        while True:
            if self.msg_li_queue.empty() and self.htmls_queue.empty() and self.urls_queue.empty():
                break
            if self.msg_li_queue.empty():
                time.sleep(4)
                continue
            li_list, li_list_name = self.msg_li_queue.get()
            for li in li_list:
                # 获取图片元素和网址
                image_url_element = li.cssselect('div.p-img > a > img')[0]
                print(image_url_element.get('source-data-lazy-img'))
                # 获取价格元素和价值参数
                price_element = li.cssselect('div.p-price > strong > i')[0]
                print(price_element.text.strip())
                # 获取书名元素和书名参数
                name_element = li.cssselect('div.p-name > a > em')[0]
                print(name_element.text)
            self.msg_li_queue.task_done()
        pass

    def run(self):
        '''
        运行函数
        :return: None
        '''
        print('爬虫对象运行')
        self.make_urls_queue()
        self.get_htmls_queue()
        self.get_msg_li_queue()
        self.deal_msg_li_queue()
        pass


if __name__ == '__main__':
    msg = '爬虫'
    start = 1
    end = 2
    total = 0
    base_path = r'C:\PycharmProjects\spider\spiders\jingdong'
    params = {
        'msg': msg,
        'start': start,
        'end': end,
        'total': total,
        'base_path': base_path,
    }
    jing_dong_book_spider = JingDongBookSpider(**params)
    jing_dong_book_spider.run()
