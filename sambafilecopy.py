#!/usr/bin/env python
# -*- coding: utf-8 -*
import os
import glob
import zipfile
# 100 gs文件解压路径 filepathzip
sourcegszip = "Z:\\GS"
# 指定的解压位置
filepathzipdir = "D:\\GS\\"
os.chdir(sourcegszip)
path = os.listdir()
pathlist = []
pathdiclist = {}
for i in path:
    if os.path.isfile(i):
        if "zip" in i:
            pathdiclist.update({int(os.path.getctime(i)): i})
            pathlist.append(int(os.path.getctime(i)))
    else:
        pass
        # print("gs 文件不存在")
newfile = filepathzipdir + (pathdiclist[max(pathlist)])
sourcegszipfile = sourcegszip + "\\" + pathdiclist[max(pathlist)]
# 解压文件到目标文件
f = zipfile.ZipFile(sourcegszipfile)
f.extractall(filepathzipdir)
f.close()
print(newfile)
