# coding=utf-8
# @Time    : 2020/3/10 11:02 下午
# @Author  : 石岩
# @File    : czb_unittest.py
import unittest
import logging
from time import sleep

from common.get_driver import get_driver


class CZBUnitTest(unittest.TestCase):

    def setUp(self):
        logging.info('=====setUp=====')
        self.driver = get_driver()

    def tearDown(self):
        logging.info('=====tearDown=====')
        self.driver.quit()
