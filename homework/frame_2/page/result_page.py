from homework.frame_2.base_page import BasePage
from homework.frame_2.run_steps import run_steps


class ResultPage(BasePage):

    #获取并返回结果列表
    @run_steps
    def get_result(self,page_path=None,method=None):
        if page_path is None:
            return '../page/result_page.yaml'
        if method is None:
            return 'get_result'
        #result = self.gettexts(('xpath','//*[@resource-id="com.xueqiu.android:id/stockCode"]'))