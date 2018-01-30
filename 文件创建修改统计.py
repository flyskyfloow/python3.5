#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import glob
import time
import logging

logging.basicConfig(filename='mvfile.log', level=logging.INFO)
list_file = glob.glob("/hd2/share/public/*")


def getmtime(x):
    return time.localtime(os.stat(x).st_mtime)[0]


list2 = filter(lambda x: getmtime(x) < 2013, list_file)
for i in list2:
    #       print  i + "=====================" + str(getmtime(i))
    os.system("mv " + i + " /mnt/storagesdd/public/")
    #       print("mv " +  i + " /mnt/storagesdd/public/")
    logging.info("***************" + time.strftime('%Y-%m-%d', time.localtime(time.time())) + "********************")
    logging.info("mv " + i + " /mnt/storagesdd/public/")
