#!/usr/bin/env python
# -*-coding:utf-8-*-
'''
Author : issac
date   : 2017/7/14 下午3:13
role   : Version Update
'''
from libs.commons.webhandlers import RestfulAPIHandler


class MainHandler(RestfulAPIHandler):
    def get_123(self):
        greeting = self.get_argument('greeting', 'Hello')
        return {'fa': 123}


blog_urls = [
    (r"/(?P<res>[0-9a-zA-Z\-_]+)\/?", MainHandler)
]

if __name__ == "__main__":
    pass
