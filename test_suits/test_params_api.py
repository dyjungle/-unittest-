# coding:utf-8
import unittest
import json
# import randon
import requests
from base_data import BaseData

#接口间参数传递
class Modulelist(unittest.TestCase):
    def setUp(self):
        po = BaseData()
        self.url = po.get_httpbinurl()
        self.header = {
            "Accept": "application/json",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Host": "www.httpbin.org",
            "Pragma": "no-cache",
            "Referer": "http://www.httpbin.org/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36",
            "X-Amzn-Trace-Id": "Root=1-5eba420e-39301330ccf9764010fcab10"
          }
    #获取菜单中所有标签数据，也就是接口返回数据
    def get_all_label(self):
        url = self.url + '/get'
        data = {
            "username": "dengyi",
            "password": "111111",
            "page": "1",
            "rows": "10",
            "sort": "labelStatus",
            "order": "asc",
            "labelStatus": 0
        }

        #获取返回数据，并转换为字典格式
        response = requests.get(url, params=data, headers=self.header)
        data = json.loads(response.content)
        # print(data)

        try:
            self.assertIn("args", data)#验证“row”是data的子串
            # self.assertIn("total", data)
            if data["args"]:
                labels = [] #定义一个列表存查询到的所有标签数据
                # for t in data["args"]:#以列表中嵌套字典的格式保存，易于调用
                #     # if t['username']:#如果labelstatus为0则追加到列表中
                #     #     使用上述方法获取username报错string indices must be integers
                # print(data["args"])
                # print(data["args"]['username'])
                if data["args"]['username']:
                    #如果用户名不为空，将该接口数据存储为字典
                    labels.append(
                        {"username": data["args"]['username'],
                         "password": data["args"]['password'],
                         "page": data["args"]['page'],
                         "rows": data["args"]['rows'],
                         "sort": data["args"]['sort'],
                         "order": data["args"]['order'],
                        })
                print("labels", labels)
                return labels
            else:
                labels = None
                return labels
        except Exception as e:
            print("请求url：", response.url)
            print("请求参数：", data)
            raise e
    #新增草稿，将获取到的参数添加到草稿
    def add_draft(self, username, password):
       url = self.url + '/post'
       data = {
            "username": username,
            "password": password,
       }
       response = requests.post(url, data=data, headers=self.header)
       data = response.json()

       try:
           self.assertEqual(response.status_code, 200)

       except Exception as e:
           print("请求url：", response.url)
           print("请求参数：", data)
           raise e

    def test01(self):
        try:
            labels = self.get_all_label()
            #调用查询接口数据的方法
            if labels:
                username = labels[0]["username"]
                password = labels[0]["password"]
                data = self.add_draft(username, password)
                # print("使用的用户名：", username + ";使用的密码：", password + ";返回的草稿数据：", data["data"])
                print("post接口--使用的用户名：{}，使用的密码：{}".format(labels[0]["username"], labels[0]["password"]))

            elif labels is None:
                print("get接口无可用数据，请先增加数据")

        except Exception as e:
            print("错误详情：", e)
            raise

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Modulelist('test01'))
    runner = unittest.TextTestRunner()
    runner.run(suite)


