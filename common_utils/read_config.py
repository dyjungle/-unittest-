# coding:utf-8

import configparser
import os


class ReadConfig:
    def __init__(self, filepath=None):
        if filepath:
            configpath1 = filepath
        else:
            root_dir1 = os.path.dirname(__file__)  # 获取当前脚本的目录
            configpath1 = os.path.join(root_dir1, "config.ini")  # 拼接路径，得到配置文件路径
            # print(root_dir1)

        self.cf = configparser.ConfigParser()#实例化对象
        self.cf.read(configpath1)#读取配置文件

    def get_ip(self, param):
        ip = self.cf.get("IP", param)#获取配置文件中URL中的值，赋值给value
        return ip

    def get_51url(self, param):
        url = self.cf.get("51_URL", param)#获取配置文件中URL中的值，赋值给value
        return url

    def get_httpbinurl(self, param):
        url = self.cf.get("HTTPBIN_URL", param)#获取配置文件中URL中的值，赋值给value
        return url

    def get_port(self, param):
        port = self.cf.get("PORT", param)#获取配置文件中URL中的值，赋值给value
        return port

base_url = ReadConfig()

# if __name__ == '__main__':
#     test = ReadConfig()#实例化对象
#     t = test.get_host("url")#获取URL中 url 的值
#     print(t)
#     print(base_url.get_host("URL"))