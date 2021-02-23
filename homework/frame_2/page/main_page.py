from homework.frame_2.base_page import BasePage
from homework.frame_2.page.market_page import MarketPage
from homework.frame_2.run_steps import run_steps


class MainPage(BasePage):

    #跳转到行情页
    @run_steps
    def goto_market(self,page_path=None,method=None):
        if page_path is None:
            return '../page/main_page.yaml'
        if method is None:
            return 'goto_market'
        return MarketPage(self.driver)