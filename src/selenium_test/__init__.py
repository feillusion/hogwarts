# selenium安装
# python库  selenium
# 浏览器对应的driver，driver路径配置到环境变量


# 直接等待：time.sleep(5) 等待5s
# 隐式等待：driver.implicitly_wait(5)  隐式等待5s（每0.5s轮询，找到元素则跳过等待，超过5s返回超时）
# 显示等待：‘WebDriveraWait’ 配合 until()和 until_not()   执行显示等待，直到满足条件后继续往下执行
#           WebDriveraWait(driver,5).until(aaa)        显示等待5s直到 aaa 为True


# 使用selenium
# from selenium import webdriver
# driver = webdriver.Chrome()   创建一个chrome浏览器实例
# driver = webdriver.Firefox()  创建一个firefox浏览器实例
# driver.maximize_window()      浏览器实例窗口最大化
# driver.implicitly_wait(5)     浏览器实例设置隐式等待5s
# driver.get(url)               打开一个网址
# element.click()               点击某个元素
# element.send_keys()           点击某个元素

# web控件定位
# find_element(By.ID,'{id}')    通过id定位
# find_element_by_xpath()

