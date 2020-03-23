# -*- coding:utf-8 -*-
__author__ = "lizhouquan"

import unittest
import logging
from base.BaseDriver import BaseDriver
from PO.business.demo import DemoBusiness


class TestDemo(unittest.TestCase):

    def setUp(self):
        b = BaseDriver()
        self.driver = b.start_driver()
        self.imgs = []

    def test_one(self):
        try:
            db_driver = DemoBusiness(self.driver)
            db_driver.enter_login()
            self.imgs.append(self.driver.get_screenshot_as_base64())
            self.assertTrue(db_driver.check_status())
            self.imgs.append(self.driver.get_screenshot_as_base64())
            logging.info(r'success')

        except Exception as e:
            self.imgs.append(self.driver.get_screenshot_as_base64())
            logging.error(r'fail'+str(e))

    def tearDown(self):
        self.driver.quit()

