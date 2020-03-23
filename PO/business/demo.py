# coding:utf-8
import logging
from base.BaseOperation import BaseOperation
from base.BaseReadIni import ReadIni
from time import sleep


class DemoBusiness(BaseOperation):

    def __init__(self, driver):
        super(DemoBusiness, self).__init__(driver)
        self.efg = ReadIni(file_name='demo_page.ini')

    # 下面为业务操作流
    # 输入电话号码
    def enter_login(self):
        sleep(10)
        self.click(self.efg.read_config(r'login_button'))

    def check_status(self):
        flag = self.is_exists(self.efg.read_config(r'next_step'))
        return flag
