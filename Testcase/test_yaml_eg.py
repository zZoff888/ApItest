import unittest
from ddt import ddt, data, unpack
from Untils.public.read_yaml import read_Yaml
from Config.config import data_Path



test_data = read_Yaml.get_yaml_test_data(data_Path+'test'+'.yaml')
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
    def test_proxy(self, case, http, expected):
        # r = requests.request(http['method'],
        #                      url=http['host'] + http['path'],
        #                      headers=http['headers'],
        #                      params=http['params'])
        # resp = r.json()
        print(http['headers'])
        print(case)
        #
        # self.assertEqual(resp['status'], expected['response']['status'])
        # self.assertEqual(resp['message'], expected['response']['message'])
        # self.assertEqual(bool(resp['data']), expected['response']['data'])