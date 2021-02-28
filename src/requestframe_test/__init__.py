'''
接口测试框架 requests
    演练环境：https://httpbin.testing-studio.com/

    jsonpath
    xmlpath(xpath)
    hamcrest断言：https://github.com/hamcrest/PyHamcrest
    schema断言：https://jsonschema.net

    http basic
        from requests.auth import HTTPBasicAuth
        import requests
        requests.get(url,auth=HTTPBasicAuth(username,password))

    基于加密接口的测试用例设计
        1.对响应加密的接口。发起一个get请求后，得到一个加密过后的响应信息
        2.准备加密文件：
            base64算法加密过后的文件：https://ceshiren.com/t/topic/2094
                2.1.创建一个demo.json文件
                2.2.使用base64 demo.json >demo.txt命令
        3.使用python命令在有加密文件的目录启动一个服务
            python -m http.server 9999
        4.访问该网站：127.0.0.1:9999/demo.txt(模拟请求，返回的是base64加密后的信息)
        5.对返回的内容进行解密：base64.b64decode(res.content)

'''