#!/usr/bin/env python
# -*-coding:utf-8-*-
'''
Author : issac
date   : 2017/7/14 上午11:27
role   : Version Update
'''

import os

ROOT_DIR = os.path.dirname(__file__)

settings = dict(
    template_path=os.path.join(ROOT_DIR, "templates"),
    static_path=os.path.join(ROOT_DIR, "static"),
    debug=True,
    xsrf_cookies=False,
    cookie_secret='61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=',
    databases={
        'default': {
            'host': '106.14.175.183',
            'port': '3306',
            'user': 'chenkun',
            'pwd': '123',
            'name': 'issac_blog',
        }
    },
    redises={
        'default': {
            'host': '192.168.1.35',
            'port': 6379,
            'db': 3,
            'auth': True,
            'charset': 'utf-8',
            'password': 'Vmobel135791'
        }
    },
    app_name='issac_blog',
    blog_log_path=os.path.join(ROOT_DIR, 'logs', 'blog_log.log')
)
