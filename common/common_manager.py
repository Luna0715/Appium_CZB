from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CommonManager(object):

    def __init__(self, driver):
        self.driver = driver

    def always_allow_v6_0_1(self, number=5):
        for i in range(number):
            loc = ('xpath', "//*[@text='允许']")
            try:
                e = WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located(loc))
                e.click()
            except:
                pass

    def always_allow_v10(self, number=5):
        for i in range(number):
            loc = ('xpath', "//*[@text='始终允许']")
            try:
                e = WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located(loc))
                e.click()
            except:
                pass
