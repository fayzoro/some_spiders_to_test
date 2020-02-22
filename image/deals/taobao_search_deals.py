#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import time
import random
from selenium import webdriver
from bs4 import BeautifulSoup
import lxml.html
from queue import Queue


class TaoBaoSpider(object):
    '''
    taobao search spider
    '''
    def __init__(self, start, end, total, search_msg, base_path):
        '''
        chushihua
        :param start: start page
        :param end: end page
        :param total: sum total search source
        :param search_msg: the waiting for search message
        :param base_path: os's base path
        '''
        self.start = start
        self.end = end
        self.total = total
        self.search_msg = search_msg
        self.base_path = base_path
        opt = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=opt)
        self.urls_queue = Queue()
        self.htmls_queue = Queue()
        self.csvs_queue = Queue()

        pass

    def get_the_first_page(self):
        time.sleep(2)
        self.driver.get('https://www.tmall.com/')
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(2 + random.random())
        self.driver.implicitly_wait(10)
        html = self.driver.page_source
        file_html_name = self.base_path + '/htmls/tmall.com.html'
        with open(file_html_name, 'w', encoding='utf-8') as f:
            f.write(html)
            print(file_html_name, 'is saved!')
        file_img_name = self.base_path + '/images/tmall.com.png'
        self.driver.save_screenshot(file_img_name)
        print("tmall.com's screenshot is saved!")
        pass

    def get_the_first_search_page(self):
        '''
        the first search page source
        :return:
        '''
        input = self.driver.find_element_by_xpath('//*[@id="mq"]')
        input.send_keys('python')
        button = self.driver.find_element_by_xpath('//*[@id="mallSearch"]/form/fieldset/div/button')
        self.driver.execute_script("arguments[0].click();", button)
        time.sleep(2)
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        self.driver.implicitly_wait(10)
        file_html_name = self.base_path + '/htmls/' + self.search_msg + '_first_search.html'
        with open(file_html_name, 'w', encoding='utf-8') as f:
            f.write(self.driver.page_source)
        file_image_name = self.base_path + '/images/' + self.search_msg + '.png'
        self.driver.save_screenshot(file_image_name)
        pass

    def run(self):
        '''
        run function
        :return: None
        '''
        self.get_the_first_page()
        self.get_the_first_search_page()
        time.sleep(5)
        self.driver.close()
        pass


def main():
    start = 1
    end = 2
    total = 10
    search_msg = 'python'
    base_path = r'C:\PycharmProjects\spider\spiders\image'
    params = {
        'start': start,
        'end': end,
        'total': total,
        'search_msg': search_msg,
        'base_path': base_path,
    }
    taobao_spider = TaoBaoSpider(**params)
    taobao_spider.run()
    pass


if __name__ == '__main__':
    main()
