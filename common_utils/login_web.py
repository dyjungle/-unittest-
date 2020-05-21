# coding:utf-8
import requests
#通过request模块导入cookiejar 方法,主要功能是对接收下来的cookie进行存储
from requests.cookies import RequestsCookieJar
from base_data import BaseData


class Login():
    @staticmethod
    #输入密码、用户名等信息，通过post请求登录，返回response
    def login_userpsd():
        po = BaseData()
        url = po.get_51url() + '/login'
        data = {
            'loginStr': '15928037997',
            'pwd': 'Dy337371811',
            '__RequestVerificationToken': '',
            'isRememberlogin': 'false'
        }
        header = {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        }
        req = requests.post(url=url, data=data, headers=header, timeout=20)

        return req
    #获取response中的cookies信息，并已字典形式存储，返回字典
    def get_cookies(self):
        response = Login.login_userpsd()
        try:
            if response.cookies:
                labels = []
                for key, value in response.cookies.items():
                    labels.append(
                        {
                            key: value,
                        }
                    )
                # print(labels)
            return labels

        except Exception as e:
            print("为获取到cookies！")
            raise e

    #设置cookies草稿，使用cookies 保持登录，返回session会话
    def cookie_login(self):
        s = requests.session()
        jar = RequestsCookieJar()#实例化对象 创建一个cookis jar对象
        cookies = Login.get_cookies(self)
        #设置cookie
        jar.set('ASP.NET_SessionId', cookies[0]['ASP.NET_SessionId'])
        jar.set('CNZZDATA520717', 'cnzz_eid%3D2133152280-1589332634-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1589332634')
        jar.set('__RequestVerificationToken_L2xvZ2lu0', cookies[1]['__RequestVerificationToken_L2xvZ2lu0'])
        jar.set('newsMember', 'kvox5nmr1rbznhw0akgpbqov')
        jar.set('ASP.NET_SessionId', 'HyT7Ht5fnEyzJu3F4V7q+93HItU3QxDSPDJtnC4ukMGJyMf6TaDFeTu4baEpr11FK7qRmLi2MzqHpSTaSGNfNK/KQkl2lqZVrx+f8+FajSI=')
        jar.set('__cfduid', 'd7eb9236d43fc8a872d2c01f586d5078e1589337010')
        s.cookies.update(jar) #把cookies追加到Session中

        return s
        #返回携带cookies 的session

if __name__ == '__main__':
    t = Login.login_userpsd()
    # print(type(t.cookies))
    # print(t.cookies)
    # for key, value in t.cookies.items():
    #     print(key + ':' + value)

    r = Login.get_cookies(t)
    print(r)
