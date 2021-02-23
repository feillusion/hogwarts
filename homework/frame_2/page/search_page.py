from homework.frame_2.base_page import BasePage
from homework.frame_2.page.result_page import ResultPage
from homework.frame_2.run_steps import run_steps


class SearchPage(BasePage):

    #搜索指定内容并点击跳转到结果页
    @run_steps
    def search(self,search,click,page_path=None,method=None):
        if page_path is None:
            return '../page/search_page.yaml'
        if method is None:
            return 'search'
        # self.sendkeys(('xpath','//*[@resource-id="com.xueqiu.android:id/search_input_text"]'),f'{search}')
        # self.click(('xpath',f'//*[@resource-id="com.xueqiu.android:id/code" and @text="{click}"]'))
        return ResultPage(self.driver)