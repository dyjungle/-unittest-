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

            # root_dir = os.path.dirname(os.path.abspath('.')) # 获取当前脚本所在目录的上一级目录
            # configpath = os.path.join(root_dir, "common_utils/config.ini") # 拼接路径
            # print(root_dir)

        self.cf = configparser.ConfigParser()#实例化对象
        self.cf.read(configpath1)#读取配置文件

    def get_host(self, param):
        value = self.cf.get("URL", param)#获取配置文件中URL中的值，赋值给value
        return value


base_url = ReadConfig()

# if __name__ == '__main__':
#     test = ReadConfig()#实例化对象
#     t = test.get_host("url")#获取URL中 url 的值
#     print(t)
#     print(base_url.get_host("URL"))