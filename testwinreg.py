#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
import os
os.chdir(os.getcwd())
print(os.getcwd())
# subprocess.run('dir', shell=True)
cmd = os.listdir(os.getcwd())
for i in cmd:
    print(i)
