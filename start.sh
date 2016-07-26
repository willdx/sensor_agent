#!/bin/bash
#coding=utf-8

basedir=$(cd "$(dirname "$0")"; pwd)
cd $basedir;python sensor_agent.py
echo "Start completed!"
