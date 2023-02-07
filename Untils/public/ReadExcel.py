import os

import pandas as pd
import xlrd
from Config.config import bady_Path, data_Path
from Untils.public.read_yaml import read_Yaml


#读取Excel的方法
class ReadExcel():
     def readExcel(fileName,SheetName=None):
         data = xlrd.open_workbook(fileName)
         table = data.sheet_by_name(SheetName)

         #获取总行数、总列数
         nrows = table.nrows
         ncols = table.ncols
         if nrows > 1:
             #获取第一行的内容，列表格式
             keys = table.row_values(0)
             #print(keys)

             listApiData = []
             #获取每一行的内容，列表格式
             for col in range(1,nrows):
                 values = table.row_values(col)
                 # keys，values这两个列表一一对应来组合转换为字典
                 api_dict = dict(zip(keys, values))
                 #print(api_dict)
                 listApiData.append(api_dict)
             return listApiData
         else:
             return None

     def get_excel_test_data(filename, sheet_name=0):
         """
         读取Excel表格
         :param filename: 文件名
         :param sheet_name: 工作表名
         :return: 包含所有行的列表
         """
         filepath = data_Path + filename

         # if not os.path.exists(filepath):
         #     raise ValueError(f'({filepath}) - 文件不存在，请检查！')
         # print(filepath)
         # print(sheet_name)
         data = pd.read_excel(filepath, sheet_name=sheet_name)  # 读取表格
         # print(data)
         data.fillna('', inplace=True)  # 替换所有的缺失值为空字符""
         new_list = data.values.tolist()
         # print(new_list)
         return new_list

     def read1(self,fileaddress=None,raw=None):
         s = ReadExcel.readExcel(fileaddress,raw)
         return s


# if __name__ == '__main__':
    # s = ReadExcel.readExcel(bady_Path,"需求")
    # inter=s[0]["url"]
    #
    # ReadExcel.get_excel_test_data('bady.xlsx','qq')
    # bady=s[1]["请求参数"]
    # print(inter,bady)