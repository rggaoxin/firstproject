#coding:utf-8
import unittest
from selenium import webdriver
from common.base import BasePage
from page.Page_login import LoginPage
from page.Page_wodegongzuotai import GongzuotaiPage
import time

class Fb_qy(unittest.TestCase):
    """车辆分布，区域"""
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

    def test_fenbu(self):
        """验证车辆分布是否显示"""
        cheliangfenbu_loc=("xpath",".//*[@id='container']/div[2]/div[1]")                                                           #车辆分布
        result=self.driver_g.is_text_in_element(cheliangfenbu_loc,u"车辆分布")
        self.assertEqual(result,True)

    # def test_quyu(self):
    #暂未查出原因，无法用xpath方法定位到元素，无法判断元素
    #     """验证区域是否能点击"""
    #     time.sleep(2)
    #     self.driver_g.click_quyu()
    #     xuanzequyu_loc=("xpath","html/body/div[5]/div[1]")
    #
    #     time.sleep(2)
    #     result=self.driver_g.is_visibility(xuanzequyu_loc)
    #     print result
        #result=self.driver_g.is_text_in_element(xuanzequyu_loc,u"选择区域")
        #self.assertEqual(result,True)

    def tearDown(self):
        self.driver.quit()

if  "__name__"=="__main__":
    unittest.main()