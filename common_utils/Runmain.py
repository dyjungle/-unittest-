# coding:utf-8
import requests
import json
from requests.exceptions import RequestException
from common_utils.login_web import Login

#使用带session的会话发送请求
class Runmain:
    def __init__(self):
        self.s = Login()

    """定义一个执行接口的请求的类"""
    def send_get(self, url, data=None, header=None):
        response = self.s.cookie_login().get(url=url, params=data, headers=header, timeout=20)
        try:
            if response.status_code == 200:
                r = response
                return r
            else:
                return None
        except RequestException:
            print("get请求失败")
            return None

    def send_post(self, url, data=None, header=None):
        response = self.s.cookie_login().requests.get(url=url, data=data, headers=header, timeout=20)
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
    url = 'https://www.51zxw.net'
    t = Runmain()
    print(t.run_main("GET", url))
    print(t.run_main("GET", url))
    r = t.run_main("GET", url)
    res = r.text
    print(res)

