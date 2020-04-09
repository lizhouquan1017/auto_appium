# coding:utf-8
import allure
from base.BaseOperation import BaseOperation
from base.BaseReadIni import ReadIni
from time import sleep


@allure.feature("WeCat登录业务")
class LoginBusiness(BaseOperation):

    def __init__(self, driver):
        super(LoginBusiness, self).__init__(driver)
        self.efg = ReadIni(file_name='demo_page.ini')

    # 下面为业务操作流
    # 输入电话号码
    @allure.step("登录")
    def enter_login(self):
        sleep(5)
        print('点击登录')
        self.click(self.efg.read_config(r'login_button'))

    @allure.step("登录结果判断")
    def check_status(self):
        print('判断登录成功')
        flag = self.is_exists(self.efg.read_config(r'next_step'))
        return flag
