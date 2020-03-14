# coding=utf-8
# @Time    : 2020/3/12 2:42 下午
# @Author  : 石岩
# @File    : run.py
import unittest
import sys
import time, logging
from common.HTMLTestReportCN import HTMLTestRunner
from common.send_email import smtp_email

path = '/Users/shiyan/Code/Appium_CZB/'
sys.path.append(path)

test_dir = '../test_case'
report_dir = '../reports'

discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_firstpage.py')
now = time.strftime('%Y-%m-%d %H_%M_%S')
report_name = report_dir + '/' + now + ' czb_report.html'

with open(report_name, 'wb') as f:
    runner = HTMLTestRunner(stream=f, title='Czb Test Report', description='Czb Android app test report', tester='石岩')
    logging.info('start run test case...')
    runner.run(discover)