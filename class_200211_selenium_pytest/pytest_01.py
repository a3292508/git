#!usr/bin/env python
#-*- coding:utf-8 -*-

#pytest框架：基于unittest之上的单元测试框架

#1.自动发现测试模块和测试方法；
#2.断言使用assert + 表达式即可；
#3.可以设置会话级/模块级/类级/函数级的fixtures
#4.有丰富的插件库，目前在500+以上

#安装命令：pip install pytest
#安装html报告的插件：pip install pytest-html
#插件地址：http://plugincompat.herokuapp.com/

#pytest收集测试用例的规则：
#1.默认当前目录中搜索测试用例，即在哪个目录下运行pytest命令，则从哪个目录当中搜索；
#2.搜索规则：
#（1)符合命名规则test_*.py或者*_test.py的文件
#（2）以test_开头的函数名
#（3）以Test开头的测试类（没有__init__函数）当中，以test_开头的函数

#pytest-mark
#对测试用例打标签，在运行测试用例的时候，可根据标签名来过滤运行的用例
#使用方法：
#在测试用例/测试类前面加上：@pytest.mark.标记名
#可在一个用例上打多个标签，多次使用@pytest.mark.标签名即可

#pytest命令行:pytest --help(查看所有命令)
#运行有特定标签的用例：pytest -m 标签名
#运行所有的用例：pytest（直接使用pytest,会按顺序自动查找用例)

#pytest用例执行顺序是按从上到下的顺序执行，因此可以通过调整用例顺序，或改变文件名称来实现自己的目的！！！

#pytest-定义fixture
# fixture：即测试用例执行的环境准备和清理，在unit test中即指setup/teardown/setupClass/teardownClass
#fixture主要的目的是为了提供一种可靠和可重复性的手段去运行那些最基本的测试内容。比如在测试网站的功能时，每个测试用例都要登录和退出，
#利用fixture就可以只做一次，否则每个测试用例都要做这2步。
#1.定义fixture：
#把一个函数定义为fixture很简单，在函数声明之前加上@pytest.fixture，表示此函数为测试环境数据的准备和清理。
#在一个fixture内部如何区分环境准备和环境清理：在函数内部使用yield关键字。yield关键字以后的代码，就是环境清理的代码，即在测试用例
#执行完成之后会执行的代码
#2.conftest.py 配置里可以实现数据共享，不需要import就能自动找到一些配置。需要和测试用例放在同一文件夹

#pytest-参数化
#在测试用例的前面加上：@pytest.mark.parametrize("参数名",列表数据)
#参数名：用来接收每一项数据，并作为测试用例的参数
#列表数据：一组测试数据

#pytest-重运行机制（需要装插件）
# 插件名称：rerunfailures
#安装方法：pip install pytest-rerunfailures
#使用方式：命令行参数形式
#命令：pytest --reruns 重试次数
#命令：pytest --reruns 重试次数 --reruns-delay 次数之间的延时设置（单位：秒）---表示失败的用例可以重新运行2次，间隔时间为5秒

#pytest-测试报告（需要装插件pytest-html）
# pytest可以生成多种样式的结果：
#1.生成JunitXML格式的测试报告：命令：--junitxml=相对路径
#2.生成result log格式的测试报告：命令：--resultlog=report\log.txt
#3.生成Html格式的测试报告：命令：--html=report\testReport.html

#命令举例：pytest -m smoke --reruns 2 --reruns-delay 5 -s --junitxml=Report/report/report.xml --html=Report/report/report.html

#Master/Slave模式：

# pytest-allure报告