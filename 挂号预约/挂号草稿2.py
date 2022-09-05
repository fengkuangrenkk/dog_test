from idlelib import browser
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from xml import etree
# 显示等待
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
# 键盘事件
from selenium.webdriver.common.keys import Keys
# 鼠标事件
from selenium.webdriver.common.action_chains import ActionChains
import self
import random

import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException  # 导入NoSuchElementException


class ExceptionTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com")

    def test_exception(self):

        driver = self.driver
        try:

            search_text = driver.find_element_by_id("ss")

            self.assertEqual('百度一下', search_text.get_attribute("value"))
        except NoSuchElementException:
            file_name = "no_such_element.png"
            # driver.save_screenshot(file_name)
        driver.get_screenshot_as_file(file_name)
        raise  # 抛出异常，注释后则不抛出异常

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
