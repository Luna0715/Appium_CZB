# coding=utf-8
# @Time    : 2020/3/10 11:09 下午
# @Author  : 石岩
# @File    : test_firstpage.py
from common.czb_unittest import CZBUnitTest
from business_view.first_page_view import FirstPageView
import unittest


class TestFirstPage(CZBUnitTest):

    def test_login_phone(self):
        view = FirstPageView(self.driver)
        self.assertTrue(view.click_phone_login())


if __name__ == '__main__':
    unittest.main()
