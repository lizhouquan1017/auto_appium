# coding=utf-8

import smtplib
import os
import mimetypes
import time
import sys
import logging

sys.path.append('./..')
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from base.BaseReadIni import ReadIni
from util import operationFile


cfg = ReadIni(isconfig=True, file_name="email_conf.ini")
email_host = cfg.read_config('email_config', 'email_host')
send_user = cfg.read_config('email_config', 'send_user')
password = cfg.read_config('email_config', 'password')


def pre_send_mail(report_name):
    """发送邮件预处理"""
    logging.info('测试任务完成，编写邮件中...')
    message = MIMEMultipart("related")
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    to_addr = cfg.read_config("email", "To_addr")
    cc_addr = cfg.read_config("email", "Cc_addr")
    user_list = to_addr.split(',') + cc_addr.split(',')
    sub = "【自动发送】移动端APP自动化测试报告" + current_time
    user = send_user
    message['Subject'] = sub
    message['From'] = user
    message['To'] = to_addr
    message['Cc'] = cc_addr
    # 添加内容(或图片)到邮件正文中
    mail_content = """
            <p>您好，附件为移动端APP自动化测试报告，详情请下载查看，推荐使用Chrome浏览器查看!</p>
            """
    # 添加邮件正文信息
    mail_body = MIMEText(mail_content, _subtype='html', _charset='utf-8')
    message.attach(mail_body)
    # 添加附件1
    ctype, encoding = mimetypes.guess_type(report_name)
    if ctype is None or encoding is not None:
        ctype = "application/octet-stream"
    maintype, subtype = ctype.split("/", 1)
    att1 = MIMEImage((lambda f: (f.read(), f.close()))(open(report_name, 'rb'))[0], _subtype=subtype)
    att1.add_header("Content-Disposition", "attachment", filename=os.path.basename(report_name))
    message.attach(att1)
    # 发送邮件
    server = smtplib.SMTP()
    server.connect(email_host)
    server.login(send_user, password)
    server.sendmail(user, user_list, message.as_string())
    server.close()


def new_report(test_report):
    """找出最新的测试报告"""
    # 列出目录下的所有文件和文件夹保存到lists
    lists = os.listdir(test_report)
    lists.sort(key=lambda fn: os.path.getmtime(test_report + "/" + fn))
    # 获取最新的文件保存到file_new
    file_new = os.path.join(test_report, lists[-1])
    return file_new


def send_email():
    """执行发送邮件"""
    report_path = os.path.dirname(os.path.dirname(__file__)) + '/report_his/'
    operationFile.zipping_file("../reports", "../report_his/report.zip")
    report_name = new_report(report_path)
    try:
        pre_send_mail(report_name)
        logging.info("编写完成，邮件发送成功")
    except Exception as e:
        logging.info("邮件发送失败！" + str(e))


