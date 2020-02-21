#!/usr/bin/env python
# _*_ coding:utf-8 _*_


class JingDongSpiders(object):
    '''
    main function of jingdong spider
    '''
    def __init__(self, params):
        '''
        初始化函数
        :param params: 参数字典
        '''
        self.params = params
        pass

    def run(self):
        pass


if __name__ == '__main__':
    msg = '爬虫'
    start = 1
    end = 1
    total = 0
    base_path = r'C:\PycharmProjects\spider\spiders\jingdong'
    params = {
        'msg': msg,
        'start': start,
        'end': end,
        'total': total,
        'base_path': base_path,
    }
    jingdong_spider = JingDongSpiders(params)
    jingdong_spider.run()
