'''
纯web测试
环境准备（参考：https://blog.csdn.net/xmy0501/article/details/110009725）
    手机端：
        被测浏览器(可以是手机自带浏览器，不可以使用第三方浏览器)：
        iOS：Safari、Chrome
        android：Chromium(Chrome开源版本)、Browser
    PC端：
        安装Chrome浏览器(或chromium)，并且能登录https://www.google.com/
        下载对应手机浏览器对应的driver版本：
            国内镜像地址：https://npm.taobao.org/mirrors/chromedriver/
            appium github:https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/web/chromedriver.md
    客户端代码：
        desirecapability
            “browser” = “Browser” 或 “browser” = “Chrome” (不需要app package和app activity)
            “chromedriverExecutable” = “指定driver地址”
            Chromedriver默认地址：which appium 查找appium安装目录
                //appium/node_modules/appium-chromedriver/chromedriver/mac
                \\appium\node_modules\appium-chromedriver\chromedriver\win
    adb命令:
        获取手机内所有安装包包名：   adb shell pm list package
        获取手机浏览器包名：        adb shell pm list package | grep browser
        获取浏览器版本：           adb shell pm dump 应用包名 | grep version
chrome inspector进行元素定位
----------------------------------------
混合页面测试
环境准备
    PC:
        浏览器能访问https://www.google.com
        chromedriver下载对应版本
            https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/web/chromedriver.md
    手机端：
        应用代码需要打开webview开关
    代码：
        appPackage,appActivity
        desirecapability里添加：chromedriverExecutable:driver路径
上下文（类似web的句柄）
    driver.contexts     获取所有上下文，返回是一个列表
    driver.switch_to.context(driver.contexts[-1])     切换到最后一个上下文
获取webview版本
    adb shell pm dump webview | grep version

微信小程序测试（不建议使用官方自动化框架：https://developers.weixin.qq.com/miniprogram/dev/devtools/auto/）
运行环境
    在iOS上：小程序逻辑层的 javascript 代码运行在 JavaScriptCore 中，视图层是由 WKWebView来渲染的，环境有 iOS8、iOS9、iOS10
    在Android上：
        旧版本，小程序逻辑层的 javascript 代码运行中 X5 JSCore 中，视图层是由 X5 基于 Mobile Chrome 57内核来渲染的
        新版本，小程序逻辑层的 javascript 代码运行在 V8 中，视图层是由自研 XWeb 引擎基于 Mobile Chrome 67内核来渲染的
    在开发工具上，小程序逻辑层的 javascript 代码是运行在 NW.js 中，视图层是由 Chromium 60 Webview来渲染的
自动化测试关键步骤（参考6-14 微信小程序测试）
    设置chromedriver正确版本
    设置chrome option传递给chromedriver
        caps['chromeOptions'] = {'androidProcess': 'com.tencent.mm:appbrand0'}  --小程序的地址
        caps['adbPort'] = 5038
    使用adb proxy解决fix chromedriver的bug       参考https://ceshiren.com/t/topic/3994

appium设备交互api（官方文档：http://appium.io/docs/en/commands/device/network/send-sms/）
    来短信：self.driver.send_sms('555-123-4567', 'Hey lol')
    来电话：self.driver.make_gsm_call('5551234567', GsmCallActions.CALL)
    来电话：self.driver.set_network_connection(connection_type)

模拟器控制(只能用android studio创建的虚拟模拟器avd)
    获取模拟器列表     emulator -list-avds
    设置模拟器        desire_caps['avd']='模拟器名字'

capibility进阶使用（官网文档：http://appium.io/docs/en/writing-running-appium/caps/index.html）
newCommandTimeout       新命令的超时时间（默认是60s）
udid                    指定设备运行（默认是设备列表的第一个设备）
autoGrantPermissions    设备权限（默认是False）
noReset                 不重置app
                        Android:Do not stop app, do not clear app data, and do not uninstall apk
                        IOS:Do not destroy or shut down sim after test. Start tests running on whichever sim is running, or device is plugged in
fullReset               重置app
                        Android:Stop app, clear app data and uninstall apk before session starts and after test
                        IOS:Uninstall app before and after real device test, destroy Simulator before and after sim test. They happen only before if resetOnSessionStartOnly: true is provided
dontStopAppOnReset      在运行是不要先关掉app（正常在运行时会先关闭app进程再重新启动）

android webview技术原理（参考：https://blog.csdn.net/qq_38870503/article/details/109454376）
    多看视频6-18

appium问题定位分析
    appium -g xx.log    保存日志信息（appium -g xx.log|tee）
    [http] -->          发出了http的请求
    [http] <--          接收了http的响应

appium原理与JsonWP协议分析（官网文档：http://appium.io/docs/en/about-appium/appium-clients/）
    session_id创建：
        curl -l -H "Content-type:application/json" -X POST -d '{"desiredCapabilities":{"platformName":"Android","deviceName":"device","platformNameVersion":"6.0","appPackage":"com.xueqiu.android","appActivity":".common.MainActivity"}}' 'http://127.0.0.1:4723/wd/hub/session'
    session_id获取：
        session_id=$(curl 'http://127.0.0.1:4723/wd/hub/sessions' \ | awk -F\" '{print $}')
    element_id获取：
        curl -X POST http://127.0.0.1:4723/wd/hub/session/$session_id/elements --data-binary '{"using":"xpath","value":"$xpath表达式"}' -H "Content-type:application/json;charset=UTF-8"
    元素属性获取：
        curl http://127.0.0.1:4723/wd/hub/session/$session_id/element/$element_id/attribute/${属性名}
    元素动作(例如：点击)：
        curl -X POST curl -X POST http://127.0.0.1:4723/wd/hub/session/$session_id/element/$element_id/click

appium源代码解析
    参考文档：http://appium.io/docs/en/contributing-to-appium/appium-packages/
    参考学习视频6-21

 appium二次封装
    自定义appium server
    重新编译Uiautomator

测试框架设计思想（教学代码地址：https://github.com/yuruotong1/ui_framework）
    视频6-32进行了总结
        测试数据的数据驱动
        测试步骤的数据驱动
        自动化异常处理机制
        通用测试用例封装

pageobject改造
    base_page
    app
    main
    other

自动化异常处理机制
    弹窗问题：利用try catch 捕获异常，异常处理弹窗（黑名单），关闭掉之后重新调用自身方法

通用测试用例封装
    使用TestBase封装通用测试用例
    使用fixture


'''