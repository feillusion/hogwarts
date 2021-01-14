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
# find_element(By.ID,'{id}')                通过id定位(第一个参数决定查找的类型，实质上还是css_selector查找)
# find_element_by_xpath('{xpath}')          通过Xpath定位
# find_element_by_class_name('{class_name}')通过class_name定位
# find_element_by_link_text('{link_text}')  通过link_text定位
# find_element_by_id('{id}')                通过id定位
# find_element_by_css_selector('{css}')     通过css定位

# web控件交互
# ActionChains：执行PC端的鼠标点击，双击，右键，拖拽等事件
    #原理：调用方法时，不会立即执行，会把所有操作按顺序放在一个队列里，调用perform()方法时，队列中的事件一次进行
    #用法：   生成一个动作 action = ActionChains(driver)
    #        添加动作1   action.方法1
    #        添加动作2   action.方法2
    #        执行动作    action.perform()
# TouchActions：模拟PC和移动端的点击，滑动，拖拽，多点触控等多种手势
    #用法类似于ActionChains
# 处理W3C问题：
# option = webdriver.ChromeOptions()
# option.add_experimental_option('w3c',False)
# self.driver = webdriver.Chrome(options=option)

# 多窗口--句柄是窗口的身份标识
# 获取当前窗口的句柄：driver.current_window_handle
# 获取所有窗口的句柄：driver.window_handles
# 切换句柄：driver.switch_to.window({目标句柄})

# frame切换
# driver.switch_to.frame()              #根据id,name,元素对象定位切换到frame
# driver.switch_to.default_content()    #切换到默认frame
# driver.switch_to.parent_frame()       #切换到父级frame

# 选择浏览器测试
# browser = os.getenv("browser")
# if browser == 'chrome':
#   self.driver = webdriver.Chrome()
# else:
#   self.driver = webdriver.Firefox()
# 执行
# mac:     browser=chrome pytest test_selenium/test_hogwarts.py
# windows: set browser=chrome
#          pytest test_selenium/test_hogwarts.py


# 执行js脚本（一些通过selenium无法操作的动作可以通过js代码块来实现）
# 如何调用： selenium内置方法： 执行 execute_script()    返回js的返回结果 return    传参 execute_script: arguments
#   driver.execute_script("window.alert('selenium弹框测试')")
#   driver.execute_script("a = document.getElementById('kw').value;window.alert(a)")
#   driver.execute_script("return document.getElementById('kw').value")
#   时间控件赋值： a.removeAttribute("readonly")   移除元素a的readonly属性--->赋值  a.value = ‘2020-12-30’

# 文件上传
# input标签可以直接使用send_keys(文件地址)上传
# driver.find_element_by_id().send_keys(文件地址)

# 弹框处理（JS生成的alert,confirm,prompt弹框）
# switch_to.alert()定位弹框
# text: 返回alert,confirm,prompt中的文字信息
# accept(): 接受现有警告框
# dismiss(): 解散现有警告框
# send_keys(keysToSend): 发送文本至警告框。keysToSend：将文本发送至警告框

# pageobject六大原则

# The public methods represent the services that the page offers
# 公共方法表示页面提供的服务
# Try not to expose the internals of the page
# 不要暴露页面的细节
# Generally don't make assertions
# Page设计中不要出现断言，应该写在测试用例类中
# Methods return other PageObjects
# 方法应该返回其他的Page对象
# Need not represent an entire page
# 不要去代表整个page，如果一个页面中有很多功能，只需要对重点功能封装方法即可
# Different results for the same action are modeled as different methods
# 不同的结果返回不同的方法，不同的模式