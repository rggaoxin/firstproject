#coding:utf-8
from selenium import webdriver
from page.Page_login import LoginPage
from page.Page_cheliangguanli_dengji import ClbadjPage
from page.Page_wodegongzuotai import GongzuotaiPage
import unittest
import time

class Chaxuntiaojian(unittest.TestCase):
    """备案登记-查询条件"""
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver_c=ClbadjPage(self.driver)
        self.driver_l=LoginPage(self.driver)
        self.driver_l.open()
        self.driver_l.input_username()
        self.driver_l.input_password()
        self.driver_l.click_login()
        title=self.driver_l.get_title()
        self.assertEqual(title,u"后台管理")
        """进入车辆管理--车辆备案登记页面"""#默认页面为车辆备案登记页面，不需要进去页面
        #self.driver_c.click_cheliangguanli()
        #self.driver_c.click_cheliangbeiandengji()

    def test_xinming(self):
        """查询条件-姓名"""
        self.driver_c.click_chaxuntiaojian_xuanze()
        self.driver_c.click_chaxuntiaojian_xuanze_xingming()
        self.driver_c.input_chaxuntiaojian_neirong(u"肖银才")
        self.driver_c.click_chaxun()
        text=("xpath",".//*[@id='app']/div[2]/div/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr/td[2]/div")
        result=self.driver_c.is_text_in_element(text,"肖银才")
        self.assertEqual(result,True)

    def test_shoujihao(self):
        """查询条件-手机号"""
        self.driver_c.click_chaxuntiaojian_xuanze()
        time.sleep(2)
        self.driver_c.click_chaxuntiaojian_xuanze_shoujihao()
        self.driver_c.input_chaxuntiaojian_neirong("13308630215")
        self.driver_c.click_chaxun()
        text=("xpath",".//*[@id='app']/div[2]/div/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr/td[3]/div")
        result=self.driver_c.is_text_in_element(text,"13308630215")
        self.assertEqual(result,True)

    def test_shenfenzhenghao(self):
        """查询条件-身份证号"""
        self.driver_c.click_chaxuntiaojian_xuanze()
        time.sleep(2)
        self.driver_c.click_chaxuntiaojian_xuanze_shenfenzheng()
        self.driver_c.input_chaxuntiaojian_neirong("420106196908233566")
        self.driver_c.click_chaxun()
        text=("xpath",".//*[@id='app']/div[2]/div/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr/td[3]/div")
        result=self.driver_c.is_text_in_element(text,"13971331771")
        self.assertEqual(result,True)

    def test_chepaihao(self):
        """查询条件-车牌号"""
        self.driver_c.click_chaxuntiaojian_xuanze()
        time.sleep(2)
        self.driver_c.click_chaxuntiaojian_xuanze_chepaihao()
        self.driver_c.input_chaxuntiaojian_neirong(u"武汉Z25397")
        self.driver_c.click_chaxun()
        text=("xpath",".//*[@id='app']/div[2]/div/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr/td[5]/div")
        result=self.driver_c.is_text_in_element(text,"武汉Z25397")
        self.assertEqual(result,True)

    def test_chejiahao(self):
        """查询条件-车架号"""
        self.driver_c.click_chaxuntiaojian_xuanze()
        time.sleep(2)
        self.driver_c.click_chaxuntiaojian_xuanze_chejiahao()
        self.driver_c.input_chaxuntiaojian_neirong(u"373521512023153")
        self.driver_c.click_chaxun()
        text=("xpath",".//*[@id='app']/div[2]/div/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr/td[3]/div")
        result=self.driver_c.is_text_in_element(text,"13027191879")
        self.assertEqual(result,True)

    def test_xinpianbianhao(self):
        """查询条件-芯片编号"""
        self.driver_c.click_chaxuntiaojian_xuanze()
        time.sleep(2)
        self.driver_c.click_chaxuntiaojian_xuanze_fangdaoxinpian()
        self.driver_c.input_chaxuntiaojian_neirong(u"531175")
        self.driver_c.click_chaxun()
        text=("xpath",".//*[@id='app']/div[2]/div/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr/td[6]/div")
        result=self.driver_c.is_text_in_element(text,"531175")
        self.assertEqual(result,True)

    def test_shijianfangwei(self):
        """时间范围"""
        self.driver_c.input_shijianfanwei("2017-11-01 17:45:00 - 2017-11-02 00:00:00")
        self.driver_c.click_chaxun()
        text=("xpath",".//*[@id='app']/div[2]/div/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr/td[6]/div")
        result=self.driver_c.is_text_in_element(text,"531206")
        self.assertEqual(result,True)

    def test_zhuangtai_suoyou(self):
        """状态-所有"""
        self.driver_c.click_chaxuntiaojian_xuanze()
        self.driver_c.click_chaxuntiaojian_xuanze_shoujihao()
        self.driver_c.input_chaxuntiaojian_neirong("15972035798")
        self.driver_c.click_chaxuntiaojian_zhuangtai()
        self.driver_c.click_chaxuntiaojian_zhuangtai_suoyou()
        #time.sleep(2)
        self.driver_c.click_chaxun()
        t1=("xpath",".//*[@id='app']/div[2]/div/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[6]/div")
        t2=("xpath",".//*[@id='app']/div[2]/div/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr[2]/td[6]/div")
        text1=self.driver_c.get_text(t1)
        text2=self.driver_c.get_text(t2)
        self.assertEqual(text1,'792340') and self.assertEqual(text2,'586219')

    def test_zhuangtai_zhengchang(self):
        """状态-正常"""
        self.driver_c.click_chaxuntiaojian_xuanze()
        self.driver_c.click_chaxuntiaojian_xuanze_shoujihao()
        self.driver_c.input_chaxuntiaojian_neirong("15972035798")
        self.driver_c.click_chaxuntiaojian_zhuangtai()
        self.driver_c.click_chaxuntiaojian_zhuangtai_zhengchang()
        #time.sleep(2)
        self.driver_c.click_chaxun()
        t1=("xpath",".//*[@id='app']/div[2]/div/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[6]/div")
        t2=("xpath",".//*[@id='app']/div[2]/div/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr[2]/td[6]/div")
        text1=self.driver_c.get_text(t1)
        self.assertEqual(text1,'792340') and self.driver_c.is_invisibility(t2)

    def test_zhuangtai_heimingdan(self):
        """状态-黑名单"""
        self.driver_c.click_chaxuntiaojian_xuanze()
        self.driver_c.click_chaxuntiaojian_xuanze_shoujihao()
        self.driver_c.input_chaxuntiaojian_neirong("15972035798")
        self.driver_c.click_chaxuntiaojian_zhuangtai()
        self.driver_c.click_chaxuntiaojian_zhuangtai_heimingdan()
        #time.sleep(2)
        self.driver_c.click_chaxun()
        t1=("xpath",".//*[@id='app']/div[2]/div/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[6]/div")
        t2=("xpath",".//*[@id='app']/div[2]/div/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr[2]/td[6]/div")
        text1=self.driver_c.get_text(t1)
        self.assertEqual(text1,'586219') and self.driver_c.is_invisibility(t2)

    def test_tianjiaren(self):
        """添加人-秀派"""
        self.driver_c.click_chaxuntiaojian_tianjiaren()
        self.driver_c.click_chaxuntiaojian_tianjiaren_xiupai()
        #self.driver_c.click_chaxun()
        t1=("xpath",".//*[@id='app']/div[2]/div/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[6]/div")
        t2=("xpath",".//*[@id='app']/div[2]/div/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr[2]/td[6]/div")
        text1=self.driver_c.get_text(t1)
        text2=self.driver_c.get_text(t2)
        self.assertEqual(text1,"124385")  and self.assertEqual(text2,"149456")

    def tearDown(self):
        self.driver.quit()

if  "__name__"=="__main__":
    unittest.main()