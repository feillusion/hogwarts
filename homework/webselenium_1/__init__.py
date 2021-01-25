# 复用浏览器
# 进入浏览器的安装地址
# 使用命令开启调试窗口  chrome --remote-debugging-port=9222 (9222为端口号，可以换成任意一个没有被占用的端口)
# python代码
# chrome_args = webdriver.ChromeOptions()
# chrome_args.debugger_address = "127.0.0.1:9222"
# driver = webdriver.Chrome(options=chrome_args)

# 读取/设置浏览器cookies
# 读取        cookies = driver.get_cookies()
# 添加        cookies = driver.add_cookie(cookie_dict)
# 删除特定     cookies = driver.delete_cookie(name)
# 删除所有     cookies = driver.delete_all_cookies()


# json
# 读取json内容
# cookies = json.load(dict)
# 存储json内容
# cookies = json.dump(json,dict)
# 把一行内容换成易读的  ctrl+alt+l