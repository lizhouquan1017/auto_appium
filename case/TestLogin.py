# -*- coding:utf-8 -*-
__author__ = "lizhouquan"

import unittest
import logging
import allure
from base.BaseDriver import BaseDriver
from PO.business.login import LoginBusiness


# class TestLogin(unittest.TestCase):
@allure.feature("登录后操作")
class TestLogin():

    # def setUp(self):
    #     b = BaseDriver()
    #     self.driver = b.start_driver()
    #     self.imgs = []

    @allure.story("登录-下一步")
    def test_one(self,login):
        try:
            # db_driver = LoginBusiness(self.driver)
            self.driver = login
            l = LoginBusiness(self.driver)
            l.enter_login()
            # self.imgs.append(self.driver.get_screenshot_as_base64())
            # self.assertTrue(self.driver.check_status())
            flag = l.check_status()
            assert flag
            # self.imgs.append(self.driver.get_screenshot_as_base64())
            logging.info(r'success')

        except Exception as e:
            # self.imgs.append(self.driver.get_screenshot_as_base64())
            logging.error(r'fail'+str(e))

    # def tearDown(self):
    #     self.driver.quit()

