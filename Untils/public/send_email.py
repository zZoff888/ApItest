'''
本模块实现发送邮件的功能
'''
import os
import smtplib
from email.mime.text import MIMEText
from Untils.public.read_ini import read_ini
from email.mime.multipart import MIMEMultipart
from Config.config import email_Path,report_Path

class send_email():
    def __init__(self):
        readini = read_ini(r"{}".format(email_Path))
        self.respone=readini.data("QQ")
        self.smtpobj = smtplib.SMTP_SSL(self.respone["ip"], port=int(self.respone["prot"]))  # 连接qq的邮箱服务器
        self.smtpobj.login(self.respone["loginer"], self.respone["code"])  # 登录人家服务器的认证
        self.msgRoot = MIMEMultipart() #生成对象


    def send(self,type,value):


        if type.lower()=="text":
            data = MIMEText(str(value))
        elif type.lower()=="file":
            with open(file=r"{}".format(value), mode="rb") as f:  # rb读成字节
                mail_msg = f.read()
            data = MIMEText(mail_msg, "base64", "utf-8")  # _subtype 默认不支持文件流，需要改成base64
            # 设置成文件流
            data["Content-Type"] = "application/octer-stream"
            # 设置附件的名字
            data["Content-Disposition"] = "attachment;filename='{}'".format(os.path.split(value)[1])

        self.msgRoot.attach(data)



    def run(self):
        # 设置发送者
        self.msgRoot["from"] = self.respone["sendner"]
        # 接收者
        self.msgRoot["To"] = self.respone["recvner"]
        self.msgRoot["Subject"] = "自动化测试结果"
        self.smtpobj.sendmail(self.respone["sendner"], self.respone["recvner"], self.msgRoot.as_string())

# if __name__ == '__main__':
#     se = send_email()
#     # se.send("text","111")
#     se.send("file", r"{}text01.html".format(report_Path))
#     se.send("file", r"{}test01.html".format(report_Path))
#     se.run()