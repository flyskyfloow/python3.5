#!/usr/bin/env python
# -*- coding: utf-8 -*-
import demjson
import json
data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}, {'guo': 502}]
# json = demjson.encode(data)
# print(json)
# print(type(data))
# print(type(json))
js = json.dumps(data)
print(js)
jsl = json.loads(js)
print(jsl[0]["d"])
print(type(data))
print(type(js))
