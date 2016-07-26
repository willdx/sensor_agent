# -*- coding: utf-8 -*-
'''
File Name: post_data.py
Author: WillDX
mail: xiang.dai@shuyun.com
Created Time: 2016年04月21日 星期四 11时35分46秒
'''
import json
import urllib 
import urllib2 
from settings import auth_token
from settings import sensor_server_url

def http_post(data):
    """使用httplib实现HTTP POST数据"""
    Token = "Token %s" % auth_token
    url = sensor_server_url
    data = json.dumps(data)
    headers = {
        'content-type' : 'application/json' ,
        'charset' : 'utf-8',
        "Authorization": Token
        }
    req = urllib2.Request(url, data, headers )
    res = urllib2.urlopen(req)
    out = res.read().strip()
    return out

if __name__=="__main__":
    data = {
      "status": "online",
      "is_valid": True,
      "disk_type": "other",
      "disk_size": "20G_493G",
      "version": "0.0.1",
      "resource_group": "Aliyun-RDS",
      "hostname": "ops-dev-01",
      "innerip": "10.153.195.80",
      "idc": "JST",
      "resource_type": "4c_4g",
      "last_time": "2016-04-22 15:15",
    }
    res = http_post(data)
    print res

