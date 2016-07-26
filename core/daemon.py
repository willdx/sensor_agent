# -*- coding: utf-8 -*-
'''
File Name: core/daemon.py
Author: WillDX
mail: xiang.dai@shuyun.com
Created Time: 2016年04月19日 星期二 17时54分52秒
'''
import os 
import sys

def daemonize (stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
     #重定向标准文件描述符
    try: 
        pid = os.fork() 
        #会话头领进程退出,意味着一个非会话组头领进程永远不能重新获得控制终端
        if pid > 0:
            sys.exit(0)   #父进程退出
    except OSError, e: 
        sys.stderr.write ("fork #1 failed: (%d) %s\n" % (e.errno, e.strerror) )
        sys.exit(1)

    #从母体环境脱离
    os.chdir("/") #chdir确认进程不保持任何目录于使用状态，否则不能umount一个文件系统
    os.umask(0) #调用umask(0)以便拥有对于写的任何东西的完全控制，因为有时不知道继承了什么样的umask
    os.setsid() #setsid调用成功后，进程成为新的会话组长和新的进程组长，并与原来的登录会话和进程组脱离

    #执行第二次fork
    try: 
        pid = os.fork() 
        if pid > 0:
            #第二个父进程退出
            sys.exit(0)
    except OSError, e: 
        sys.stderr.write ("fork #2 failed: (%d) %s\n" % (e.errno, e.strerror) )
        sys.exit(1)

    #进程已经是守护进程了，重定向标准文件描述符
    for f in sys.stdout, sys.stderr: 
        f.flush()
    si = open(stdin, 'r')
    so = open(stdout, 'a+')
    se = open(stderr, 'a+', 0)
    #dup2函数原子化关闭和复制文件描述符
    os.dup2(si.fileno(), sys.stdin.fileno())    
    os.dup2(so.fileno(), sys.stdout.fileno())
    os.dup2(se.fileno(), sys.stderr.fileno())


