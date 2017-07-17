#!/usr/bin/env python
# -*-coding:utf-8-*-
'''
Author : issac
date   : 2017/7/14 下午2:46
role   : Version Update
'''
import fire


class MainProgram(object):
    def __init__(self, abc):
        pass

    @staticmethod
    def run(cls_inst):
        if issubclass(cls_inst, MainProgram):
            fire.Fire(cls_inst)
        else:
            raise Exception('')

