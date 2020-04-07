# -*- coding:utf-8 -*-
__author__ = "lizhouquan"

import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import subprocess
import os
import platform
from util.getSystem import getsystemstr
from base.BaseAdb import AndroidDebugBridge
from base.BaseCheckPort import Port
from base.BaseReadYaml import ReadYaml
from util.operationFile import remove_file
from time import sleep


class Server(object):

    def creat_command_list(self, devices_list):
        p = Port()
        command_list = []
        appium_port_list = p.creat_port_list(4700, devices_list)
        bootstrap_prot_list = p.creat_port_list(4900, devices_list)
        for i in range(len(devices_list)):
            cmd = 'appium -a ' + '127.0.0.1' + ' -p ' + str(appium_port_list[i]) + ' -bp ' + \
                  str(bootstrap_prot_list[i])
            command_list.append(cmd)
            device = devices_list[i]
            bp = bootstrap_prot_list[i]
            port = appium_port_list[i]
            ReadYaml().write_data(i, device, bp, port)
        return command_list

    def start_appium_server(self, devices_list):
        self.close_appium_server()
        sleep(15)
        cmd = self.creat_command_list(devices_list)
        for i in range(len(cmd)):
            remove_file(rootPath+'/appium_log')
            subprocess.Popen(cmd[i], shell=True, stdout=open(rootPath+'/appium_log/'+str(i)+'.log', 'a'),
                             stderr=subprocess.STDOUT)

    def close_appium_server(self):
        system = getsystemstr()
        if system != 'Darwin':
            server_list = os.popen('tasklist | find "node.exe" ').readlines()
            if len(server_list) > 0:
                os.system('taskkill -F -PID node.exe')
        elif system == 'Darwin':
            cmd_find = 'lsof -i tcp:4700'
            result = os.popen(cmd_find)
            text = result.read()
            if text != "":
                pid = text.split()[10]
                print(pid)
                cmd_kill = 'kill -9 %s' % pid
                print(cmd_kill)
                os.popen(cmd_kill)


if __name__ == '__main__':

    devices = AndroidDebugBridge().attached_devices()
    s =Server()
    s.start_appium_server(devices)
