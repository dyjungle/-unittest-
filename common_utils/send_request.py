# coding:utf-8
import requests
import json
from requests.exceptions import RequestException

class RunMethod:
    """定义一个执行接口的请求的类"""
    @staticmethod
    def send_get(url, data=None, header=None):
        response = requests.get(url=url, params=data, headers=header, timeout=20)
        try:
            if response.status_code == 200:
                r = response
                return r
            else:
                return None
        except RequestException:
            print("get请求失败")
            return None

    @staticmethod # 当该方法不需要用到对象中的任何资源时，可加上静态方法装饰器
    def send_post(url, data=None, header=None):
        response = requests.get(url=url, data=data, headers=header, timeout=20)
        try:
            if response.status_code == 200:
                r = response
                return r
            else:
                return None
        except RequestException:
            print("post请求失败")
            return None

    def run_main(self, method, url, data=None, header=None):
        if method == "GET":
            res = self.send_get(url, data, header)
        else:
            res = self.send_post(url, data, header)
        return res

if __name__ == '__main__':
    url = "http://www.httpbin.org/stream/10"
    data = {"user": "dengyi", "password": "111111"}
    t = RunMethod()
    print(t.run_main("GET", url, data))
    print(t.run_main("GET", url, data))

