# -*- coding:utf-8 -*-
__author__ = "lizhouquan"

import allure
from base.BaseOperation import BaseOperation
from base.BaseReadIni import ReadIni
from time import sleep


@allure.feature("冒烟测试")
class SomkeBusiness(BaseOperation):

    def __init__(self, driver):
        super(SomkeBusiness, self).__init__(driver)
        self.efg = ReadIni(file_name='home_page.ini')

    # 下面是业务代码
    # 下面是步骤
    @allure.step("点击蓝牙连接")
    def click_bluetooth(self, num=0):
        self.click(self.efg.read_config("bluetooth_connection"))
        sleep(num)

    @allure.step("点击切换硬件")
    def click_switch_hardware(self, num=0):
        self.click_text("切换硬件")
        sleep(num)

    @allure.step("选择B21系列")
    def choose_hardware_series(self, hardware_series_name=None, num=0):
        xpath = "//*[@resource-id='"+self.efg.read_config("hardware_series")+"' and @text='"+hardware_series_name+"']"
        print(xpath)
        e = self.find_element_xpath(xpath)
        e.click()
        sleep(num)

    @allure.step("选择连接打印机")
    def connection_device(self, device_name=None, num=0):
        xpath = "//*[@resource-id='"+self.efg.read_config("device_name")+"' and @text='"+device_name+"']/../android.widget.TextView"
        print(xpath)
        e = self.find_element_xpath(xpath)
        e.click()

    @allure.step("判断打印机是否连接")
    def check_device_connection(self, connection_name=None, num=0):
        v = self.get_text(self.efg.read_config("bluetooth_connection"))
        if v != connection_name:
            return False
        elif v == r"未连接":
            return False
        elif v == connection_name:
            return True
        else:
            return False

    # 蓝牙打印机
    def bluetooth_connection(self, num=3,hardware_series_name=None,device_name=None,connection_name=None):
        self.click_bluetooth(num=num)
        self.click_switch_hardware(num=num)
        self.choose_hardware_series(hardware_series_name=hardware_series_name,num=num)
        self.connection_device(device_name=device_name, num=num)
        flag = self.check_device_connection(connection_name=connection_name, num=10)
        return flag



