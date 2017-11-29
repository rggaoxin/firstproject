#coding:utf-8
import unittest
from selenium import webdriver
from page.Page_login import LoginPage
from page.Page_wodegongzuotai import GongzuotaiPage
from common.base import BasePage


class Hmd_ck(unittest.TestCase):
    """我的工作台-黑名单车辆-查看"""
    def  setUp(self):
        self.driver=webdriver.Chrome()
        self.driver_b=BasePage(self.driver)
        self.driver_l=LoginPage(self.driver)
        self.driver_g=GongzuotaiPage(self.driver)
        #self.driver_c=ClbjPage(self.driver)
        self.driver_l.open()
        """登录"""
        self.driver_l.input_username("admin")
        self.driver_l.input_password("super_0711")
        self.driver_l.click_login()
        title=self.driver_l.get_title()
        self.assertEqual(title,u"后台管理")
        """进入工作台"""
        self.driver_g.click_gongzuotai()

    def test_heimingdan(self):
        self.driver_g.click_heimingdan_chakan()
        heimingdan_loc=("xpath",".//*[@id='app']/div[2]/div/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div")                #显示的第一条数据的名字是张峰
        result=self.driver_b.is_text_in_element(heimingdan_loc,u"张峰")
        self.assertEqual(result,True)

    def tearDown(self):
        self.driver.quit()

if  "__name__"=="__main__":
    unittest.main()