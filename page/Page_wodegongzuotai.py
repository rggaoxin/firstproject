#coding:utf-8
from common.base import BasePage

class GongzuotaiPage(BasePage):
    """我的工作台"""
    gongzuotai_loc=("xpath",".//*[@id='app']/div[2]/div/div[1]/div/ul/li[1]/span")                                            #工作台
    zhucecheliang_tianjia_loc=("xpath",".//*[@id='app']/div[2]/div/div[2]/div/div[1]/div[1]/div/div/div[2]/button")       #车辆管理-添加
    baojing_chakan_loc=("xpath",".//*[@id='app']/div[2]/div/div[2]/div/div[1]/div[2]/div/div/div[2]/button")              #报警车辆-查看
    heimingdan_chakan_loc=("xpath",".//*[@id='app']/div[2]/div/div[2]/div/div[1]/div[3]/div/div/div[2]/button")           #黑名单车辆-查看
    baojing_heimingdan_loc=("xpath",".//*[@id='app']/div[2]/div/div[2]/div/div[1]/div[2]/div/div/div[2]/div/button")     #报警车辆-黑名单车辆报警
    cheliangfenbu_loc=("xpath",".//*[@id='container']/div[2]/div[1]")                                                           #车辆分布
    quyu_loc=("xpath",".//*[@id='app']/div[2]/div/div[2]/div/div[2]/div/div[1]/div[1]/button[1]")                         #区域
    guiji_loc=("xpath",".//*[@id='app']/div[2]/div/div[2]/div/div[2]/div/div[1]/div[1]/button[2]")                        #轨迹
    dingwei_loc=("xpath",".//*[@id='app']/div[2]/div/div[2]/div/div[2]/div/div[1]/div[1]/button[3]")                      #定位
    """区域"""
    quyu_xuanze_loc=("xpath","html/body/div[8]/div[1]")
    """轨迹"""
    guiji_chaxuntiaojian_loc=("xpath","html/body/div[7]/form/div[1]/div/div/div[1]/div/div[1]/input")                       #查询条件
    guiji_neirong_loc=("xpath","html/body/div[2]/form/div[1]/div/div/div[2]/div/div/div/div[1]/input")                     #防盗芯片&车牌号
    guiji_neirong_chepaihao_loc=("xpath","html/body/div[3]/div/div[1]/ul/li[1]")                                                #车牌号
    guiji_neirong_fangdaoxinpian_loc=("xpath","html/body/div[3]/div/div[1]/ul/li[2]/span")                                     #防盗芯片
    guiji_shuruneirong_loc=("xpath","html/body/div[2]/form/div[1]/div/div/div[2]/div/input")                                 #输入内容框
    guiji_jinriguiji_loc=("class name","el-checkbox__inner")                                                                      #今日轨迹选项框
    guiji_kaishishijian_loc=("xpath","html/body/div[2]/form/div[2]/div/div[1]/input")                                         #开始时间，时间格式2017-11-21 14:18:29
    guiji_jieshushijian_loc=("xpath","html/body/div[2]/form/div[2]/div/div[2]/input")                                         #结束时间
    guiji_genzonggui_loc=("xpath","html/body/div[3]/form/div[2]/div/div[3]/span/label/div[3]")                              #跟踪轨迹
    guiji_chaxunguiji_loc=("xpath","html/body/div[2]/form/div[3]/div/button[1]")                                              #查询轨迹
    guiji_guijihuifang_loc=("xpath","html/body/div[2]/form/div[3]/div/button[2]")                                             #轨迹回放
    guiji_guijiqingli_loc=("xpath","html/body/div[2]/form/div[3]/div/button[3]")                                              #清理轨迹
    """定位"""
    dingwei_xinpianzhonglei_loc=("xpath","html/body/div[5]/form/div[1]/div/div/div[1]/div/div[1]/input")                    #芯片种类：电动车、老人、小孩、宠物
    dingwei_chaxuntiaojian_loc=("xpath","html/body/div[2]/form/div[1]/div/div/div[2]/div/div/div/div[1]/input")            #查询条件：防盗芯片id，车牌号，车主姓名，手机号
    dingwei_shurukuang_loc=("xpath","html/body/div[2]/form/div[1]/div/div/div[2]/div/input")                                 #输入框
    dingwei_queren_loc=("xpath","html/body/div[2]/form/div[2]/div/button[1]")                                                  #确认
    dingwei_qingchu_loc=("xpath","html/body/div[2]/form/div[2]/div/button[2]")                                                 #清楚定位
    dingwei_chaxuntiaojian_chepaihao_loc=("xpath","html/body/div[4]/div/div[1]/ul/li[1]/span")                                  #查询内容-车牌号
    dingwei_chaxuntiaojian_xinpian_loc=("xpath","html/body/div[4]/div/div[1]/ul/li[2]")                                         #查询内容-防盗芯片
    dingwei_chaxuntiaojian_phonenumber_loc=("xpath","html/body/div[4]/div/div[1]/ul/li[4]")                                     #查询内容-手机号
    dingwei_chaxuntiaojian_xingming_loc=("xpath","html/body/div[4]/div/div[1]/ul/li[3]")                                        #查询内容-车主姓名


    def click_gongzuotai(self):
        '''进入工作台'''
        self.click(self.gongzuotai_loc)

    def click_zhucecheliang_tianjia(self):
        '''点击注册车辆添加'''
        self.click(self.zhucecheliang_tianjia_loc)

    def click_baojing_chakan(self):
        '''点击报警车辆查看'''
        self.click(self.baojing_chakan_loc)

    def click_heimingdan_chakan(self):
        '''点击黑名单车辆查看'''
        self.click(self.heimingdan_chakan_loc)

    def click_baojing_heimingdan(self):
        '''点击黑名单车辆报警'''
        self.click(self.baojing_heimingdan_loc)

    def click_quyu(self):
        """点击区域按钮"""
        self.click(self.quyu_loc)

    def click_guiji(self):
        """点击轨迹按钮"""
        self.click(self.guiji_loc)

    def click_guiji_chaxun(self):
        """点击轨迹-查询轨迹"""
        self.click(self.guiji_chaxunguiji_loc)

    def click_guiji_jinriguiji(self):
        """点击轨迹-今日轨迹"""
        self.click(self.guiji_jinriguiji_loc)

    def click_guiji_id(self):
        """点击轨迹-防盗芯片/车牌号"""
        self.click(self.guiji_neirong_loc)

    def click_guiji_neirong_chepaihao(self):
        """点击轨迹-内容-车牌号"""
        self.click(self.guiji_neirong_chepaihao_loc)

    def click_guiji_neirong_xinpian(self):
        """点击轨迹-内容-防盗芯片"""
        self.click(self.guiji_neirong_fangdaoxinpian_loc)

    def input_guiji_neirong(self,neirong):
        """发送轨迹-请输入内容"""
        self.send_keys(self.guiji_shuruneirong_loc,neirong)

    def click_guiji_neirong(self):
        """点击输入内容,让时间可以输入"""
        self.click(self.guiji_shuruneirong_loc)

    def input_guiji_begintime(self,time):
        """发送轨迹-开始时间"""
        self.send_keys(self.guiji_kaishishijian_loc,time)#2017-11-22 13:39:32

    def input_guiji_endtime(self,time):
        """发送轨迹-结束时间"""
        self.send_keys(self.guiji_jieshushijian_loc,time)#2017-11-22 13:39:32

    def click_guiji_genzong(self):
        """点击跟踪轨迹"""
        self.click(self.guiji_genzonggui_loc)

    def click_dingwei(self):
        """点击定位"""
        self.click(self.dingwei_loc)

    def click_dingwei_tiaojian(self):
        """点击定位-查询条件"""
        self.click(self.dingwei_chaxuntiaojian_loc)

    def click_dingwei_tiaojian_chepaihao(self):
        """点击定位-查询条件-车牌号"""
        self.click(self.dingwei_chaxuntiaojian_chepaihao_loc)

    def click_dingwei_tiaojian_xinpian(self):
        """点击定位-查询条件-芯片"""
        self.click(self.dingwei_chaxuntiaojian_xinpian_loc)

    def click_dingwei_tiaojian_phone(self):
        """点击定位-查询条件-手机号"""
        self.click(self.dingwei_chaxuntiaojian_phonenumber_loc)

    def click_dingwei_tiaojian_xingming(self):
        """点击定位-查询条件-车主姓名"""
        self.click(self.dingwei_chaxuntiaojian_xingming_loc)

    def input_dingwei_neirong(self,neirong):
        """输入定位-请输入内容"""
        self.send_keys(self.dingwei_shurukuang_loc,neirong)

    def click_dingwei_queding(self):
        """点击定位-确定"""
        self.click(self.dingwei_queren_loc)