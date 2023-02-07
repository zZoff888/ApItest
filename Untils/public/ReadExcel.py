import xlrd
from Config.config import bady_Path
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
     def read1(self,fileaddress=None,raw=None):
         s = ReadExcel.readExcel(fileaddress,raw)
         return s


# if __name__ == '__main__':
    # s = ReadExcel.readExcel(bady_Path,"需求")
    # inter=s[0]["url"]
    #
    # bady=s[1]["请求参数"]
    # print(inter,bady)