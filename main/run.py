# -*- coding:utf-8 -*-

import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import unittest
from util.HTMLTestRunnerSimple import HTMLTestRunner
from util.email import send_email
from base.BaseAppiumServer import Server
from base.BaseAdb import AndroidDebugBridge
import time
import logging



devices = AndroidDebugBridge().attached_devices()
s = Server()
s.start_appium_server(devices)

time.sleep(10)

test_dir = rootPath+'/case'
report_dir = rootPath+'/reports'

discover = unittest.defaultTestLoader.discover(test_dir, pattern='demo.py')

now = time.strftime('%Y-%m-%d %H_%M_%S')
report_name = report_dir+'/'+now+' test_report.html'

with open(report_name, 'wb') as f:
    runner = HTMLTestRunner(stream=f, title='Demo Test Report', description='Demo Android app test report')
    logging.info('start run test case...')
    runner.run(discover)

# send_email()
