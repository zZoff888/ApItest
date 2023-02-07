# -*- coding:utf-8 -*-
"""
装饰器模块
"""

import os
import datetime
import functools

from Untils.public.log import logger


# 测试参数打印装饰器
def test_param_print():
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            func_name = func.__name__  # 获取测试函数名
            log = logger()
            log.info(f'开始执行用例：{func_name}')

            log.info('测试数据' + '*' * 50)
            for each in args[1:]:  # 打印所有测试数据
                log.info(each)
            log.info('*' * 58)

            start_time = datetime.datetime.now()
            log.info(f'执行时间：{start_time}')

            try:
                func(*args, **kwargs)  # 执行测试函数
            except Exception as ex:
                log.info(f'执行失败，错误信息：{ex}')

            end_time = datetime.datetime.now()
            log.info(f'结束时间：{start_time}，耗时：{(end_time - start_time).total_seconds()}s')
        return wrapper
    return decorator