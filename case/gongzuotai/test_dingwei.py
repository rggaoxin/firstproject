#coding:utf-8
from selenium import webdriver
from common.base import BasePage
from page.Page_login import LoginPage
from page.Page_wodegongzuotai import GongzuotaiPage
import unittest
import time

class Guji(unittest.TestCase):
    """定位"""
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver_g=GongzuotaiPage(self.driver)
        self.driver_l=LoginPage(self.driver)
        self.driver_l.open()
        self.driver_l.input_username()
        self.driver_l.input_password()
        self.driver_l.click_login()
        title=self.driver_l.get_title()
        self.assertEqual(title,u"后台管理")
        """进入工作台"""
        self.driver_g.click_gongzuotai()
        self.driver_g.click_dingwei()

    def test_dingwei_chepaihao(self):
        """定位-芯片编号"""
        self.driver_g.input_dingwei_neirong(u"511539")
        self.driver_g.click_dingwei_queding()
        text=("xpath","html/body/div[2]/form/div[3]/div/div/div[1]/span[4]")
        result=self.driver_g.is_text_in_element(text,"王连珍")
        self.assertEqual(result,True)

    def tearDown(self):
        self.driver.quit()

if  "__name__"=="__main__":
    unittest.main()