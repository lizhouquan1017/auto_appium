# -*- coding:utf-8 -*-
__author__ = "lizhouquan"


import allure
import os
import sys
from util.readExcel import read_xlsx
from base.App import App
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

userconfig = read_xlsx(rootPath + '/data/user_lizhouquan.xlsx')


@allure.epic("云打印登录业务")
class TestLogin(object):

    def setup_method(self):
        self.login_page = App.start().to_login_page()

    def teardown_method(self):
        App.quit()

    @allure.story("验证码登录")
    @allure.severity("critical")
    def test_verifycode_login(self):
        flag1 = self.login_page.verify_login(phone=userconfig[0].get('phonenumber'),
                                             code=userconfig[0].get('code'), num=2, result=r"账号管理")
        flag2 = self.login_page.logout(num=2, result=r"欢迎回来")
        assert flag1 & flag2

    @allure.story("密码登录")
    @allure.severity("critical")
    def test_pwd_login(self):
        flag1 = self.login_page.pwd_login(phone=userconfig[0].get('phonenumber'),
                                          pwd=userconfig[0].get('password'), num=2, result=r"账号管理")
        flag2 = self.login_page.logout(num=2, result=r"欢迎回来")
        assert flag1 & flag2

    @allure.story("用户注销")
    @allure.severity("critical")
    def test_user_logged_off(self):
        flag1 = self.login_page.verify_login(phone=userconfig[0].get('phonenumber'),
                                             code=userconfig[0].get('code'), num=2, result=r"账号管理")
        flag2 = self.login_page.user_logged(num=2, result=r"欢迎回来")
        assert flag1 & flag2

    @allure.story("字体下载")
    @allure.severity("critical")
    def test_font_down(self):
        flag1 = self.login_page.verify_login(phone=userconfig[0].get('phonenumber'),
                                             code=userconfig[0].get('code'), num=2, result=r"账号管理")
        flag2 = self.login_page.font_down(num=3, font_name="竹石体")
        return flag1 & flag2

