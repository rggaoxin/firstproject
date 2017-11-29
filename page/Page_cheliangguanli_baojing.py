#coding:utf-8
from common.base import BasePage

class ClbjPage(BasePage):
    """车辆报警"""
    """左侧菜单"""
    cheliangguanli_loc=("xpath",".//*[@id='app']/div[2]/div/div[1]/div/ul/li[2]/div/span")                                        #车辆管理
    cheliangbaojing_loc=("xpath",".//*[@id='app']/div[2]/div/div[1]/div/ul/li[2]/ul/li/ul/li[3]/span")                          #车辆报警
    """上方按钮"""
    xinzengbaojing_loc=("class name","el-button--info")                                                                                #新增报警并加入黑名单



