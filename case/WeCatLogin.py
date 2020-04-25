# -*- coding:utf-8 -*-
__author__ = "lizhouquan"

from PO.business.WeCatLogin import WeCatLoginBusiness
from base.BaseDriver import BaseDriver
from util.readExcel import read_xlsx
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

# userconfig = read_xlsx(rootPath + '/data/user_lizhouquan.xlsx')


class TestWeCatLogin(object):

    def setup_method(self):
        print("启动方法")
        self.driver = BaseDriver().start_driver()
        self.driver.launch_app()

    def teardown_method(self):
        print("结束方法")
        self.driver.close_app()

    def test_verifycode_login1(self):
        w = WeCatLoginBusiness(self.driver)
        w.enter_login()
        flag = w.check_status()
        assert flag

    def test_verifycode_login2(self):
        w = WeCatLoginBusiness(self.driver)
        w.enter_login()
        flag = w.check_status()
        assert flag
