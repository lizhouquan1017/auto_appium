# -*- coding:utf-8 -*-
__author__ = "lizhouquan"

import unittest
import logging
import allure
from base.BaseDriver import BaseDriver
from PO.business.login import LoginBusiness


@allure.epic("云打印登录业务")
class TestLogin(object):

    # def setUp(self):
    #     b = BaseDriver()
    #     self.driver = b.start_driver()
    #     self.imgs = []

    @allure.story("验证码登录")
    @allure.severity("critical")
    def test_verifycode_login(self,login):
        self.driver = login
        l = LoginBusiness(self.driver)
        l.verify_login(phone=r'15927169432', code=r'2583', num=2)
        flag1 = l.check_login_success(result=r'账号管理')
        l.logout(num=2)
        flag2 = l.check_logout_success(result=r'欢迎回来')
        assert flag1&flag2

    @allure.story("密码登录")
    @allure.severity("critical")
    def test_pwd_login(self,login):
        self.driver = login
        l = LoginBusiness(self.driver)
        l.pwd_login(phone=r'15927169432', pwd=r'a123456', num=2)
        flag1 = l.check_login_success(result=r'账号管理')
        l.logout(num=2)
        flag2 = l.check_logout_success(result=r'欢迎回来')
        assert flag1 & flag2

