#传感器sensor_agent

##版本

    version:0.0.1

##功能
    
    收集线上数据，发送到sensor_server的rest_api接口, server端负责数据的处理；最终保证CMDB数据的完整性;


##配置信息

1.配置文件路径

    core/settings.py

2.传感器获取信息模型

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
    }

3.处理逻辑

    在配置文件core/settings.py的host_output信息模型中设定需要获取的参数名称,并在core/res_format.py中定义同名处理函数;

##添加额外监控项 

例如:获取mac地址 

1.添加信息模型
    
    vim core/settings.py 

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
    "mac":"", #ADD
    }

2.添加同名处理函数

    vim core/res_format.py
    
    def mac(funcname):
        """获取mac地址"""
        import uuid
        m=uuid.UUID(int = uuid.getnode()).hex[-12:]
        return ":".join([m[e:e+2] for e in range(0,11,2)])

3.再次执行
    
    $ python sensor_agent.py

    [执行时间]: 2016-07-26 10:59:38
    [获取数据]: {
      "status": "online",
      "version": "0.0.1",
      "resource_group": "ops",
      "mac": "00:16:3e:00:0d:de", #获取到的mac地址
      "disk_type": "normal",
      "innerip": "10.153.195.80",
      "last_time": "2016-07-26 10:59:38",
      "disk_size": "20G_493G",
      "hostname": "ops-dev-01",
      "is_valid": true,
      "idc": "JST",
      "resource_type": "4c_4g"
    }

##上线前开始守护进程方式运行agent

    vim core/settings.py
    daemon = True

##提交到指定的sensor_server(server端需要另外搭建)
    
    #传感器server接口地址
    sensor_server_url = "http://gw.api.fenxibao.com/sensor/postdata"

    #传感器server授权Token
    auth_token = "xxxxxxxxxxx"

    
