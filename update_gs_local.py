#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import glob
import zipfile
# 100 gs文件解压路径 filepathzip
sourcegszip1 = "Z:\\GS"
sourcegszip2 = "Z:\\GS\\GSInternalTestingVersion"
# 指定的解压位置
filepathzipdir1 = "D:\\GS\\"
filepathzipdir2 = "D:\\GS\\GSInternalTestingVersion\\"
sourcegszipfile1 = (max(glob.glob(sourcegszip1 + r'\*zip'), key=os.path.getctime))
sourcegszipfile2 = (max(glob.glob(sourcegszip2 + r'\*zip'), key=os.path.getctime))
# print(sourcegszipfile1.split("\\")[-1].replace('.zip', ''))


def unzip(filepathzipdir, sourcegszipfile):
    if not os.path.exists(filepathzipdir):
        os.mkdir(filepathzipdir)
    if (filepathzipdir + sourcegszipfile.split("\\")[-1].replace('.zip', '')) not in glob.glob(filepathzipdir + '*'):
        f = zipfile.ZipFile(sourcegszipfile)
        f.extractall(filepathzipdir)
        f.close()
        # print(sourcegszipfile)
        # print(glob.glob(filepathzipdir + '*'))

if __name__ == "__main__":
    unzip(filepathzipdir1, sourcegszipfile1)
    unzip(filepathzipdir2, sourcegszipfile2)
