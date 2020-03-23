# -*- coding:utf-8 -*-

import unittest
from util.HTMLTestRunnerSimple import HTMLTestRunner
from util.email import send_email
from base.BaseAppiumServer import Server
from base.BaseAdb import AndroidDebugBridge
import time
import logging
import sys


devices = AndroidDebugBridge().attached_devices()
s = Server()
s.start_appium_server(devices)

time.sleep(15)

test_dir = '../case'
report_dir = '../reports'

discover = unittest.defaultTestLoader.discover(test_dir, pattern='demo.py')

now = time.strftime('%Y-%m-%d %H_%M_%S')
report_name = report_dir+'/'+now+' test_report.html'

with open(report_name, 'wb') as f:
    runner = HTMLTestRunner(stream=f, title='Demo Test Report', description='Demo Android app test report')
    logging.info('start run test case...')
    runner.run(discover)

# send_email()
