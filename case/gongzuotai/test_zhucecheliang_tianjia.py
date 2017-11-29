#coding:utf-8
from common.base import BasePage
from selenium import webdriver
from page.Page_login import LoginPage
from page.Page_wodegongzuotai import GongzuotaiPage
#from page.Page_cheliangguanli_baojing import ClbjPage
import unittest

login_url="http://192.168.3.139:8010/#/"
class  Zccl_tj(unittest.TestCase):
    """我的工作台-注册车辆-添加"""
    def  setUp(self):
        self.driver=webdriver.Chrome()
        self.driver_b=BasePage(self.driver)
        self.driver_l=LoginPage(self.driver)
        self.driver_g=GongzuotaiPage(self.driver)
#        self.driver_c=ClbjPage(self.driver)
        self.driver_l.open(login_url)
        """登录"""
        self.driver_l.input_username("admin")
        self.driver_l.input_password("super_0711")
        self.driver_l.click_login()
        title=self.driver_l.get_title()
        self.assertEqual(title,u"后台管理")
        """进入工作台"""
        self.driver_g.click_gongzuotai()

    def  test_zccl_tj(self):
        """测试注册车辆中的添加按钮能否正常使用并转入注册页面"""
        """点击车辆注册-添加按钮"""
        self.driver_g.click_zhucecheliang_tianjia()
        """判断进入页面的左上角的文字是否为备案登记"""
        beiandengji_beiandengji_loc=("xpath",".//*[@id='app']/div[2]/div/div[2]/div/div[3]/div/div[1]/span")                                          #左上角车辆备案文字
        result=self.driver_b.is_text_in_element(beiandengji_beiandengji_loc,u"备案登记")
        self.assertEqual(result,True)

    def  tearDown(self):
        self.driver.quit()


if "__name__"=="__main__":
    unittest.main()