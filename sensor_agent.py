# -*- coding: utf-8 -*-
'''
File Name: sensor_agent.py
Author: WillDX
mail: xiang.dai@shuyun.com
Created Time: 2016年04月18日 星期一 17时22分05秒
'''
import time
import json
from core.settings import *
from core.daemon import daemonize
from core.post_data import http_post

def format(filename,funcname):
    dir = __import__('core.'+filename)
    module = getattr(dir, filename)
    func = getattr(module, funcname)
    return func(funcname)

def main():
    """启动传感器程序"""
    while True:
        filename = "res_format"
        data = host_output
        for k,v in host_output.items(): 
            res = format(filename,k)
            #print "函数:[%s]-执行结果:[%s]" % (k,res)
            data[k]=res
        t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
        print "[执行时间]:",t
        print "[获取数据]:",
        print(json.dumps(data,indent=2,ensure_ascii=False))
        data=json.dumps(data)
        try:
            res = http_post(data) 
            print "[Post接口返回]:",res
        except Exception as e:
            print "[error]:",e
        time.sleep(sensor_rate)

if __name__=="__main__":
    if daemon:
        daemonize(sensor_stdin,sensor_stdout,sensor_stderr)
        main()
    else:
        main()




