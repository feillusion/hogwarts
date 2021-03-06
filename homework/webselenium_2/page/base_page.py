from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import json


class BasePage:
    def __init__(self,base_driver=None):
        base_driver: WebDriver
        #若没有窗口实例，则创建一个，若有则复用已有的
        if base_driver is None:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(5)
            self.driver.maximize_window()
            #添加登录cookie,隐式等待
            self._login_cookie()
            self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
            self.driver.implicitly_wait(5)
        else:
            self.driver = base_driver

    def _login_cookie(self):
        self.driver.get('https://work.weixin.qq.com/')
        with open('../testcase/cookies.json', 'r') as f:
            cookies = json.load(f)
        for cookie in cookies:
            self.driver.add_cookie(cookie)

    def find(self,value,by='xpath'):
        if by=='id':
            return self.driver.find_element(By.ID,value)
        elif by=='css':
            return self.driver.find_element((By.CSS_SELECTOR,value))
        else:
            return self.driver.find_element(By.XPATH,value)

    def finds(self,value,by='xpath'):
        if by=='id':
            return self.driver.find_elements(By.ID,value)
        elif by=='css':
            return self.driver.find_elements((By.CSS_SELECTOR,value))
        else:
            return self.driver.find_elements(By.XPATH,value)

    def quit(self):
        self.driver.quit()
