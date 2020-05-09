# coding:utf-8
from common_utils.read_config import ReadConfig
import os

class BaseData:
    #初始化参数
    def __init__(self):
        self.data = ReadConfig()

    def get_ip(self):
        """从配置文件中获取固定IP"""
        ip = self.data.get_host("url")
        return ip


if __name__ == '__main__':
    #实例化对象，检查是否获取到配置文件的数据
    base_data = BaseData()
    print(base_data.get_ip())