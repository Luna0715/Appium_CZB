# coding=utf-8
# @Time    : 2020/3/9 4:33 下午
# @Author  : 石岩
import os
import time
import logging
from common.yaml_manager import YamlManager


class BaseView(object):

    def __init__(self, driver):
        self.driver = driver
        self.conf = YamlManager('../config/page_element.yaml').read()

    # 获取屏幕的宽度和高度
    def get_size(self):
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        return width, height

    # 左滑
    def swipe_left(self):
        x1 = self.get_size()[0] / 10 * 9
        y1 = self.get_size()[1] / 2
        x2 = self.get_size()[0] / 10
        self.driver.swipe(x1, y1, x2, y1)

    # 右滑
    def swipe_right(self):
        x1 = self.get_size()[0] / 10
        y1 = self.get_size()[1] / 2
        x2 = self.get_size()[0] / 10 * 9
        self.driver.swipe(x1, y1, x2, y1)

    # 上滑
    def swipe_up(self):
        y1 = self.get_size()[1] / 10 * 9
        x1 = self.get_size()[0] / 2
        y2 = self.get_size()[1] / 10
        self.driver.swipe(x1, y1, x1, y2)

    # 下滑
    def swipe_down(self):
        y1 = self.get_size()[1] / 10
        x1 = self.get_size()[0] / 2
        y2 = self.get_size()[1] / 10 * 9
        self.driver.swipe(x1, y1, x1, y2)

    # 滑动
    def swipe_on(self, direction):
        if direction == 'left':
            self.swipe_left()
        elif direction == 'right':
            self.swipe_right()
        elif direction == 'up':
            self.swipe_up()
        elif direction == 'down':
            self.swipe_down()

    def get_time(self):
        self.now = time.strftime("%Y-%m-%d %H-%M-%S")
        return self.now

    def get_screen_shot(self, module):
        time = self.get_time()
        image_file = os.path.dirname(os.path.dirname(__file__)) + "/screenshots/%s_%s.png" % (module, time)
        logging.info("get %s screenshot" % module)
        self.driver.get_screenshot_as_file(image_file)

    def is_element_exist(self, element):
        source = self.driver.page_source
        if element in source:
            return True
        else:
            return False


if __name__ == '__main__':
    pass
