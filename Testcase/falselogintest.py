import unittest
from ddt import *
from Config.config import bady_Path
from Untils.public.ReadExcel import ReadExcel
from API.NewApi import New
from Untils.public.read_yaml import read_Yaml

a = read_Yaml.readYaml('test')
# print(a)
# @ddt()
class TestDemo(unittest.TestCase):

    def test01(self):
        # interexcle = None
        # url = None
        # #     bady=None
        # interexcle = read_Yaml.readYaml('test')
        # print(interexcle)
        # # getLoginMessagedata=[]
        # # print(interexcle)
        # a = read_Yaml.readYaml('test')['getNewsInfo'][1]['bady']
        bady = {"id": 1}
        New.getNewsInfo('/news/getNewsInfo', bady)


if __name__ == '__main__':
    unittest.main(verbosity=2)
