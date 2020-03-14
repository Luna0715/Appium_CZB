import os
import logging
import logging.config

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common.common_manager import CommonManager
from common.yaml_manager import YamlManager
from common.get_devices import get_devices

CON_LOG = '../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()


def get_driver():
    conf = YamlManager('../config/czb_caps.yaml').read()

    base_dir = os.path.dirname(os.path.dirname(__file__))
    app_path = os.path.join(base_dir, 'app', conf['Android']['appName'])
    conf['Android']['app'] = app_path

    # 设置deviceName
    if get_devices() is not None:
        conf['Android']['deviceName'] = get_devices()[0]

    desired_caps = conf['Android']
    logging.info('start app...')
    driver = webdriver.Remote(conf['Url'], desired_caps)
    conf = YamlManager('../config/page_element.yaml').read()
    CommonManager(driver).always_allow_v10()
    loc = ['id', conf['SplashPage']['KnownButton']['element_info']]
    WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located(tuple(loc))).click()
    return driver


if __name__ == '__main__':
    # driver = get_driver()
    # driver.implicitly_wait(8)
    # CommonManager(driver).always_allow_v10()
    # driver.find_element_by_id('com.czb.chezhubang:id/tv_center').click()
    # driver.implicitly_wait(8)

    conf = YamlManager('../config/page_element.yaml').read()
    loc = ['id', conf['SplashPage']['KnownButton']['element_info']]
    print(tuple(loc))
