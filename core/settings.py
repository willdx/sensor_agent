# -*- coding: utf-8 -*-
'''
File Name: core/settings.py
Author: WillDX
mail: xiang.dai@shuyun.com
Created Time: 2016年04月18日 星期一 17时55分27秒
'''
import os
import sys

#传感器版本
agent_version="0.0.1"

#config.ini文件路径
sensor_path = os.path.split(os.path.abspath(sys.argv[0]))[0]
config_file = "%s/core/config.ini" % sensor_path

#传感器获取信息模型
##注释:
##现在的idc和resource_group信息是通过初始化写入配置文件的方式写入的
##如果需要修改数据来源可以更改core/res_format.py下的idc和resource_group函数

host_output = {
    "innerip":"",
    "hostname":"",    
    "idc":"", 
    "resource_group":"",    
    "resource_type":"",
    "status":"",
    "disk_size":"",    
    "disk_type":"",
    "version":"",
    "is_valid":"",    
    "last_time":"",
    "mac":"",
}

#传感器额外参数文本位置
custom_param_file = "./sensor_custom_args.ini" 

#传感器信息条目默认状态
agent_status = "online"

#传感器信息条目有效性
agent_is_valid = True

#传感器调用频率,单位秒
sensor_rate = 900

#传感器标准输入
sensor_stdin = "/dev/null"

#传感器标准输出
sensor_stdout = "%s/log/sensor_stdout.log" % sensor_path

#传感器标准错误输出
sensor_stderr = "%s/log/sensor_stderr.log" % sensor_path

#传感器server接口地址
sensor_server_url = "http://gw.api.fenxibao.com/sensor/postdata"

#传感器server授权Token
auth_token = ""

#是否开启守护进程运行
daemon = False
