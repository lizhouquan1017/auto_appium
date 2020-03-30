# coding:utf-8
from appium import webdriver
import yaml
import logging.config
import os
from time import ctime
from base.BaseReadYaml import ReadYaml
PATH = (lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p)))
yaml.warnings({'YAMLLoadWarning': False})
log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../config/log.conf')
logging.config.fileConfig(log_file_path)
logger = logging.getLogger()


class BaseDriver(object):

    def start_driver(self):
            with open('../config/Ys.yaml', 'r', encoding='utf-8') as file:
                data = yaml.load(file)
                ry = ReadYaml()
                # devices = ry.get_value('user_info_0', 'deviceName')
                port = ry.get_value('user_info_0', 'port')
                desired_caps = {}
                desired_caps['platformName'] = data['platformName']
                desired_caps['platformVersion'] = data['platformVersion']
                # desired_caps['deviceName'] = devices
                # desired_caps['app'] = PATH('../app/vx.apk')
                desired_caps['appPackage'] = data['appPackage']
                desired_caps['appActivity'] = data['appActivity']
                desired_caps['noReset'] = "True"
                desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
                desired_caps['resetKeyboard'] = data['resetKeyboard']
                desired_caps['automationName'] = "uiautomator2"
                desired_caps['systemPort'] = port+8000
                udid = os.getenv('udid',None)
                if udid is not None:
                    desired_caps['udid'] = udid
                    print('udid is %s' %udid)
                driver = webdriver.Remote('http://127.0.0.1' + ':' + str(port) + '/wd/hub', desired_caps)
            return driver


if __name__ == '__main__':
    b = BaseDriver()
    driver = b.start_driver()
