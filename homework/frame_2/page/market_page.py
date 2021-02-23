from homework.frame_2.base_page import BasePage
from homework.frame_2.page.search_page import SearchPage
from homework.frame_2.run_steps import run_steps


class MarketPage(BasePage):

    #跳转到搜索页
    @run_steps
    def goto_search(self,page_path=None,method=None):
        if page_path is None:
            return '../page/market_page.yaml'
        if method is None:
            return 'goto_search'
        return SearchPage(self.driver)