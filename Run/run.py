import time
import unittest

from Config.config import testcase_Path,report_Path,contrl_Path
from Untils.public.HTMLTestRunnerCN import HTMLTestRunner
from Untils.public.read_ini import read_ini
from Untils.public.send_email import send_email

#发邮件，跟着时间生成的测试报告

#ini
def run():

    s = time.strftime("%Y%m%d%H%M%S", time.localtime()) #生成当前时间
    readini = read_ini(r"{}".format(contrl_Path)) #读取控制用例跑的contrl.ini配置
    infor_dict = readini.data("case") #读取配置数据
    # print(infor_dict)
    if "True" in infor_dict.values(): #判断有用例需要执行
        fp = open(file=report_Path + str(s) + "text.html", mode="wb")  # s+"".html 生成报告
        # print(fp)
        for i in infor_dict:
            # print(i)
            if infor_dict[i] == "True":
                # 执行脚本
                suit = unittest.defaultTestLoader.discover(fr"{testcase_Path}", pattern=str(i))  # 匹配脚本的路径，匹配规则
                # print(testcase_Path)
                # print(suit)
                runner = HTMLTestRunner(fp, title="自动化测试结果", description="执行情况", tester="qw")
                runner.run(suit)
            else:
                print("{}脚本不执行！".format(i))
        fp.close() #关闭文件
        se = send_email() #生成发送邮件的对象
        se.send("file", report_Path + str(s) + "text.html") #配置邮件
        se.run() #进行发送
    else:
        print("没有需要执行的脚本用例！")

if __name__ == '__main__':
    run()

