# -*- coding:utf-8 -*-
__author__ = "lizhouquan"
import allure
from base.BaseOperation import BaseOperation
from base.BaseReadIni import ReadIni
from time import sleep

efg = ReadIni(file_name='login_page.ini')

@allure.feature("云打印登录业务")
class LoginPage(BaseOperation):

    # 下面为业务操作流
    # 验证码登录步骤
    @allure.step("点击我的")
    def click_personal_center(self, num=0):
        self.click(efg.read_config("personal_center"))
        sleep(num)

    @allure.step("点击密码tab")
    def click_pwd_tab(self, num=0):
        self.click(efg.read_config("pwd_tab"))
        sleep(num)

    @allure.step("点击跳转登录页面")
    def click_login_page(self, num=0):
        self.click(efg.read_config("login_success"))
        sleep(num)

    @allure.step("点击验证码tab")
    def click_verify_tab(self, num=0):
        self.click(efg.read_config("verify_tab"))
        sleep(num)

    @allure.step("输入手机号")
    def input_phone(self, phone=None, num=0):
        self.type(efg.read_config("login_phone_input"), phone)
        sleep(num)

    @allure.step("输入验证码")
    def input_verify_code(self, code=None, num=0):
        self.type(efg.read_config("verify_code_input"), code)
        sleep(num)

    @allure.step("输入密码")
    def input_pwd(self, pwd=None, num=0):
        self.type(efg.read_config("pwd_input"), pwd)
        sleep(num)

    @allure.step("点击登录")
    def click_login_button(self, num=0):
        self.click(efg.read_config("login_button"))
        sleep(num)

    @allure.step("点击设置")
    def click_setting_button(self, num=0):
        self.click(efg.read_config("setting_button"))
        sleep(num)

    @allure.step("点击退出")
    def click_logout_button(self, num=0):
        self.click(efg.read_config("logout_button"))
        sleep(num)

    @allure.step("点击弹框确认")
    def click_bounced_confirm(self, num=0):
        self.click(efg.read_config("bounced_confirm"))
        sleep(num)

    @allure.step("点击QQ第三方登录")
    def click_qq_login(self, num=0):
        self.click(efg.read_config("qq_login"))
        sleep(num)

    @allure.step("点击QQ授权按钮")
    def click_qq_authorization(self, num=0, text=None):
        xpath = "//*[@resource-id='"+efg.read_config("authorization_button")+"' and @text='"+text+"']"
        e = self.find_element_xpath(xpath)
        e.click()

    @allure.step("判断登录成功")
    def check_login_success(self, result=None, num=0):
        text = self.get_text(efg.read_config("login_title"))
        sleep(num)
        if result == text:
            return True
        else:
            return False

    @allure.step("判断退出成功")
    def check_logout_success(self, result=None, num=0):
        text = self.get_text(efg.read_config("login_title"))
        sleep(num)
        if result == text:
            return True
        else:
            return False

    # 验证码登录
    def verify_login(self, phone, code, num, result=None):
        # self.click_personal_center(num)
        # self.click_login_page(num)
        self.click_verify_tab(num)
        self.input_phone(phone, num)
        self.input_verify_code(code, num)
        self.click_login_button(num)
        flag = self.check_login_success(result=result)
        return flag

    # 密码登录
    def pwd_login(self, phone, pwd, num, result=None):
        # self.click_personal_center(num)
        # self.click_login_page(num)
        self.click_pwd_tab(num)
        self.input_phone(phone, num)
        self.input_pwd(pwd, num)
        self.click_login_button(num)
        flag = self.check_login_success(result=result)
        return flag

    # 第三方QQ登录
    def qq_login(self, num, text="授权并登录", result=None):
        # self.click_personal_center(num)
        # self.click_login_page(num)
        self.click_verify_tab(num)
        self.click_qq_login(num)
        self.click_qq_authorization(10, test=text)
        flag = self.check_login_success(result=result)
        return flag

    # 退出登录
    def logout(self, num, result=None):
        self.click_personal_center(num)
        self.click_setting_button(num)
        self.click_logout_button(num)
        self.click_bounced_confirm(num)
        flag = self.check_logout_success(result=result)
        return flag



