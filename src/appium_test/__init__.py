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