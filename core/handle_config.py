# -*- coding: utf-8 -*-
'''
File Name: handle_config.py
Author: WillDX
mail: xiang.dai@shuyun.com
Created Time: 2016年04月19日 星期二 09时36分58秒
'''
import json
from ConfigParser import ConfigParser

def handle(configfile,item_name):
    #print "[configfile]:%s" % configfile
    cp = ConfigParser()
    cp.read(configfile)
    res = cp.items(item_name)
    #print "传感器获取资源项[%s]命令字典如下:" % item_name
    #print(json.dumps(dict(res),indent=2,ensure_ascii=False))
    return dict(res)

