#coding:utf-8
from selenium import webdriver
from page.Page_login import LoginPage
from page.Page_wodegongzuotai import GongzuotaiPage
import unittest

login_url="http://192.168.3.139:8010/#/"
class hmdbj(unittest.TestCase):
    """黑名单车辆报警"""
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver_l=LoginPage(self.driver)
        self.driver_g=GongzuotaiPage(self.driver)
        self.driver_g.open(login_url)
        """登录"""
        self.driver_l.input_username("admin")
        self.driver_l.input_password("super_0711")
        self.driver_l.click_login()
        title=self.driver_l.get_title()
        self.assertEqual(title,u"后台管理")
        """进入工作台"""
        self.driver_g.click_gongzuotai()

    def test_hmdbj(self):
        self.driver_g.click_baojing_heimingdan()
        jilu_loc=("class name","el-dialog__title")          #异常车辆报警记录
        result=self.driver_g.is_text_in_element(jilu_loc,u'异常车辆报警记录')
        self.assertEqual(result,True)

    def tearDown(self):
        self.driver.quit()

if "__name__"=="__main__":
    unittest.main()