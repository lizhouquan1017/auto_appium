# -*- coding:utf-8 -*-
__author__ = "lizhouquan"

import allure
from PO.business.smoke import SomkeBusiness
from PO.business.login import LoginBusiness
from util.readExcel import read_xlsx
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

userconfig = read_xlsx(rootPath + '/data/user_lizhouquan.xlsx')


@allure.epic("云打印冒烟测试")
class TestSmoke(object):

    def setup_function(self, login):
        self.driver = login

    def teardown_function(self, login):
        self.driver = login
        self.driver.close_app("com.gengcon.android.jccloudprinter")


    @allure.story("连接蓝牙")
    @allure.severity("critical")
    def test_device_connection(self,login):
        self.driver = login
        s = SomkeBusiness(self.driver)
        flag = s.bluetooth_connection(num=3,hardware_series_name=r"B21", device_name=r"B21-C1176202",connection_name=r"B21")
        assert flag


    @allure.story("验证码登录")
    @allure.severity("critical")
    def test_verifycode_login(self,login):
        self.driver = login
        l = LoginBusiness(self.driver)
        flag1 = l.verify_login(phone=userconfig[0].get('phonenumber'), code=userconfig[0].get('code'), num=2, result=r"账号管理")
        flag2 = l.logout(num=2, result=r"欢迎回来")
        assert flag1 & flag2

    @allure.story("密码登录")
    @allure.severity("critical")
    def test_pwd_login(self,login):
        self.driver = login
        l = LoginBusiness(self.driver)
        flag1 = l.pwd_login(phone=userconfig[0].get('phonenumber'), pwd=userconfig[0].get('password'), num=2, result=r"账号管理")
        flag2 = l.logout(num=2, result=r"欢迎回来")
        assert flag1 & flag2

    @allure.story("第三方QQ登录")
    @allure.severity("critical")
    def test_qq_login(self,login):
        self.driver = login
        l = LoginBusiness(self.driver)
        flag1 = l.qq_login(num=2, result=r"账号管理")
        flag2 = l.logout(num=2, result=r"欢迎回来")
        assert flag1 & flag2
