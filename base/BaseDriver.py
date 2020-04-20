# -*- coding:utf-8 -*-
__author__ = "lizhouquan"

import yaml
import sys
import os
from selenium.webdriver.common import utils
from appium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from base.BaseReadYaml import ReadYaml
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
yaml.warnings({'YAMLLoadWarning': False})


class BaseDriver(object):

    driver: WebDriver = None

    @classmethod
    def start_driver(cls):
            with open(rootPath+'/config/Ys.yaml', 'r', encoding='utf-8') as file:
                data = yaml.load(file)
                ry = ReadYaml()
                # port = ry.get_value('user_info_0', 'port')
                # port = utils.free_port()
                desired_caps = {}
                desired_caps['platformName'] = data['platformName']
                desired_caps['platformVersion'] = data['platformVersion']
                desired_caps['appPackage'] = data['appPackage']
                desired_caps['appActivity'] = data['appActivity']
                desired_caps['noReset'] = "True"
                desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
                desired_caps['resetKeyboard'] = data['resetKeyboard']
                desired_caps['automationName'] = "uiautomator2"
                desired_caps['noReset'] = True
                desired_caps['systemPort'] = utils.free_port()
                udid = os.getenv('udid',None)
                if udid is not None:
                    desired_caps['udid'] = udid
                    print('udid is %s' %udid)
                cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
                cls.driver.implicitly_wait(10)
            return cls.driver

    @classmethod
    def quit(cls):
        cls.driver.quit()


if __name__ == '__main__':
    b = BaseDriver()
    driver = b.start_driver()
