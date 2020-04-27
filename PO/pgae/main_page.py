# -*- coding:utf-8 -*-
__author__ = "lizhouquan"

import allure
from time import sleep

from PO.pgae.home_page import HomePage
from base.BaseOperation import BaseOperation
from base.BaseReadIni import ReadIni
from PO.pgae.login_page import LoginPage

efg = ReadIni(file_name='main_page.ini')


class MainPage(BaseOperation):

    @allure.step("进入登录页面")
    def to_login_page(self):
        self.click(efg.read_config("personal_center"))
        self.click(efg.read_config("login_success"))
        sleep(5)
        return LoginPage(self.driver)

    @allure.step("进入首页")
    def to_home_page(self):
        self.click(efg.read_config("main_page_button"))
        sleep(5)
        return HomePage(self.driver)
