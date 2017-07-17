#!/usr/bin/env python
# -*-coding:utf-8-*-
'''
Author : issac
date   : 2017/7/17 上午10:33
role   : Version Update
'''


from libs.commons.enums import ErrorCode, IntEnum


class BaseError(Exception):
    """ 错误基类，所有错误必须从该类继承 """

    def __init__(self, errorcode, *args, **kwargs):
        """
        初始化错误基类
        :param errorcode: 错误码
        :param args:
        :param kwargs:
        """
        if isinstance(errorcode, IntEnum):
            self._errorcode = errorcode
            self.kwargs = kwargs
            super(BaseError, self).__init__(*args)
        else:
            raise TypeError(
                'Error code must be enums.ErrorCode type.')

    @property
    def errorcode(self):
        return self._errorcode


class BizError(BaseError):
    """ 业务错误 """

    def __init__(self, errorcode, *args, **kwargs):
        self.__subcode = int(args[1]) if len(args) > 1 else 0
        super(BizError, self).__init__(errorcode, *args, **kwargs)

    @property
    def subcode(self):
        """
        获取
        :return:
        """
        return self.__subcode


class ConfigError(BaseError):
    pass


class NetError(BaseError):
    """ 网络错误 """
    pass


class BadRequestError(BizError):
    """ 错误的请求 """

    def __init__(self, *args, **kwargs):
        super(BadRequestError, self).__init__(ErrorCode.bad_request,
                                              *args, **kwargs)


class NotFoundError(BizError):
    """ 资源未找到 """

    def __init__(self, *args, **kwargs):
        super(NotFoundError, self).__init__(ErrorCode.not_found,
                                            *args, **kwargs)


class UnAuthorizedError(BizError):
    """ 请求要求身份验证。 对于需要登录的网页，服务器可能返回此响应。 """

    def __init__(self, *args, **kwargs):
        super(UnAuthorizedError, self).__init__(ErrorCode.unauthorized,
                                                *args, **kwargs)


class ForbiddenError(BizError):
    """ 服务器拒绝请求 """

    def __init__(self, *args, **kwargs):
        super(ForbiddenError, self).__init__(ErrorCode.forbidden,
                                             *args, **kwargs)


class NotAllowedError(BizError):
    """ 请求中指定的方法已被禁用 """

    def __init__(self, *args, **kwargs):
        super(NotAllowedError, self).__init__(ErrorCode.not_allowed,
                                              *args, **kwargs)


class NotAcceptableError(BizError):
    """ 当前请求服务器无法接受 """

    def __init__(self, *args, **kwargs):
        super(NotAcceptableError, self).__init__(ErrorCode.not_acceptable,
                                                 *args, **kwargs)


class ConflictError(BizError):
    """ 服务在完成请求时发生冲突，需附带冲突资源 """

    def __init__(self, conflict_resource, *args, **kwargs):
        """
        服务在完成请求时发生冲突，需附带冲突资源
        :param conflict_resource: 发生冲突的资源
        :param args:
        :param kwargs:
        """
        self.conflict_resource = conflict_resource
        super(ConflictError, self).__init__(ErrorCode.conflict,
                                            *args, **kwargs)


class GoneError(BizError):
    """ 当前资源已被删除，无法访问 """

    def __init__(self, *args, **kwargs):
        super(GoneError, self).__init__(ErrorCode.gone, *args, **kwargs)


class PreconditionFailedError(BizError):
    """ 未满足执行的前提条件 """

    def __init__(self, *args, **kwargs):
        super(PreconditionFailedError, self).__init__(
            ErrorCode.precondition_failed, *args, **kwargs)


class RequestEntityTooLargeError(BizError):
    """ 请求内容太大 """

    def __init__(self, *args, **kwargs):
        super(RequestEntityTooLargeError, self).__init__(
            ErrorCode.request_entity_too_large, *args, **kwargs)


class UnsupportMediaType(BizError):
    """ 错误的资源类型 """

    def __init__(self, *args, **kwargs):
        super(UnsupportMediaType, self).__init__(
            ErrorCode.unsupport_media_type, *args, **kwargs)


class InternalServerError(BizError):
    """ 服务出现未知错误 """

    def __init__(self, *args, **kwargs):
        super(InternalServerError, self).__init__(
            ErrorCode.internal_server_error, *args, **kwargs)


class ServiceUnavailableError(BizError):
    """ 服务无法响应 """

    def __init__(self, *args, **kwargs):
        super(ServiceUnavailableError, self).__init__(
            ErrorCode.service_unavailable, *args, **kwargs)


class ServiceNotImplementedError(BizError):
    """ 服务尚未实现 """

    def __init__(self, *args, **kwargs):
        super(ServiceNotImplementedError, self).__init__(
            ErrorCode.service_not_implemented, *args, **kwargs)


class ConfigImportError(ConfigError):
    """ 配置导入错误 """

    def __init__(self, *args, **kwargs):
        super(ConfigImportError, self).__init__(
            ErrorCode.config_import_error, *args, **kwargs)


class ConfigNotFoundError(ConfigError):
    """ 找不到配置项错误 """

    def __init__(self, *args, **kwargs):
        super(ConfigNotFoundError, self).__init__(
            ErrorCode.config_item_notfound_error, *args, **kwargs)
