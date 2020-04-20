# coding:utf-8
import allure
from base.BaseOperation import BaseOperation
from base.BaseReadIni import ReadIni
from time import sleep


@allure.feature("云打印登录业务")
class LoginBusiness(BaseOperation):

    def __init__(self, driver):
        super(LoginBusiness, self).__init__(driver)
        self.efg = ReadIni(file_name='login_page.ini')

    # 下面为业务操作流
    # 验证码登录步骤
    @allure.step("点击我的")
    def click_personal_center(self):
        self.click(self.efg.read_config("personal_center"))
        sleep(3)

    @allure.step("点击跳转登录页面")
    def click_login_page(self):
        self.click(self.efg.read_config("login_success"))
        sleep(3)

    @allure.step("点击验证码tab")
    def click_verift_tab(self):
        self.click(self.efg.read_config("verify_tab"))
        sleep(3)

    @allure.step("输入手机号")
    def input_phone(self, phone):
        self.type(self.efg.read_config("login_phone_input"), phone)
        sleep(3)

    @allure.step("输入验证码")
    def input_verify_code(self, code):
        self.type(self.efg.read_config("verify_code_input"), code)
        sleep(3)

    @allure.step("点击登录")
    def click_login_button(self):
        self.click(self.efg.read_config("login_button"))
        sleep(3)

    @allure.step("判断登录是否成功")
    def check_login_success(self, result):
        text = self.get_text(self.efg.read_config("login_title"))
        sleep(3)
        if result == text:
            return True
        else:
            return False

    def verify_login(self, phone, code):
        self.click_personal_center()
        self.click_login_page()
        self.input_phone(phone)
        self.input_verify_code(code)
        self.click_login_button()
