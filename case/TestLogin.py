# -*- coding:utf-8 -*-
__author__ = "lizhouquan"

import unittest
import logging
import allure
from base.BaseDriver import BaseDriver
from PO.business.login import LoginBusiness

@allure.epic("云打印登录业务")
@allure.severity("normal")
class TestLogin(object):

    # def setUp(self):
    #     b = BaseDriver()
    #     self.driver = b.start_driver()
    #     self.imgs = []

    @allure.story("验证码登录")
    def test_verifycode_login(self,login):
        self.driver = login
        l = LoginBusiness(self.driver)
        l.verify_login(phone=15927169432, code=2583)
        flag = l.check_login_success(result=r'管理账号')
        assert flag
        if flag:
            logging.info(r'success')
        else:
            logging.info(r'fail')
