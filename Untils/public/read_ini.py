import sys
sys.path.append(r"D:")
'''
本模块提供读取ini文件的数据
configparser:他提供读取ini文件数据的能力
'''

import configparser


class read_ini():
    def __init__(self,filename):
        self.config = configparser.ConfigParser()
        self.config.read(filename, encoding="utf-8")

    def data(self,name):
        data=dict(self.config.items(name))
        return data

if __name__ == '__main__':
    readini=read_ini(r"/Users/mac/Desktop/web/web/Data/config.ini")
    print(readini.data("log"))
    # import os
    # str0=r"/Users/mac/Desktop/web/web/Data/config.ini"
    # print(os.path.split(str0)[1])

# class read_ini():
#     #进行初始化configparser
#     def __init__(self,path):
#         #实例化configparser
#         self.config=configparser.ConfigParser()
#         #设置读取的配置文件
#         self.config.read(path,encoding="utf-8")
#
#     #读取某个类型的配置
#     def read(self,section_name):
#         value=self.config.items(section_name) #获取到的数据格式：[(),(),()]
#         data=dict(value) #进行josn格式转换
#         return data #返回josn格式
