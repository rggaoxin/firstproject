#coding:utf-8
from common.base import BasePage

class ClbadjPage(BasePage):
    """定位车辆备案登记页面元素"""
    """左侧菜单"""
    cheliangguanli_loc=("xpath",".//*[@id='app']/div[2]/div/div[1]/div/ul/li[2]/div/span")                                        #车辆管理
    cheliangbeiandengji_loc=("xpath",".//*[@id='app']/div[2]/div/div[1]/div/ul/li[2]/ul/li/ul/li[1]/span")                      #车辆备案登记
    cheliangbeiandengji_gaopaiyi_loc=("xpath",".//*[@id='app']/div[2]/div/div[1]/div/ul/li[2]/ul/li/ul/li[2]/span")             #车辆备案登记-高拍仪
    """页面按钮"""
    beiandengji_loc=("xpath",".//*[@id='app']/div[2]/div/div[2]/div/div[1]/button[1]")                                            #备案登记
    shanchu_loc=("xpath",".//*[@id='app']/div[2]/div/div[2]/div/div[1]/button[2]")                                                #删除
    chaxun_loc=("xpath",".//*[@id='app']/div[2]/div/div[2]/div/div[1]/button[3]")                                                 #查询
    chaxuntiaojian_neirong_loc=("xpath",".//*[@id='app']/div[2]/div/div[2]/div/div[1]/span[2]/div/div/input")                   #查询条件,请输入内容
    chaxuntiaojian_xuanze_loc=("xpath",".//*[@id='app']/div[2]/div/div[2]/div/div[1]/span[2]/div/div/div/div/div[1]/input")  #查询条件-选择查询条件
    chaxuntiaojian_xuanze_xingming_loc=("xpath","html/body/div[@class='el-select-dropdown']/div/div[1]/ul/li[1]")                                       #查询条件,请输入内容，姓名
    chaxuntiaojian_xuanze_shoujihao_loc=("xpath","html/body/div[@class='el-select-dropdown']/div/div[1]/ul/li[2]")                                      #查询条件,请输入内容，手机号
    chaxuntiaojian_xuanze_shenfenzhenghao_loc=("xpath","html/body/div[@class='el-select-dropdown']/div/div[1]/ul/li[3]")                                #查询条件,请输入内容，身份证号
    chaxuntiaojian_xuanze_chepaihao_loc=("xpath","html/body/div[@class='el-select-dropdown']/div/div[1]/ul/li[4]")                                      #查询条件,请输入内容，车牌号
    chaxuntiaojian_xuanze_chejiahao_loc=("xpath","html/body/div[@class='el-select-dropdown']/div/div[1]/ul/li[5]")                                      #查询条件,请输入内容，车架号
    chaxuntiaojian_xuanze_xinpianhao_loc=("xpath","html/body/div[@class='el-select-dropdown']/div/div[1]/ul/li[6]")                                     #查询条件,请输入内容，防盗芯片编号
    shijianfanwei_loc=("xpath",".//*[@id='app']/div[2]/div/div[2]/div/div[1]/span[3]/div/input")                                #时间范围，输入完成后需要点击一下其他地方
    chaxuntiaojian_zhuangtai_loc=("xpath",".//div[@class='right flex1 vbox']/div/div[2]/div/div[1]/span[4]/div/div[1]/input")              #用户状态
    chaxuntiaojian_zhuangtai_suoyou_loc=("xpath","html/body/div[@class='el-select-dropdown'][2]/div/div[1]/ul/li[1]")                                      #用户状态-所有
    chaxuntiaojian_zhuangtai_zhengchang_loc=("xpath","html/body/div[@class='el-select-dropdown'][2]/div/div[1]/ul/li[2]")                                  #用户状态-正常
    chaxuntiaojian_zhuangtai_heimingdan_loc=("xpath","html/body/div[@class='el-select-dropdown'][2]/div/div[1]/ul/li[3]")                                  #用户状态-黑名单
    chaxuntiaojian_tianjiaren_loc=("xpath",".//*[@id='app']/div[2]/div/div[2]/div/div[1]/span[5]/div/div[1]/input")           #查询条件添加人
    chaxuntiaojian_tianjiaren_xiupai_loc=("xpath","html/body/div[2]/div/div[1]/ul/li[4]")                                     #添加人-秀派
    guijichaxun_loc=("xpath",".//*[@id='app']/div[2]/div/div[2]/div/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[10]/div/button")  #轨迹查询
    """备案登记中的填充项"""
    beiandengji_phone_loc=('xpath',".//*[@id='app']/div[2]/div/div[2]/div/div[3]/div/div[2]/form/div[2]/div[1]/div/div/div[1]/input")                   #手机号
    beiandengji_name_loc=('xpath',".//*[@id='app']/div[2]/div/div[2]/div/div[3]/div/div[2]/form/div[2]/div[2]/div/div/div/input")                       #姓名
    beiandengji_address_loc=('xpath',".//*[@id='app']/div[2]/div/div[2]/div/div[3]/div/div[2]/form/div[3]/div[1]/div/div/div/input")                    #地址
    beiandengji_mancardid_loc=('xpath',".//*[@id='app']/div[2]/div/div[2]/div/div[3]/div/div[2]/form/div[3]/div[2]/div/div/div/input")                  #身份证号码
    beiandengji_cardid_loc=('xpath',".//*[@id='app']/div[2]/div/div[2]/div/div[3]/div/div[2]/form/div[5]/div[1]/div[1]/div/div/input")                 #芯片编号
    beiandengji_chejiaid_loc=('xpath',".//*[@id='app']/div[2]/div/div[2]/div/div[3]/div/div[2]/form/div[5]/div[1]/div[3]/div/div/input")               #车架号
    beiandengji_chepaiid_loc=("xpath",".//*[@id='app']/div[2]/div/div[2]/div/div[3]/div/div[2]/form/div[5]/div[1]/div[2]/div/div/input")               #车牌号
    beiandengji_chepinpai_loc=('xpath',".//*[@id='app']/div[2]/div/div[2]/div/div[3]/div/div[2]/form/div[5]/div[1]/div[4]/div/div/div[1]/input")      #车品牌
    beiandengji_chepinpai_xinlei=("xpath","html/body/div[3]/div/div[1]/ul/li[6]/span")                                                                          #车品牌-小鸟
    beiandengji_goucheriqi_loc=("xpath",".//*[@id='app']/div[2]/div/div[2]/div/div[3]/div/div[2]/form/div[5]/div[1]/div[5]/div/div/input")             #购车日期
    beiandengji_cheliangyanse_loc=("xpath",".//*[@id='app']/div[2]/div/div[2]/div/div[3]/div/div[2]/form/div[5]/div[1]/div[6]/div/div/div[1]/input")  #车辆颜色
    beiandengji_cheliangyanse_huangse=("xpath","html/body/div[5]/div/div[1]/ul/li[7]/span")                                                                     #车辆颜色-黄色
    beiandengji_dianjihao_loc=("xpath",".//*[@id='app']/div[2]/div/div[2]/div/div[3]/div/div[2]/form/div[5]/div[1]/div[7]/div/div/input")              #电机号
    beiandengji_beizhu_loc=("xpath",".//*[@id='app']/div[2]/div/div[2]/div/div[3]/div/div[2]/form/div[5]/div[1]/div[8]/div/div/input")                 #备注
    beiandengji_toubaomingxi_loc=("xpath",".//*[@id='app']/div[2]/div/div[2]/div/div[3]/div/div[2]/form/div[5]/div[2]/div[2]/div/div/div[1]/input")   #投保明细
    beiandengji_baocun_loc=("xpath",".//*[@id='app']/div[2]/div/div[2]/div/div[3]/div/div[3]/span/button[1]")                                              #保存
    beiandengji_quxiao_loc=("xpath",".//*[@id='app']/div[2]/div/div[2]/div/div[3]/div/div[3]/span/button[2]")                                              #取消
    """数据定位"""
    chezhuxingming_loc=("xpath",".//*[@id='app']/div[2]/div/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div")                   #车主姓名
    shoujihao_loc=("xpath",".//*[@id='app']/div[2]/div/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div")                        #手机号
    cheliangpinpai_loc=("xpath",".//*[@id='app']/div[2]/div/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[4]/div")                   #车辆品牌
    chepaihao_loc=("xpath",".//*[@id='app']/div[2]/div/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[5]/div")                        #车牌号
    xinpianhao_loc=("xpath",".//*[@id='app']/div[2]/div/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[6]/div")                       #芯片编号
    shangpaishijian_loc=("xpath",".//*[@id='app']/div[2]/div/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[7]/div")                  #上牌时间
    tianjiaren_loc=("xpath",".//*[@id='app']/div[2]/div/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[8]/div")                       #添加人
    shefangzhuangtai_loc=("xpath",".//*[@id='app']/div[2]/div/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[9]/div")                 #设防状态

    def click_cheliangguanli(self):
        """点击车辆管理页面"""
        self.click(self.cheliangguanli_loc)

    def click_cheliangbeiandengji(self):
        """点击车辆备案登记"""
        self.click(self.cheliangbeiandengji_loc)

    def click_cheliangbeiandengji_gaopaiyi(self):
        """点击车辆备案登记-高拍仪"""
        self.click(self.cheliangbeiandengji_gaopaiyi_loc)

    def click_beiandengji(self):
        """点击车辆备案登记-备案登记"""
        self.click(self.beiandengji_loc)

    def click_chaxuntiaojian_xuanze(self):
        """点击车辆备案登记-防盗芯片（选择条件）"""
        self.click(self.chaxuntiaojian_xuanze_loc)

    def click_chaxuntiaojian_xuanze_xingming(self):
        """点击车辆备案登记-选择查询条件-姓名"""
        self.click(self.chaxuntiaojian_xuanze_xingming_loc)

    def click_chaxuntiaojian_xuanze_shoujihao(self):
        """点击车辆备案登记-选择查询条件-手机号"""
        self.click(self.chaxuntiaojian_xuanze_shoujihao_loc)

    def click_chaxuntiaojian_xuanze_shenfenzheng(self):
        """点击车辆备案登记-选择查询条件-身份证"""
        self.click(self.chaxuntiaojian_xuanze_shenfenzhenghao_loc)

    def click_chaxuntiaojian_xuanze_chepaihao(self):
        """点击车辆备案登记-选择查询条件-车牌号"""
        self.click(self.chaxuntiaojian_xuanze_chepaihao_loc)

    def click_chaxuntiaojian_xuanze_chejiahao(self):
        """点击车辆备案登记-选择查询条件-车架号"""
        self.click(self.chaxuntiaojian_xuanze_chejiahao_loc)

    def click_chaxuntiaojian_xuanze_fangdaoxinpian(self):
        """点击车辆备案登记-选择查询条件-防盗芯片"""
        self.click(self.chaxuntiaojian_xuanze_xinpianhao_loc)

    def input_chaxuntiaojian_neirong(self,text):
        """车辆备案登记-查询条件内容输入"""
        self.send_keys(self.chaxuntiaojian_neirong_loc,text)

    def input_shijianfanwei(self,time):
        """车辆备案登记-输入时间范围"""
        self.send_keys(self.shijianfanwei_loc,time)   #2017-11-02 00:00:00 - 2017-11-04 00:00:00

    def click_chaxuntiaojian_zhuangtai(self):
        """车辆备案登记-状态（默认为所有）"""
        self.click(self.chaxuntiaojian_zhuangtai_loc)

    def click_chaxuntiaojian_zhuangtai_suoyou(self):
        """车辆备案登记-状态-所有"""
        self.click(self.chaxuntiaojian_zhuangtai_suoyou_loc)

    def click_chaxuntiaojian_zhuangtai_zhengchang(self):
        """车辆备案登记-状态-正常"""
        self.click(self.chaxuntiaojian_zhuangtai_zhengchang_loc)

    def click_chaxuntiaojian_zhuangtai_heimingdan(self):
        """车辆备案登记-状态-黑名单"""
        self.click(self.chaxuntiaojian_zhuangtai_heimingdan_loc)

    def click_chaxuntiaojian_tianjiaren(self):
        """车辆备案登记-添加人"""
        self.click(self.chaxuntiaojian_tianjiaren_loc)

    def click_chaxuntiaojian_tianjiaren_xiupai(self):
        """车辆备案登记-添加人-秀派"""
        self.click(self.chaxuntiaojian_tianjiaren_xiupai_loc)

    def click_chaxun(self):
        """车辆备案登记-查询"""
        self.click(self.chaxun_loc)

    def click_shanchu(self):
        """车辆备案登记-删除"""
        self.click(self.shanchu_loc)