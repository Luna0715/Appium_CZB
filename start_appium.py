# coding=utf-8
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_driver():
    desired_caps = {
        'platformName': 'Android',
        'deviceName': '127.0.0.1:62001',
        'app': '/Users/shiyan/Tools/mukewang.apk',
        'appWaitActivity': 'cn.com.open.mooc.index.splash.GuideActivity',
        'automationName': 'uiautomator2',
    }
    app_driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    time.sleep(10)
    return app_driver


# 获取屏幕的宽度和高度
def get_size():
    size = driver.get_window_size()
    width = size['width']
    height = size['height']
    return width, height


# 左滑
def swipe_left():
    x1 = get_size()[0] / 10 * 9
    y1 = get_size()[1] / 2
    x2 = get_size()[0] / 10
    driver.swipe(x1, y1, x2, y1)


# 右滑
def swipe_right():
    x1 = get_size()[0] / 10
    y1 = get_size()[1] / 2
    x2 = get_size()[0] / 10 * 9
    driver.swipe(x1, y1, x2, y1)


# 上滑
def swipe_up():
    y1 = get_size()[1] / 10 * 9
    x1 = get_size()[0] / 2
    y2 = get_size()[1] / 10
    driver.swipe(x1, y1, x1, y2)


# 下滑
def swipe_down():
    y1 = get_size()[1] / 10
    x1 = get_size()[0] / 2
    y2 = get_size()[1] / 10 * 9
    driver.swipe(x1, y1, x1, y2)


# 滑动
def swipe_on(direction):
    if direction == 'left':
        swipe_left()
    elif direction == 'right':
        swipe_right()
    elif direction == 'up':
        swipe_up()
    elif direction == 'down':
        swipe_down()


def go_login():
    driver.find_element_by_id('cn.com.open.mooc:id/tv_go_login').click()


def login():
    driver.find_element_by_id('cn.com.open.mooc:id/account_edit').send_keys('1002450926@qq.com')
    driver.find_element_by_id('cn.com.open.mooc:id/password_edit').send_keys('shiyan86534346')
    driver.find_element_by_id('cn.com.open.mooc:id/login').click()


# 猿问
def go_yuanwen():
    driver.find_elements_by_id('cn.com.open.mooc:id/iv_icon')[2].click()


# 切换webview
def go_webview():
    time.sleep(5)
    webview = driver.contexts
    print(webview)
    # for viw in webview:
    #     if 'WEBVIEW_cn.com.open.mooc' in viw:
    #         driver.switch_to.context(viw)
    #         break
    # driver.find_element_by_link_text('pp').click()
    # try:
    #     driver.find_element_by_id('cn.com.open.mooc:id/left_icon').click()
    # except Exception as e:
    #
    #     driver.switch_to.context(webview[0])
    #     driver.find_element_by_id('cn.com.open.mooc:id/left_icon').click()
    #     raise e


def go_next():
    ele = driver.find_element_by_xpath('//*[contains(@text,"java好学吗.??pp")]').click()
    ele.find_elements_by_class_name('android.widget.RelativeLayout')[2].click()


def go_toast():
    driver.find_element_by_id('cn.com.open.mooc:id/account_edit').send_keys('1002450926@qq.com')
    driver.find_element_by_id('cn.com.open.mooc:id/login').click()
    toast_element = ("xpath", "//*[contains(@text,'请输入密码')]")
    WebDriverWait(driver, 10, 0.1).until(EC.presence_of_element_located(toast_element))


driver = get_driver()
swipe_on('left')
swipe_on('left')
swipe_on('up')
time.sleep(1)
go_login()
time.sleep(1)
go_toast()
