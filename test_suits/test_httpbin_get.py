# coding:utf-8
import unittest
from common_utils.send_request import RunMethod
import json
from base_data import BaseData

run = RunMethod()
class Test(unittest.TestCase):
    """验证http://www.httpbin.org/get接口"""
    @classmethod
    def setUpClass(cls):
        #实例化对象
        po = BaseData()
        #获取配置文件中的httpbinurl 并拼接get 作为新url
        cls.url = po.get_httpbinurl() + "/get"

    @classmethod
    def tearDownClass(cls):
        pass

    def test01(self):
        """参数正常"""
        print("test01 start...")
        data = {"user": "dengyi", "password": "666666"}
        print(self.url)
        r = run.run_main("GET", self.url, data)
        res = r.json()
        print(json.dumps(res, indent=2, sort_keys=False, ensure_ascii=False))
        self.assertEqual(200, r.status_code)
        self.assertNotEqual([], res["args"])#判断datalist不为空
        print("test01 end...")

#测试单个测试用例是否能执行成功
if __name__ == '__main__':
    #调用unittest的TestSuite()，理解为管理case的一个容器（测试套件）
    suite = unittest.TestSuite()
    #向测试套件中添加用例
    suite.addTest(Test('test01'))
    #加载测试用例
    runner = unittest.TextTestRunner(verbosity=1)
    #执行测试用例
    runner.run(suite)