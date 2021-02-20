'''
环境准备
    Appium建议1.15
    Java 1.8
    SDK build-tools/ 下对应的版本，需要使用<=29的版本

获取app的包名、activity
    mac：
        adb logcat "ActivityManager:I *:s" | grep "cmp"
    win：
        adb logcat ActivityManager:I *:s | findstr "cmp"

测试步骤三要素
    定位，交互，断言

定位
    ID定位（优先级最高）
    XPath定位（速度慢，定位灵活）
    Accessibility ID定位（content-desc）
    Uiautomator 定位（速度快，语法复杂）

常用定位
    //*[contains(@resource-id, ‘login’)]（重点）
    //*[@text=‘登录’]  （重点）
    //*[contains(@resource-id, ‘login’) and contains(@text, ‘登录’)] （重点）

# 设置页面等待空闲状态的时间为0秒（动态刷新默认为10000ms，不设置的话对于动态刷新的页面（例如时间不停刷新）会等待10s才开始定位元素）
    caps['settings[waitForIdleTimeout]'] = 0


'''