# coding:utf-8
from common_utils.read_config import ReadConfig
import os

class BaseData:
    #初始化参数
    def __init__(self):
        self.data = ReadConfig()

    def get_51url(self):
        """从配置文件中获取url"""
        url = self.data.get_51url("51_URL")
        return url

    def get_httpbinurl(self):
        """从配置文件中获取url"""
        url = self.data.get_httpbinurl("HTTPBIN_URL")
        return url

    def get_ip(self):
        """从配置文件中获取url"""
        ip = self.data.get_ip("IP")
        return ip

    def get_port(self):
        """从配置文件中获取url"""
        port = self.data.get_port("PORT")
        return port


if __name__ == '__main__':
    #实例化对象，检查是否获取到配置文件的数据
    base_data = BaseData()
    print(base_data.get_httpbinurl())