#!/usr/bin/env python
# -*-coding:utf-8-*-
'''
Author : issac
date   : 2017/7/13 下午2:35
role   : Version Update
'''
from tornado.options import define

from biz.applications import Application as BlogAPP
from libs.commons.program import MainProgram
from settings import settings as app_settings

define("service", default='blog', help="start service flag", type=str)


class BlogProgram(MainProgram):
    def __init__(self, service='blog_issac', progressid=''):
        self.__app = None
        settings = app_settings

        if service == 'blog':
            self.__app = BlogAPP(**settings)
        super(BlogProgram, self).__init__(progressid)
        self.__app.start_server()


if __name__ == '__main__':
    MainProgram.run(BlogProgram)
