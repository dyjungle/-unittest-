import os
from selenium import webdriver
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def insert_img(driver,filename):
    func_path = os.path.dirname(__file__)
    # print(func_path)
    base_dir = os.path.dirname(func_path)
    # print(base_dir)

    # 将路径转化为字符串
    base_dir = str(base_dir)

    # 对路径的字符串进行替换
    base_dir = base_dir.replace('\\', '/')
    #print(base_dir)

    base=base_dir.split('/Website')[0]

    # print(base)
    filepath=base+'/Website/test_report/screenshot/'+filename
    # print(filepath)
    driver.get_screenshot_as_file(filepath)

def send_mail(latest_report):
    f = open(latest_report, 'rb')
    mail_content = f.read()
    f.close()

    smtpserver = 'smtp.163.com'

    user = 'dengyi_cuit@163.com'
    # 根据自己邮箱密码来设置
    password = 'OAJXBBUIYOXRDABN'

    sender = 'dengyi_cuit@163.com'
    receives = ['337371811@qq.com']

    subject = 'Web Selenium 自动化测试报告'


    msg = MIMEText(mail_content, 'html', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = ','.join(receives)

    smtp = smtplib.SMTP_SSL(smtpserver, 465)
    smtp.helo(smtpserver)
    smtp.ehlo(smtpserver)
    smtp.login(user, password)

    print("Start send email...")
    smtp.sendmail(sender, receives, msg.as_string())
    smtp.quit()
    print("Send email end!")

def latest_report(report_dir):
    #获取report文件夹中所有的文件列表 report_dir：文件夹路径
    lists = os.listdir(report_dir)
    print(lists)
    #按时间顺序对该目录文件夹下面的文件进行排序
    lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))

    print("the latest report is " + lists[-1])
    #返回测试报告文件名
    file = os.path.join(report_dir, lists[-1])
    # print(file)
    return file


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("http://www.sogou.com")
    insert_img(driver, 'sougou.png')
