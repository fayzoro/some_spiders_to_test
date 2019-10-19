#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   selenium_search.py    
@Contact :   625711951@qq.com
@License :   (C)Copyright 2019-2020, Zyf-FT

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/10/19 16:45   zyfei      1.0         None
'''
from selenium import webdriver


def main():
    driver = webdriver.Firefox()
    driver.get('http://example.webscraping.com/search')
    driver.find_element_by_id('search_term').send_keys('.')
    driver.execute_script("document.getElementById('page_size').options[1].text = '1000'");
    driver.find_element_by_id('search').click()
    driver.implicitly_wait(30)
    links = driver.find_elements_by_css_selector('#results a')
    countries = [link.text for link in links]
    driver.close()
    print(countries)


if __name__ == '__main__':
    main()
