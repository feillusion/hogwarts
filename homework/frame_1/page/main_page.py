from homework.frame_1.base_page import BasePage


class MainPage(BasePage):

    def goto_market(self):
        #手动点击跳转模拟异常弹窗，方便练习
        self.click(('xpath','//*[@resource-id="com.xueqiu.android:id/post_status"]'))
        #点击行情tab
        self.click(('xpath','//*[@resource-id="com.xueqiu.android:id/tab_name" and @text="行情"]'))
        #MarketPage未创建，先不返回
        #return MarketPage(self.driver)