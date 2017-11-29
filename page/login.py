#coding:utf-8
def login(self,user='admin',psw='super_0711'):
    username=('xpath',".//*[@id='app']/div[2]/div/div/form/div[1]/div/div/input")
    password=('xpath',".//*[@id='app']/div[2]/div/div/form/div[2]/div/div/input")
    button=('xpath',".//*[@id='app']/div[2]/div/div/form/div[3]/div/button")
    self.driver_n.send_keys(username,user)
    self.driver_n.send_keys(password,psw)
    self.driver_n.click(button)