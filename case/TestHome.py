# -*- coding:utf-8 -*-
__author__ = "lizhouquan"

import allure

from base.App import App
from util.readExcel import read_xlsx
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

# userconfig = read_xlsx(rootPath + '/data/user_lizhouquan.xlsx')


@allure.epic("云打印冒烟测试")
class TestHome(object):

    def setup_method(self):
        self.home_page = App.start().to_home_page()

    def teardown_method(self):
        App.quit()

    @allure.story("连接蓝牙")
    @allure.severity("critical")
    def test_device_connection(self):
        flag = self.home_page.bluetooth_connection(num=3, hardware_series_name=r"B21",
                                                   device_name=r"B21-C1176202", connection_name=r"B21")
        assert flag
