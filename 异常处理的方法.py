#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 捕获系统异常
# try:
#     raise ValueError
# except ValueError as t:
#     print("Exception caught")
# 捕获自定义异常类


class MyException(Exception):
    pass
try:
    raise MyException
except MyException:
    print(" MyException caught")
