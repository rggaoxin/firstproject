#coding:utf-8
import unittest
from selenium import webdriver
from page.Page_login import LoginPage

class  Login_test(unittest.TestCase):
    """登录"""
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver_n=LoginPage(self.driver)
        self.driver_n.open()

    def test_login(self):
        self.driver_n.input_username("admin")
        self.driver_n.input_password("super_0711")
        self.driver_n.click_login()
        title=self.driver_n.get_title()
        self.assertEqual(title,u"后台管理")

    def tearDown(self):
        self.driver.quit()

if "__name__"=="__main__":
    unittest.main()