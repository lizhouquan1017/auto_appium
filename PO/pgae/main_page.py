# -*- coding:utf-8 -*-
__author__ = "lizhouquan"

import allure
from time import sleep
from base.BaseOperation import BaseOperation
from base.BaseReadIni import ReadIni
from PO.pgae.login_page import LoginPage

efg = ReadIni(file_name='login_page.ini')


class MainPage(BaseOperation):

    @allure.step("进入登录页面")
    def to_login_page(self):
        sleep(5)
        self.click(efg.read_config("personal_center"))
        self.click(efg.read_config("login_success"))
        return LoginPage(self.driver)
