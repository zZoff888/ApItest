import unittest
from ddt import ddt, data, unpack
from Untils.public.read_yaml import read_Yaml
from Config.config import data_Path
from Untils.public.ReadExcel import ReadExcel

test_data=ReadExcel.get_excel_test_data('bady.xlsx','qq')
print(test_data)
@ddt
class TestAPI(unittest.TestCase):

    def setUp(self):
        """在每个测试方法之前执行"""
        pass

    def tearDown(self):
        """在每个测试方法之后执行"""
        pass

    @unpack
    @data(*test_data)
    def test_proxy(self):
        # r = requests.request(http['method'],
        #                      url=http['host'] + http['path'],
        #                      headers=http['headers'],
        #                      params=http['params'])
        # resp = r.json()
        print(data)