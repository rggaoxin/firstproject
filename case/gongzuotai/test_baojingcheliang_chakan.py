#coding:utf-8
from common.base import BasePage
from selenium import webdriver
from page.Page_login import LoginPage
from page.Page_wodegongzuotai import GongzuotaiPage
import unittest

class Bjcl_ck(unittest.TestCase):
    """我的工作台-报警车辆-查看"""
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver_l=LoginPage(self.driver)
        self.driver_g=GongzuotaiPage(self.driver)
        self.driver_g.open()
        """登录"""
        self.driver_l.input_username("admin")
        self.driver_l.input_password("super_0711")
        self.driver_l.click_login()
        title=self.driver_l.get_title()
        self.assertEqual(title,u"后台管理")
        """进入工作台"""
        self.driver_g.click_gongzuotai()

    def test_bjcl_ck(self):
        """工作台-报警车辆-查看"""
        self.driver_g.click_baojing_chakan()
        xinzengbaojing_loc=("class name","el-button--info")
        result=self.driver_g.is_text_in_element(xinzengbaojing_loc,u"新增报警")
        self.assertEqual(result,True)

    def tearDown(self):
        self.driver.quit()

if "__name__"=="__main__":
    unittest.main()