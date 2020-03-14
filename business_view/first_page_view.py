# coding=utf-8
# @Time    : 2020/3/9 11:45 下午
# @Author  : 石岩
# @File    : first_page_view.py
import time

from base_view.base_czb_view import BaseCZBView
import logging


class FirstPageView(BaseCZBView):

    def click_phone_login(self):
        logging.info('perform click_phone_login')
        self.excute_element_action(self.conf['FirstPage']['PhoneLoginButton'])
        time.sleep(1)
        if self.is_element_exist('本机号码一键登录') or self.is_element_exist('发送验证码'):
            logging.info('phone_login success!')
            return True
        else:
            logging.error('phone_login Fail!')
            return False
