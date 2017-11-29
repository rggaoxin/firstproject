#coding:utf-8
from common.base import BasePage


class LoginPage(BasePage):
    username_loc=("xpath",".//*[@id='app']/div[2]/div/div/form/div[1]/div/div[1]/input")
    password_loc=("xpath",".//*[@id='app']/div[2]/div/div/form/div[2]/div/div/input")
    loginbutton_loc=("class name","el-button")
    def input_username(self,username="admin"):
        self.send_keys(self.username_loc,username)

    def input_password(self,password="super_0711"):
        self.send_keys(self.password_loc,password)

    def click_login(self):
        self.click(self.loginbutton_loc)