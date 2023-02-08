import xlrd
from Config.config import bady_Path

class read_xlrd(object):
    #定义类属性nrows
    nrows=None
    #定义类属性nclos
    ncols=None
    def __init__(self,filename):
        self.workbook = xlrd.open_workbook(filename)
    def Sheet(self,name):
        Sheet = self.workbook.sheet_by_name(name)
        #设置类属性nrows=Sheet.nrows
        read_xlrd.nrows=Sheet.nrows
        # 设置类属性ncols=Sheet.ncols
        read_xlrd.ncols=Sheet.ncols
        return Sheet



    '''
    不传开始行和结束行时，默认取莫一列的所有有行的数据
    '''
    def all_cols(self,Sheet,clo,start_row=0,end_row=nrows):
        if end_row !=None:
            if start_row<=end_row:
                data=Sheet.col_values(clo, start_row, end_row)
                return data
            else:
                raise Exception("start_row的值大于end_row的值") #设置报错信息
        else:
            data = Sheet.col_values(clo, start_row, end_row)
            return data

    '''
    不传开始列和结束列时，默认取莫一行中的所有列数数据
    '''
    def all_rows(self,Sheet,row,start_clo=0,end_clo=ncols):
        if end_clo!=None:
            if start_clo<=end_clo:
                data=Sheet.row_values(row, start_clo, end_clo)
                return data
            else:
                raise Exception("start_clo的值大于end_clo的值")
        else:
            data = Sheet.row_values(row, start_clo, end_clo)
            return data
read = read_xlrd(filename=r"{}".format(bady_Path))
sheet = read.Sheet("qq")
infor_dict = dict(list(zip(read.all_cols(sheet, 1)[0:], read.all_cols(sheet, 2)[1:])))
print(infor_dict)