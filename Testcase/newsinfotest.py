import unittest
from ddt import ddt, data, unpack
from Untils.public.read_yaml import read_Yaml
from Config.config import data_Path
from API.NewApi import New



test_data = read_Yaml.get_yaml_test_data(data_Path+'NewApiTestcase/getNewsInfo'+'.yaml')
# print(test_data)
test_data1= read_Yaml.get_yaml_test_data(data_Path+'NewApiTestcase/getNewsList'+'.yaml')
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
    def test01(self, case, http, expected):
        a=New.getNewsInfo(http['path'],http['params'])
        # r = requests.request(http['method'],
        #                      url=http['host'] + http['path'],
        #                      headers=http['headers'],
        #                      params=http['params'])
        # print(http['params'])
        # resp = r.json()
        # print(http['headers'])
        # print(case)
        #
        # self.assertEqual(resp['status'], expected['response']['status'])
        # self.assertEqual(resp['message'], expected['response']['message'])
        # self.assertEqual(bool(resp['data']), expected['response']['data'])

    @unpack
    @data(*test_data1)
    def test02(self, case, http, expected):
        a=New.getNewsList(http['path'],http['params'])