import unittest
from Untils.public.log import logger
import requests
from ddt import ddt, data, unpack
from Untils.public.read_yaml import read_Yaml
from Config.config import data_Path



test_data = read_Yaml.get_yaml_test_data(data_Path+'new'+'.yaml')
# print(test_data)
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
        log = logger()
        # r = requests.request(http['method'],
        #                      url=http['host'] + http['path'],
        #                      headers=http['headers'],
        #                      params=http['body'])
        print(http['host'] + http['path'])
        resp = 1
        # log.info('__________%s' % resp.json()['msg'] + f'\n位置为:{case}')
        log.info(f'用例名称:{case}'+f',预期结果为：{expected["msg"]}')
        # print(http['headers'])
        # print(case)
        #
        # self.assertEqual(resp['status'], expected['response']['status'])
        # self.assertEqual(resp['message'], expected['response']['message'])
        # self.assertEqual(bool(resp['data']), expected['response']['data'])