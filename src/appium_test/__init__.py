# appium 生态工具
# adb：安卓的控制工具，用于获取安卓的各种数据和控制
# appium desktop:内嵌了appium server 和 inspector的综合工具
# appium server: appium的核心工具，命令行工具
# appium client: 各种语言的客户端封装库，用于连接appium server
# appium crawler:自动遍历工具

# 环境安装
# Java 1.8版本
    #官网下载安装
    #配置环境变量(windows)
        #JAVA_HOME  jdk目录
        #classpath  .;%JAVA_HOME%\lib\dt.jar;%JAVA_HOME%\lib\tools.jar  (最前面加.和;)
        #path  %JAVA_HOME%\bin;%JAVA_HOME%\jre\bin
    #检查是否成功：命令行输入 java

# Android SDK
    #官网下载安装(其实就是个文件夹，下载后手动更新，配置环境变量，不需要安装)
    #配置环境变量
        #ANDROID_HOME sdk目录
        #PATH %ANDROID_HOME%\tools;%ANDROID_HOME%\platform-tools
    #检查是否成功：命令行输入 adb 或 adb shell

# Node js(>=10版本),npm(>=6版本)
# python 3

# appium-desktop(appium server+appium inspector工具)
    #下载对应操作系统安装包：https://github.com/appium/appium-desktop/releases
    #如果不需要appium inspector,也可以通过npm直接安装appium
        # 官方：npm install -g appium
        # 淘宝：npm install -g cnpm --registry=https://registry.npm.taobao.org
            # cnpm install -g appium
        # 运行：appium

# appium python client
    #方式一：pip install appium-python-client
    #方式二：下载源码包
        #下载地址：https://github.com/appium/python-client
                #https://pypi.python.org/pypi/appium-python-client
        #解压后命令行进入python-client-master目录，该目录下包含setup.py文件
        #执行命令python setup.py install 命令安装客户端

# 安装appium-doctor检测appium的安装环境
    #cnpm install appium-doctor
    #命令行执行 appium-doctor

# adb devices  获取当前终端连接的设备
# app信息
# adb shell dumpsys activity top  获取当前界面元素
# adb shell dumpsys activity activities   获取任务列表
# app入口
# adb logcat | grep -i displayed  启动app,根据句日志获取appPackage 和 appActivity
# aapt dump badging mobike.apk | grep launchable-activity
# 启动应用
# adb shell am start -W -n appPackage/.appActivity -S


# 测试用例的重要部分
# 导入依赖：from appium import webdriver
# capabilities设置
# 初始化driver: python webdriver.remote
# 饮食等待，增强用例的稳定性
# 元素定位与操作 find+action
# 断言 assert

# capability 设置 ---官方文档https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/caps.md
# app apk 地址
# appPackage 包名
# appActivity Activity名字
# automationName 默认使用uiautomator2 (andorid默认使用uiautomator2,IOS默认使用XCUITest)
# noReset fullReset 是否在测试前后重置相关环境 (例如首次打开弹窗，登录信息等)
# unicodeKeyBoard resetKeyBoard 是否需要输入非英文之外的语言并在测试完成后重置输入法
# dontStopAppOnReset 首次启动的时候，不停止app
# skipDeviceInitialization 跳过安装，权限设置等操作

# appium元素定位
# driver.find_element_by_id(resource-id)
# driver.find_element_by_accessibility_id(content-desc)
# driver.find_element_by_xpath(xpath属性值)

# 强制等待：sleep()
# 隐式等待：driver.manage().timeouts().implicitlyWait(10,TimeUnit.SECONDS)  在服务端等待
# 显式等待：Element = WebDriverWait(driver,10,0.5).until(expected_conditions.visibility_of_element_located((MobileBy.ID,"com.android.settings:id/title")))  在客户端等待

# android 基础知识
# android是通过容器的布局属性来管理子控件的位置关系，布局过程就是把界面上的所有控件根据他们的间距大小摆放在正确的位置
# android七大布局：
    # 线性布局（LInearLayout）
    # 相对布局（RelativeLayout）
    # 帧布局（FrameLayout）
    # 表格布局（TableLayout）
    # 绝对布局（absoluteLayout）
    # 网格布局（GridLayout）
    # 约束布局（ConstraintLayout）
# android四大组件：
    # activity   与用户交互的可视化界面
    # service    实现程序后台运行的解决方案
    # content provider    内容提供者，提供程序所需要得数据
    # broadcast receiver   广播接收器，监听外部事件的到来（比如来电）
# 常用的控件
    # TextView(文本控件)，EditText(可编辑文本控件)
    # Button(按钮)，ImageButton(图片按钮)，ToggleButton(开关按钮)
    # ImageView(图片控件)
    # CheckBox(复选框控件),RadioButton(单选框控件)


# IOS基础知识
# 布局：IOS去掉了布局的概念，直接用变量之间的相对关系完成位置的计算
# 开发环境：
    # 系统：MacOS X
    # 开发工具：Xcode
    # 开发语言：ObjectC
    # 安装文件：.ipa文件/.app文件
# 元素定位：实际上就上定位控件


# 控件基础知识
# dom: Document Object Model 文档对象模型
# dom应用: 最早应用于html和js的交互。用于表示界面的控件层级，界面的结构化描述，常见的格式为html/xml。核心元素为节点和属性
# xpath：xml路径语言，用于xml中的节点定位
# Android应用的层级结构与html不一样，是一个定制的xml
# app source类似于dom，表示app的层级，代表了界面里面所有的控件树的结构
# 每个控件都要它的属性(resourceid,xpath,aid)，没有css属性


# 定位工具
# uiautomatorviewer(only for android)
# Appium inspector