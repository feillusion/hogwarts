from appium.webdriver.common.touch_action import TouchAction

from homework.appium_1.page.base_page import BasePage


class AddMember(BasePage):
    def manual_add(self):
        self.click('//*[@class="android.widget.TextView" and @text="手动输入添加"]/../..')
        return AddMember(self.driver)

    def add_member(self,name,sex,phone,deps,asserts):
        #输入姓名
        self.sendkeys('//*[@resource-id="com.tencent.wework:id/et5"]//*[@text="必填"]',name)
        #性别选择女
        self.click('//*[@text="性别" and @resource-id="com.tencent.wework:id/b7p"]/../*[@resource-id="com.tencent.wework:id/eso"]')
        sex = self.find(f'//*[@text="{sex}" and @resource-id="com.tencent.wework:id/en5"]')
        TouchAction(self.driver).tap(x=sex.location['x'],y=sex.location['y']).perform()
        #填写手机号
        self.sendkeys('//*[@resource-id="com.tencent.wework:id/fwi" and @text="手机号"]',phone)
        #选择部门
        self.click('//*[@resource-id="com.tencent.wework:id/b8g" and @text="设置部门"]/../../..')
        deps_list = self.finds('com.tencent.wework:id/h1g','id')
        for dep in deps_list:
            if dep.is_selected():
                dep.click()
        for dep_name in deps:
            locator = f'//*[@text="{dep_name}"]/../../..//*[@resource-id="com.tencent.wework:id/h1g"]'
            self.click(locator)
        self.click('//*[@resource-id="com.tencent.wework:id/h1f" and contains(@text,"确定")]')
        #保存
        save = self.find('new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("保存").instance(0));','uiautomator')
        save.click()
        if asserts == '已添加':
            return self.find('com.tencent.wework:id/bp_','id').text
        if asserts == '无效手机号':
            return self.find('com.tencent.wework:id/g5d','id').text

