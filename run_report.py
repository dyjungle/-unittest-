# coding:utf-8
import unittest
from HTMLTestReportCN import *
import time, os
from function import *

#获取当前脚本路径
root_dir = os.path.dirname(os.path.abspath(__file__))
#根据项目路径，拼接用例路径
case_dir = root_dir + '/test_suits'
report_dir = root_dir + '/reports'
print(root_dir)
print(root_dir)

#加载测试用例文件
suits = unittest.defaultTestLoader.discover(case_dir, pattern='test_*', top_level_dir=None)
#加载测试用例
suit = unittest.TestLoader().discover(case_dir)
"""
1.case_dir即测试用例所在目录
2.pattern='test_*.py' ：表示用例文件名的匹配原则，“*”表示任意多个字符
3.top_level_dir=None：测试模块的顶层目录。如果没顶层目录（也就是说测试用例不是放在多级目录
中），默认为 None
"""
if __name__ == '__main__':
    now_time = time.strftime("%Y-%m-%d %H-%M-%S")
    filename = root_dir + '/reports/' + now_time + '_result.html'

    with open(filename, 'wb') as fp:
        """使用withopen操作文件"""
        runner = HTMLTestRunner(stream=fp, title='httpbin接口测试报告', description='接口测试结果如下：')
        runner.run(suits)

    print("find latest report")
    latest_report = latest_report(report_dir)
    print("send email report..")
    send_mail(latest_report)