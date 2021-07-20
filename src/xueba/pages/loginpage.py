from time import sleep

from selenium.webdriver.support.wait import WebDriverWait

from src.xueba.pages.basepage import BasePage


class StartPage(BasePage):
    def signin(self):
        self.click(('xpath',"//*[@resource-id='com.xiaoyu.com.xueba:id/btn_register']"))
        return SigninPage(self.driver)
    def login(self):
        self.click(('id','com.xiaoyu.com.xueba:id/btn_login'))
        return LoginPage(self.driver)


class SigninPage(BasePage):
    def signin_student(self):
        self.sendkeys(('id','com.xiaoyu.com.xueba:id/etInputPhone'),'1564008720')
        self.click(('id','com.xiaoyu.com.xueba:id/tv_get_code'))
        sleep(5)
        self.sendkeys(('id','com.xiaoyu.com.xueba:id/etValidateCode'),'111111')
        self.sendkeys(('id','com.xiaoyu.com.xueba:id/etPasswd'),'888888')
        self.click(('id','com.xiaoyu.com.xueba:id/btn_register'))
        return StartPage(self.driver)


    def signin_teacher(self):
        pass


class LoginPage(BasePage):
    def login_student(self):
        self.sendkeys(('id','com.xiaoyu.com.xueba:id/etInputPhone'),'15624008720')
        self.sendkeys(('id','com.xiaoyu.com.xueba:id/etPasswd'),'wyf19920220')
        self.click(('id','com.xiaoyu.com.xueba:id/btnLogin'))
        return FindteacherPage(self.driver)

    def login_teacher(self):
        pass
    def login_student_code(self):
        pass
    def login_teacher_code(self):
        pass

class FindteacherPage(BasePage):
    def release_task(self):
        self.click(('id','com.xiaoyu.com.xueba:id/rel_top'))
        self.click(('xpath','//*[@text="五年级"]'))
        self.click(('id', 'com.xiaoyu.com.xueba:id/sgv_subject'))
        self.click(('xpath', '//*[@text="语文"]'))
        self.click(('id', 'com.xiaoyu.com.xueba:id/sgv_schooltype'))
        self.click(('xpath','//*[@text="不限"]'))
        self.cleantext(('xpath','//*[@resource-id="com.xiaoyu.com.xueba:id/spv1"]/*[@resource-id="com.xiaoyu.com.xueba:id/tv_price"]'))
        self.sendkeys(('xpath','//*[@resource-id="com.xiaoyu.com.xueba:id/spv1"]/*[@resource-id="com.xiaoyu.com.xueba:id/tv_price"]'),'5')
        self.click(('xpath','//*[@resource-id="com.xiaoyu.com.xueba:id/spv2"]/*[@resource-id="com.xiaoyu.com.xueba:id/iv_up"]'))


    def goto_contact(self):
        self.click(('xpath','//*[@text="通讯录"]'))
        return  ContactPage(self.driver)

class ContactPage(BasePage):
    def goto_findteacher(self):
        pass

    def goto_search(self):
        self.click(('id','com.xiaoyu.com.xueba:id/tv_right_title'))
        return SearchPage(self.driver)

class SearchPage(BasePage):
    def search(self):
        self.sendkeys(('id','com.xiaoyu.com.xueba:id/et_name'),'哈哈')
        self.click(('id','com.xiaoyu.com.xueba:id/tv_search'))
        return self
    def get_techerlist(self):
        pass
    def get_studentlist(self):
        return self.finds(('xpath','//*[@resource-id="com.xiaoyu.com.xueba:id/cl_student"]//*[@resource-id="com.xiaoyu.com.xueba:id/cl_root"]'))
    def add_friend(self):
        self.click(('xpath','//*[@resource-id="com.xiaoyu.com.xueba:id/rv_student"]/*[1]/*[@text="添加好友"]'))
        self.sendkeys(('id','com.xiaoyu.com.xueba:id/et_greeting_input'),'哈哈哈')
        sleep(3)
        self.click(('id','com.xiaoyu.com.xueba:id/ig_close'))
        return self
    def more_results(self):
        self.click(('id','com.xiaoyu.com.xueba:id/cl_student_more'))
        return self.finds(('id','com.xiaoyu.com.xueba:id/cl_root'))


