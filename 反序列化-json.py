#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
f = open('test.txt', 'r')
# data = eval(f.read()) 基本弃用
data = json.loads(f.read())
print(data)
