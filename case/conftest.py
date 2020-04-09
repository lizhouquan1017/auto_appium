# -*- coding:utf-8 -*-
__author__ = "lizhouquan"

import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import pytest
import time
from base.BaseDriver import BaseDriver
from PO.business.login import LoginBusiness



# @pytest.fixture(scope="session")
# def driver(request):
#     '''打开App'''
#     b = BaseDriver()
#     driver = b.start_driver()
#     # imgs = []
#
#
#     def end():
#         print("全部用例执行完后 teardown quit dirver")
#         time.sleep(5)
#         driver.quit()
#
#     request.addfinalizer(end)
#     return driver

@pytest.fixture(scope="session")
def login():
    b = BaseDriver()
    driver = b.start_driver()
    return driver
