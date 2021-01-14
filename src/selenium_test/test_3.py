from time import sleep

from src.selenium_test.base import Base


class TestTraining(Base):

    def test_js(self):
        self.driver.get("https://www.12306.cn/index/")
        sleep(2)
        train_date = self.driver.find_element_by_xpath("//input[@id='train_date']")
        self.driver.execute_script("train_date.removeAttribute('readonly')")
        self.driver.execute_script("train_date.value='2020-12-30'")
        sleep(2)
        self.driver.execute_script("a=document.getElementById('search_one').text;window.alert(a)")
        sleep(1)
        print(self.driver.switch_to.alert.text)
        self.driver.switch_to.alert.accept()
        sleep(1)
        self.driver.find_element_by_id('search_one').click()

