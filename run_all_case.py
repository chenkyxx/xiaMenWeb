# -*- coding: utf-8 -*-
# @Time    : 2019/10/13 9:28
# @Author  : chenky
# @Email   : 842202171@qq.com
# @File    : run_all_case.py
# @Software: PyCharm
# @Project : xiaMenWeb

import unittest
import os
from BeautifulReport import BeautifulReport

from public import HTMLTestRunner_cn


def add_case(rule: str):
    case_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "testcase")
    discover = unittest.defaultTestLoader.discover(start_dir=case_path,
                                                   pattern=rule)
    return discover


def add_test_result(result_name: str, unittest_suit: unittest.suite.TestSuite)->None:
    result_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "testReport")
    f = open(result_path+result_name, "wb")
    run = HTMLTestRunner_cn.HTMLTestRunner(stream=f,
                                           description="详细测试结果",
                                           title="厦门邮轮旅客出行平台船票系统web自动化")
    run.run(unittest_suit)
    f.close()


def run_beautiful_report(discover):
    BeautifulReport(suites=discover).report(description="厦门邮轮旅客出行平台船票系统",
                                            filename="result",
                                            log_path="./result")

if __name__ == '__main__':
    a = add_case(rule="test*.py")
    run_beautiful_report(a)


