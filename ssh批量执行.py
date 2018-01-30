#!/usr/bin/env python
# -*- coding: utf-8 -*-
import paramiko
# 服务器账密列表
ciscoIpList = [
    ["192.168.1.161", "root", "gft123"],
    # ["192.168.1.12", "user", "passwd"]
]


def sshLogin(ip, user, passwd, commands):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, 22, user, passwd, timeout=5)
    with open(commands, "r") as f:
        for i in f.readlines():
            print(i)
            stdin, stdout, stderr = ssh.exec_command(i)
            print(stdout.read())
            print(stderr.read())
    ssh.close()
if __name__ == '__main__':
    # sshLogin("192.168.1.161", "root", "gft123", "test1.txt")
    for i in ciscoIpList:
        sshLogin(i[0], i[1], i[2], "test1.txt")
