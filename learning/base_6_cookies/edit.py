#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   edit.py    
@Contact :   625711951@qq.com
@License :   (C)Copyright 2019-2020, Zyf-FT

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/10/19 16:50   zyfei      1.0         None
'''

import urllib
import urllib.request
import mechanize
import login

COUNTRY_URL = 'http://example.webscraping.com/edit/United-Kingdom-239'



def edit_country():
    opener = login.login_cookies()
    country_html = opener.open(COUNTRY_URL).read()
    data = login.parse_form(country_html)
    import pprint; pprint.pprint(data)
    print('Population before: ' + data['population'])
    data['population'] = int(data['population']) + 1
    encoded_data = urllib.urlencode(data)
    request = urllib.request.Request(COUNTRY_URL, encoded_data)
    response = opener.open(request)

    country_html = opener.open(COUNTRY_URL).read()
    data = login.parse_form(country_html)
    print('Population after:', data['population'])



def mechanize_edit():
    """Use mechanize to increment population
    """
    # login
    br = mechanize.Browser()
    br.open(login.LOGIN_URL)
    br.select_form(nr=0)
    print(br.form)
    br['email'] = login.LOGIN_EMAIL
    br['password'] = login.LOGIN_PASSWORD
    response = br.submit()

    # edit country
    br.open(COUNTRY_URL)
    br.select_form(nr=0)
    print('Population before:', br['population'])
    br['population'] = str(int(br['population']) + 1)
    br.submit()

    # check population increased
    br.open(COUNTRY_URL)
    br.select_form(nr=0)
    print('Population after:', br['population'])


if __name__ == '__main__':
    edit_country()
    mechanize_edit()
