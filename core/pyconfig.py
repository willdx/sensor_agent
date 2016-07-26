# -*- coding: utf-8 -*-
'''
File Name: pyconfig.py
Author: WillDX
mail: xiang.dai@shuyun.com
Created Time: 2016年04月26日 星期二 09时17分34秒
'''

import socket
import fcntl
import struct
  
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])


if __name__=="__main__":
    print get_ip_address('lo')
    print get_ip_address('eth0')
