#!/usr/bin/env python
# -*-coding:utf-8-*-
'''
Author : issac
date   : 2017/7/14 下午3:52
role   : Version Update
'''
import json
from datetime import datetime, timedelta

from tornado.web import RequestHandler

from libs.commons.error_base import NotAllowedError, NotFoundError, BadRequestError
from libs.commons.logs import log


def raise_http405_error():
    """ 引发 HTTP 405 异常 """
    raise NotAllowedError()


class BaseHandler(RequestHandler):
    """ HTTP Web 请求基类 """

    def get_current_user(self):
        pass

    def prepare(self):
        pass
        # ready = signal(const.REQUEST_START_SIGNAL)
        # ready.send(self)

    def get_int_arg(self, name, default=0):
        value = self.get_arg(name)
        if isinstance(value, int):
            return value
        if isinstance(value, str) and value.isdigit():
            return int(value)
        return default

    def get_datetime_arg(self, name, default=None):
        value = self.get_arg(name)
        if isinstance(value, datetime):
            return value
        if value and isinstance(value, str):
            try:
                ts = 0
                if value.isdigit():
                    ts = int(value)
                if self.__is_float(value):
                    ts = float(value)
                if ts > 0:
                    return datetime.utcfromtimestamp(ts) + timedelta(hours=8)
                return datetime.strptime(value, "%Y-%m-%d")
            except:
                return default
        if isinstance(value, (int, float)):
            return datetime.utcfromtimestamp(value) + timedelta(hours=8)
        return default

    def __is_float(self, value):
        try:
            float(value)
            return True
        except:
            return False

    def get_bool_arg(self, name, default=False):
        value = self.get_arg(name)
        if isinstance(value, bool):
            return value
        if value.lower() == 'true' or value == '1':
            return True
        return default

    def get_list_args(self, name):
        value = self.get_arg(name)
        if isinstance(value, (list, dict)):
            return value
        if value == '':
            return []
        return value.split(',')

    def get_arg(self, name, default=''):
        return self.get_argument(name, default)

    def handle_request(self, http_method, *args, **kwargs):
        resource = (kwargs['res'] if 'res' in kwargs else '').lower()
        self.resource_key = (kwargs['reskey'] if 'reskey' in kwargs else '')
        self.resource_key = self.resource_key.lower()
        if resource in ('get', 'put', 'delete', 'post', 'patch', 'options'):
            raise NotAllowedError()

        if resource:
            if http_method == 'options':
                res_method = 'options'
            else:
                method_dict = dict(method=http_method, res=resource)
                res_method = '%(method)s_%(res)s' % method_dict
            methods = dir(BaseHandler)
            if res_method in methods:
                raise NotAllowedError()
            self._method = res_method
        else:
            self._method = 'default_%(method)s' % dict(method=http_method)

        if hasattr(self, self._method.lower()):
            handler = getattr(self, self._method.lower(), raise_http405_error)
        else:
            raise NotFoundError()

        if self.request.body:
            log.info(self.request.body)
            body_content = json.loads(str(self.request.body, encoding='utf-8'))
        else:
            body_content = ''
        return handler()


class RestfulAPIHandler(BaseHandler):
    def __init__(self, application, request, **kwargs):
        self.content_type = ''
        super(RestfulAPIHandler, self).__init__(application, request, **kwargs)

    def get(self, *args, **kwargs):
        self.content_type = self.get_content_type()
        result = self.handle_request('get', *args, **kwargs)
        if result:
            self.set_header("Cache-Control", "no-cache, must-revalidate")
            self.set_header("Expires", "Mon, 00 Jul 1970 00:00:00 GMT")
            self.write(result)
        else:
            self.write({})

    def post(self, *args, **kwargs):
        if not self.request.body:
            raise BadRequestError(0, 'Post must give resource info.')
        self.content_type = self.get_content_type()
        result = self.handle_request('post', *args, **kwargs)
        if result:
            self.write(result)
        else:
            self.write({})

    def patch(self, *args, **kwargs):
        self.content_type = self.get_content_type()
        result = self.handle_request('patch', *args, **kwargs)
        if result:
            self.write(result)
        else:
            self.write({})

    def put(self, *args, **kwargs):
        if not self.request.body:
            raise BadRequestError(0, 'Post must give resource info.')
        self.content_type = self.get_content_type()
        result = self.handle_request('put', *args, **kwargs)
        if result:
            self.write(result)
        else:
            self.write({})

    def delete(self, *args, **kwargs):
        self.content_type = self.get_content_type()
        result = self.handle_request('delete', *args, **kwargs)
        if result:
            self.write(result)
        else:
            self.write({})

    def options(self, *args, **kwargs):
        self.content_type = self.get_content_type()
        result = self.handle_request('options', *args, **kwargs)
        if result:
            self.write(result)
        else:
            self.write({})

    def head(self, *args, **kwargs):
        self.content_type = self.get_content_type()
        result = self.handle_request('head', *args, **kwargs)
        if result:
            self.write(result)
        else:
            self.write({})

    def get_content_type(self):
        if 'Content-Type' in self.request.headers:
            content_type = self.request.headers['Content-Type'].lower()
        elif 'Accept' in self.request.headers:
            content_type = self.request.headers['Accept'].lower()
        elif 'content_type' in self.request.headers:
            content_type = self.request.headers['content_type'].lower()
        elif 'accept' in self.request.headers:
            content_type = self.request.headers['accept'].lower()
        else:
            return 'json'

        if 'xml' in content_type:
            return 'xml'
        if 'atom+xml' in content_type:
            return 'atom'

        return 'json'

    def write(self, chunk=None, message=None):
        if chunk is None:
            chunk = {}

        if message:
            chunk["notification"] = {"message": message}
        chunk = {"resp": chunk}
        super(RestfulAPIHandler, self).write(chunk)
