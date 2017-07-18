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
    cookie_secret='随机生成uuid',
    databases={
        'default': {
            'host': '你的host',
            'port': '你的port',
            'user': '用户名',
            'pwd': '密码',
            'name': '你的博客',
        }
    },
    redises={
        'default': {
            'host': '你的host',
            'port': 6379,
            'db': 3,
            'auth': True,
            'charset': 'utf-8',
            'password': '密码'
        }
    },
    app_name='issac_blog',
    blog_log_path=os.path.join(ROOT_DIR, 'logs', 'blog_log.log')
)