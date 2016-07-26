#!/bin/bash
#coding=utf-8
echo "Will Kill sensor_agent.py"
ps -ef | grep sensor_agent.py | grep -v grep | awk '{print $2}' | xargs -n 1 kill -9
echo "Killed!"
