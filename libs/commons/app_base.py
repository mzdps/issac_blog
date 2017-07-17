#!/usr/bin/env python
# -*-coding:utf-8-*-
'''
Author : issac
date   : 2017/7/14 下午3:02
role   : Version Update
'''

from tornado import httpserver, ioloop
from tornado import options as tnd_options
from tornado.options import options, define
from tornado.web import Application as tornado_app

from libs.commons.logs import log

define("addr", default='0.0.0.0', help="run on the given ip address", type=str)
define("port", default=8000, help="run on the given port", type=int)


class AppBase(tornado_app):
    """ 定制 Tornado Application 集成日志"""

    def __init__(self, handlers=None, default_host="", transforms=None, **settings):
        tnd_options.parse_command_line()
        super(AppBase, self).__init__(handlers, default_host, transforms, **settings)
        http_server = httpserver.HTTPServer(self)
        http_server.listen(options.port, address=options.addr)
        self.io_loop = ioloop.IOLoop.instance()

    def start_server(self):
        """
        启动 tornado 服务
        :return:
        """
        try:
            log.info('server address: %(addr)s:%(port)d' % dict(addr=options.addr, port=options.port))
            log.info('web server start sucessfuled.')
            self.io_loop.start()
        except KeyboardInterrupt:
            self.io_loop.stop()
        except:
            import traceback
            log.error(traceback.format_exc())


if __name__ == '__main__':
    pass
