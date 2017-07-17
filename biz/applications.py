#!/usr/bin/env python
# -*-coding:utf-8-*-
'''
Author : issac
date   : 2017/7/14 下午2:58
role   : Version Update
'''
from biz.handlers.index import blog_urls
from libs.commons.app_base import AppBase


class Application(AppBase):
    def __init__(self, **settings):
        urls = []
        urls.extend(blog_urls)
        super(Application, self).__init__(urls, **settings)


if __name__ == '__main__':
    pass
