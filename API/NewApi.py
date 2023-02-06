import requests

from Untils.public.read_ini import read_ini
from Config.config import env_Path
from web3 import Web3, EthereumTesterProvider
from eth_account.messages import encode_defunct
from Untils.public.log import logger
from Config.config import bady_Path
from Untils.public.ReadExcel import ReadExcel
import json

class New():
    s=None
    ip=None
    interexcle = None
    loginMessage = None
    token=None
    signature=None
    @classmethod
    def getNewsInfo(cls,api,bady):
        url=read_ini(env_Path).data('evn').get('ip')+api
        # print(url)
        log = logger()
        # print(bady)
        with requests.get(url=url,json=bady) as response:
            log.info('获取文章内容：%s' % response.json()['msg'])
            return response.json()['msg']
            # print(response.json()['msg'])
    @classmethod
    def getNewsList(cls,api,bady):
        url=read_ini(env_Path).data('evn').get('ip')+api
        # print(url)
        log = logger()
        # print(bady)
        with requests.get(url=url,json=bady) as response:
            log.info('获取文章内容：%s' % response.json()['msg'])
            print(response.json())
            return response.json()['msg']

if __name__ == '__main__':
    # bady={"id": 1}
    # New.getNewsInfo('/news/getNewsInfo',bady)

    # bady={"page": 1,"pagesize": 10}
    # New.getNewsList('/news/getNewsList',bady)