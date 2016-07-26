# -*- coding: utf-8 -*-
'''
File Name: res_format.py
Author: WillDX
mail: xiang.dai@shuyun.com
Created Time: 2016年04月18日 星期一 18时26分34秒
'''
import time
import json
import math
import commands
from core.handle_config import handle
from core.settings import config_file
from core.settings import custom_param_file
from core.settings import agent_status 
from core.settings import agent_is_valid 
from core.settings import agent_version 
from core.pyconfig import get_ip_address

host_comm = handle(config_file,"host_comm")

def innerip(funcname):
    """获取内网IP逻辑"""
    inner_ip = get_ip_address('eth0')
    return inner_ip

def hostname(funcname):
    """获取主机名逻辑"""
    comm = host_comm[funcname] 
    status, output = commands.getstatusoutput(comm)
    return output

def idc(funcname):
    """获取所属机房逻辑"""
    try:
        custom_args = handle(custom_param_file,"custom_args")
        return custom_args[funcname] 
    except Exception as e:
        print "[error]:",e
        return None

def resource_group(funcname):
    """获取资源归属逻辑"""
    try:
        custom_args = handle(custom_param_file,"custom_args")
        return custom_args[funcname] 
    except Exception as e:
        print "[error]:",e
        return None

def resource_type(funcname):
    """获取资源类型逻辑"""
    status,output = commands.getstatusoutput(host_comm["cpu"])
    cpu = "".join([str(int(output) + 1),"c"])
    status,output = commands.getstatusoutput(host_comm["mem"])
    mem = int(math.ceil(float(output)/1024/1024))
    mem = "".join([str(mem),"g"])
    return "_".join([cpu,mem])

def status(funcname):
    """获取主机默认状态逻辑"""
    return agent_status

def disk_size(funcname):
    """获取主机磁盘大小逻辑"""
    func_root = "_".join([funcname,"root"])
    func_data = "_".join([funcname,"data"])
    root_comm = host_comm[func_root]
    data_comm = host_comm[func_data]
    sta,root = commands.getstatusoutput(root_comm)
    try:
        sta,data = commands.getstatusoutput(data_comm)
    except IndexError as e:
        data = "null"
    size = "_".join([root,data])
    return size

def disk_type(funcname):
    """获取磁盘类型逻辑"""
    comm = host_comm[funcname] 
    status, output = commands.getstatusoutput(comm)
    str = "No volume groups found"
    if str in output:
        type = "normal"
    else:
        type = "lvm"
    return type

def version(funcname):
    """获取传感器版本逻辑"""
    return agent_version

def is_valid(funcname):
    """条目默认为True,表示可用"""
    return agent_is_valid

def last_time(funcname):
    """刷新时间"""
    t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    return t

def mac(funcname):
    """获取mac地址"""
    import uuid
    m=uuid.UUID(int = uuid.getnode()).hex[-12:]
    return ":".join([m[e:e+2] for e in range(0,11,2)])


