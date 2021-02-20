'''
appium 生态工具
adb：安卓的控制工具，用于获取安卓的各种数据和控制
appium desktop:内嵌了appium server 和 inspector的综合工具
appium server: appium的核心工具，命令行工具
appium client: 各种语言的客户端封装库，用于连接appium server
appium crawler:自动遍历工具

环境安装
Java 1.8版本
    官网下载安装
    配置环境变量(windows)
        JAVA_HOME  jdk目录
        classpath  .;%JAVA_HOME%\lib\dt.jar;%JAVA_HOME%\lib\tools.jar  (最前面加.和;)
        path  %JAVA_HOME%\bin;%JAVA_HOME%\jre\bin
    检查是否成功：命令行输入 java

Android SDK
    官网下载安装(其实就是个文件夹，下载后手动更新，配置环境变量，不需要安装):http://tools.android-studio.org/index.php/sdk
    配置环境变量
        ANDROID_HOME sdk目录
        PATH %ANDROID_HOME%\tools;%ANDROID_HOME%\platform-tools
    检查是否成功：命令行输入 adb 或 adb shell

Node js(>=10版本),npm(>=6版本)
python 3

appium-desktop(appium server+appium inspector工具)
    下载对应操作系统安装包：https://github.com/appium/appium-desktop/releases
    如果不需要appium inspector,也可以通过npm直接安装appium
        官方：npm install -g appium
        淘宝：npm install -g cnpm --registry=https://registry.npm.taobao.org
            cnpm install -g appium
        运行：appium

appium python client
    方式一：pip install appium-python-client
    方式二：下载源码包
        下载地址：https://github.com/appium/python-client
                https://pypi.python.org/pypi/appium-python-client
        解压后命令行进入python-client-master目录，该目录下包含setup.py文件
        执行命令python setup.py install 命令安装客户端

安装appium-doctor检测appium的安装环境
    cnpm install appium-doctor
    命令行执行 appium-doctor

adb devices  获取当前终端连接的设备
app信息
adb shell dumpsys activity top  获取当前界面元素
adb shell dumpsys activity activities   获取任务列表
app入口
adb logcat | grep -i displayed  启动app,根据句日志获取appPackage 和 appActivity
aapt dump badging mobike.apk | grep launchable-activity
启动应用
adb shell am start -W -n appPackage/.appActivity -S


测试用例的重要部分
导入依赖：from appium import webdriver
capabilities设置
初始化driver: python webdriver.remote
饮食等待，增强用例的稳定性
元素定位与操作 find+action
断言 assert

capability 设置 ---官方文档https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/caps.md
app apk 地址
appPackage 包名
appActivity Activity名字
automationName 默认使用uiautomator2 (andorid默认使用uiautomator2,IOS默认使用XCUITest)
noReset fullReset 是否在测试前后重置相关环境 (例如首次打开弹窗，登录信息等)
unicodeKeyBoard resetKeyBoard 是否需要输入非英文之外的语言并在测试完成后重置输入法
dontStopAppOnReset 首次启动的时候，不停止app
skipDeviceInitialization 跳过安装，权限设置等操作

appium元素定位
driver.find_element_by_id(resource-id)
driver.find_element_by_accessibility_id(content-desc)
driver.find_element_by_xpath(xpath属性值)

强制等待：sleep()
隐式等待：driver.manage().timeouts().implicitlyWait(10,TimeUnit.SECONDS)  在服务端等待
显式等待：Element = WebDriverWait(driver,10,0.5).until(expected_conditions.visibility_of_element_located((MobileBy.ID,"com.android.settings:id/title")))  在客户端等待

android 基础知识
android是通过容器的布局属性来管理子控件的位置关系，布局过程就是把界面上的所有控件根据他们的间距大小摆放在正确的位置
android七大布局：
    线性布局（LInearLayout）
    相对布局（RelativeLayout）
    帧布局（FrameLayout）
    表格布局（TableLayout）
    绝对布局（absoluteLayout）
    网格布局（GridLayout）
    约束布局（ConstraintLayout）
android四大组件：
    activity   与用户交互的可视化界面
    service    实现程序后台运行的解决方案
    content provider    内容提供者，提供程序所需要得数据
    broadcast receiver   广播接收器，监听外部事件的到来（比如来电）
常用的控件
    TextView(文本控件)，EditText(可编辑文本控件)
    Button(按钮)，ImageButton(图片按钮)，ToggleButton(开关按钮)
    ImageView(图片控件)
    CheckBox(复选框控件),RadioButton(单选框控件)


IOS基础知识
布局：IOS去掉了布局的概念，直接用变量之间的相对关系完成位置的计算
开发环境：
    系统：MacOS X
    开发工具：Xcode
    开发语言：ObjectC
    安装文件：.ipa文件/.app文件
元素定位：实际上就上定位控件


控件基础知识
dom: Document Object Model 文档对象模型
dom应用: 最早应用于html和js的交互。用于表示界面的控件层级，界面的结构化描述，常见的格式为html/xml。核心元素为节点和属性
xpath：xml路径语言，用于xml中的节点定位
Android应用的层级结构与html不一样，是一个定制的xml
app source类似于dom，表示app的层级，代表了界面里面所有的控件树的结构
每个控件都要它的属性(resourceid,xpath,aid)，没有css属性


定位工具
uiautomatorviewer(only for android)
Appium inspector

元素常用方法
点击方法        element.click()
输入操作        element.send_keys("words")
设置元素的值     element.set_value("words")
清除操作        element.clear()
是否可见        element.is_displayed()  返回True/False
是否可用        element.is_enabled()  返回True/False
是否被选中      element.is_selected()  返回True/False
获取属性值      get_attribute(name)

元素常用属性
获取元素文本      element.text
获取元素坐标      element.location   结果：{'y':11,'x':14}
获取元素尺寸      element.size       结果：{'width':11,'height':14}
获取屏幕尺寸      driver.get_window_size()
获取元素文本      element.text

触屏操作
TouchAction用法--常用
TouchAction(driver).行为1.行为2...perform()
按压  press(WebElement el, int x, int y)      可以传元素，也可以传坐标
释放  release()      结束按压
执行  perform()      执行操作
长按  longPress(WebElement el, int x, int y, Duration duration)      类似按压，不过多了个按压时长的参数（单位ms）
点击  tap(WebElement el, int x, int y)      类似按压
移动  move_to(WebElement el, int x, int y)      类似按压
暂停  wait(1000)      暂停脚本，单位ms

高级定位技巧
xpath定位：类似selenium，参考：https://www.w3school.com.cn/xpath/xpath_syntax.asp
uiautomator定位：安卓工作引擎，定位速度快，但书写复杂，参考：https://stuff.mit.edu/afs/sipb/project/android/docs/tools/help/uiautomator/UiSelector.html
    用法：driver.find_element_by_android_uiautomator(表达式).click()
    表达式如下：
        通过resourceId定位： new UiSelector().resourceId("id")
        通过classname定位： new UiSelector().classname("classname")
        通过content-des定位： new UiSelector().description("content-des属性")
        通过text文本定位：
            通过text文本精准定位： new UiSelector().text("text文本")
            通过text文本模糊定位： new UiSelector().textContains("包含的text文本")
            通过text文本开头定位： new UiSelector().textStartsWith("text文本开头内容")
            通过text文本正则定位： new UiSelector().textMatches("正则表达式")
        组合定位：new UiSelector().resourceId("id").classname("classname").text("text文本")
        父子定位：new UiSelector().resourceId("id").childSelector(text("text文本"))
        兄弟定位：new UiSelector().resourceId("id").fromParent(text("text文本"))
        滚动查找：new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("text文本").instance(0));

显示等待机制
强制等待：sleep(10)
隐式等待：全局，在服务端等待，implicitly_wait(10)
显式等待：在客户端等待，WebDriverWait(driver,10).until(expected_conditions.visibility_of_element_located(LOCATOR))
    WebDriverWait()搭配until()或until_not()方法使用：
        locator=(MobileBy.XPATH,"xpath表达式")
        WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable(locator))
        driver.find_element(*locator).click()

toast定位
必须使用XPATH定位：
    //*[@class='android.widget.Toast']
    //*[contains(@text,'xxxxxx')]
设置里添加‘automationName’:'uiautomator2',安卓默认就是这个，可以不加

属性获取
element.get_attribute('属性名')

断言
assert expression       expression==True时通过，False时抛出异常
hamcrest    有较多的匹配器，功能比较多
    第三方库，需要安装pyhamcrest,官方文档：https://github.com/hamcrest/PyHamcrest

参数化--同selenium
@pytest.mark.parametrize()

数据驱动（yaml,json,excel,CSV）
!!!有时间复现一下6-12的代码
yaml:
    获取yaml文件内容：steps=yaml.safe_load(open(yaml文件路径))

Android webview测试
----------------------------------------
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