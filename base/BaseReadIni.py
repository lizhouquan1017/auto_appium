# -*- coding: utf-8 -*-
__author__ = "lizhouquan"


import configparser
import os


class ReadIni(object):
    """
    默认读取页面元素
    @file_name:文件名称
    """

    def __init__(self, isconfig=False, file_name=None):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        if isconfig:
            file_path = os.path.join(base_dir + r'/config/' + file_name)
            self.cfg = configparser.ConfigParser()
            self.cfg.read(file_path)
        else:
            file_path = os.path.join(base_dir + r'/page/' + file_name)
            self.cfg = configparser.ConfigParser()
            self.cfg.read(file_path)

    def read_config(self, para1, para2="value"):
        """
        @para1: 配置文件模块
        @para2: 配置文件子模块
        @return:data 子模块内容
        """
        data = self.cfg.get(para1, para2)
        return data


if __name__ == '__main__':
    page = ReadIni(file_name="home_page.ini")
    value = page.read_config("phone_number_input")
    print(value)
