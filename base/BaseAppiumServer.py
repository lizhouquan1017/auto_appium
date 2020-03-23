# -*- coding:utf-8 -*-
__author__ = "lizhouquan"

import subprocess
import os
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
            cmd = 'start /b appium -a ' + '127.0.0.1' + ' -p ' + str(appium_port_list[i]) + ' -bp ' + \
                  str(bootstrap_prot_list[i]) + ' -U ' + str(devices_list[i])
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
            remove_file('../appium_log')
            subprocess.Popen(cmd[i], shell=True, stdout=open('../appium_log/'+str(i)+'.log', 'a'),
                             stderr=subprocess.STDOUT)

    def close_appium_server(self):
        server_list = os.popen('tasklist | find "node.exe" ').readlines()
        if len(server_list) > 0:
            os.system('taskkill -F -PID node.exe')


if __name__ == '__main__':

    devices = AndroidDebugBridge().attached_devices()
    s = Server()
    # s.close_appium_server()
    s.start_appium_server(devices)
