# coding=utf-8
# @Time    : 2020/3/9 6:56 下午
# @Author  : 石岩
# @File    : base_czb_view.py
from selenium.webdriver.support.wait import WebDriverWait

from base_view.base_view import BaseView
from selenium.webdriver.support import expected_conditions as EC


class BaseCZBView(BaseView):

    def get_element(self, data):
        if data is not None:
            find_type = data['find_type']
            element_info = data['element_info']
            loc = [find_type, element_info]
            return WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located(tuple(loc)))
            # if find_type == 'id':
            #     return self.driver.find_element_by_id(element_info)
            # elif find_type == 'className':
            #     return self.driver.find_element_by_class_name(element_info)
            # else:
            #     return self.driver.find_element_by_xpath(element_info)
        else:
            return None

    def excute_element_action(self, *args):
        action_method = args[0]['operate_type']
        excute_method = getattr(self, action_method)
        excute_method(*args)

    def input(self, *args):
        """
        输入值
        """
        # key,value
        element = self.get_element(args[0])
        if element is None:
            return args[0], "元素没找到"
        element.send_keys(args[1])

    def on_click(self, *args):
        """
        元素点击
        """
        print(args[0])
        element = self.get_element(args[0])
        if element is None:
            return args[0], "元素没找到"
        element.click()
