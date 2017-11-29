#coding:utf-8
from common.base import BasePage
from page.Page_login import LoginPage
from page.Page_wodegongzuotai import GongzuotaiPage
import unittest
from selenium import webdriver
import time

class Guji(unittest.TestCase):
    """轨迹"""
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
        self.driver_g.click_guiji()

    def test_chaxunguiji_xinpian(self):
        """输入芯片编号查询轨迹"""
        self.driver_g.input_guiji_neirong("524451")
        self.driver_g.click_guiji_jinriguiji()
        self.driver_g.input_guiji_begintime("2017-11-02 13:39:32")
        self.driver_g.click_guiji_neirong()
        self.driver_g.input_guiji_endtime("2017-11-22 13:39:32")
        self.driver_g.click_guiji_neirong()
        self.driver_g.click_guiji_chaxun()
        jizhan_loc=("xpath",".//*[@id='container']/div[1]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[1]/div")
        result=self.driver_g.is_text_in_element(jizhan_loc,"7255")
        self.assertEqual(result,True)

    def test_chaxunguiji_chepaihao(self):
        """输入车牌号查询轨迹"""
        self.driver_g.click_guiji_id()
        self.driver_g.click_guiji_neirong_chepaihao()
        self.driver_g.input_guiji_neirong(u"武汉AA2796")
        self.driver_g.click_guiji_jinriguiji()
        self.driver_g.input_guiji_begintime("2017-11-02 13:39:32")
        self.driver_g.click_guiji_neirong()
        self.driver_g.input_guiji_endtime("2017-11-22 13:39:32")
        self.driver_g.click_guiji_neirong()
        self.driver_g.click_guiji_chaxun()
        jizhan_loc=("xpath",".//*[@id='container']/div[1]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[1]/div")
        result=self.driver_g.is_text_in_element(jizhan_loc,"7255")
        self.assertEqual(result,True)

    def tearDown(self):
        self.driver.quit()

if  "__name__"=="__main__":
    unittest.main()