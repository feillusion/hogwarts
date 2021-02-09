'''
安装allure
包下载：https://repo1.maven.org/maven2/io/qameta/allure/allure-commandline/2.13.7/
解压->进入bin目录->运行allure.bat
把bin目录添加到PATH环境变量
python安装allure-pytest包


使用allure
pytest filename.py  --alluredir=dirpath  执行结果存放在dirpath下
allure serve dirpath   启动服务并对dirpath下的数据生成报告，会直接打开默认浏览器查看，不会保存报告
pytest filename.py -s -q --alluredir=dirpath   在测试执行期间收集结果
allure generate dirpath -o reportpath --clean 把dirpath下的数据生成报告，存放在reportpath下，--clean用于覆盖
allure open -h 127.0.0.1 -p 8883 reportpath   打开reportpath下的报告查看


allure常用特性
功能上加 @allure.feature('功能名称')
子功能上加 @allure.story('子功能名称')
步骤上加 @allure.step('步骤细节')
with allure.step('步骤细节'):  可以用在测试用例方法里，测试步骤放在with里面
@allure.attach('具体文本信息')，需要附加的信息，可以是数据，文本，图片，视频，网页
pytest filename.py --allure_features '功能名称' --allure_stories '子功能名称'  执行特定功能的用例

allure用例加链接
关联bug：--allure-link-pattern=issue:url/{}
@allure.issue('{id}','textname')
@allure.testcase(url,'casetitle')
@allure.link(url,name='XXXX')

allure用例加重要级别
@allure.severity(allure.severity_level.TRIVIAL)
Blocker/critical/Normal/Minor/Trivial
执行  pytest -sv 文件名 --allure-severities normal,critical

allure在测试报告里附加网页
@allure.attach(body,name,attachment_type,extension)
eg: @allure.attach('<head></head><body>首页</body>',‘这是错误页’,allure.attchment_type.HTML)
allure在测试报告里附加网页
@allure.attach.file(source,name,attachment_type,extension)
eg: @allure.attach.file('./result/a.png',‘这是错误页’,attachment_type=allure.attachment_type.PNG)
'''