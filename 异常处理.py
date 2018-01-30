#!/usr/bin/env python
# -*- coding: utf-8 -*-
data = {}
try:
    data['name']
# 方式1
except KeyError as e:
    print("没有这个key", e)
# except IndexError as e:
#     print('list 操作错误', e)
else:
    print('正常执行')
finally:
    print('无论结果如何都执行')
