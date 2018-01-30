#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

info = {
    'name': 'guo',
    'age': 26
}

f = open('test.txt', 'w')
f.write(json.dumps(info))
f.close()
