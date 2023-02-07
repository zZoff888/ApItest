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
    @classmethod
    def getNewsInfo(cls,api,bady):
        url=read_ini(env_Path).data('evn').get('ip')+api
        # print(read_ini(env_Path).data('evn'))
        log = logger()
        # print(bady)
        with requests.get(url=url,json=bady) as response:
            log.info('获取文章内容：%s' % response.json()['msg']+'\n位置为:API.NewApi.getNewsInfo')
            return response.json()['msg']
            # print(response.json()['msg'])

    @classmethod
    def getNewsList(cls,api,bady):
        url=read_ini(env_Path).data('evn').get('ip')+api
        # print(url)
        log = logger()
        # print(bady)
        with requests.get(url=url,json=bady) as response:
            log.info('分页获取所有文章列表：%s' % response.json()['msg']+'\n位置为:API.NewApi.getNewsList')
            # print(response.json())
            return response.json()['msg']

    @classmethod
    def getNewsListLimit(cls,api,bady):
        url=read_ini(env_Path).data('evn').get('ip')+api
        # print(url)
        log = logger()
        # print(bady)
        with requests.get(url=url,json=bady) as response:
            log.info('获取最新创建的四条文章消息：%s' % response.json()['msg']+'\n位置为:API.NewApi.getNewsListLimit')
            # print(response.json())
            return response.json()['msg']

    @classmethod
    def modifyNewsContent(cls,api,bady):
        url=read_ini(env_Path).data('evn').get('ip')+api
        # print(url)
        log = logger()
        # print(bady)
        with requests.get(url=url,json=bady) as response:
            log.info('重新编辑一篇文章内容：%s' % response.json()['msg']+'\n位置为:API.NewApi.modifyNewsContent')
            # print(response.json())
            return response.json()['msg']

    @classmethod
    def createNews(cls,api,bady):
        url=read_ini(env_Path).data('evn').get('ip')+api
        # print(url)
        log = logger()
        # print(bady)
        with requests.post(url=url,json=bady) as response:
            log.info('重新编辑一篇文章内容：%s' % response.json()['msg']+'\n位置为:API.NewApi.createNews')
            # print(response.json())
            return response.json()['msg']

if __name__ == '__main__':
    bady={"id": 1}
    New.getNewsInfo('/news/getNewsInfo',bady)
    #
    # bady={"page": 1,"pagesize": 10}
    # New.getNewsList('/news/getNewsList',bady)
    #
    # bady={}
    # New.getNewsListLimit('/news/getNewsListLimit',bady)
    #
    # bady={"id":1,"newsname":"重新编辑这篇文章的标题","newscontent":"重新编辑这篇文章的内容","Description":""}
    # New.modifyNewsContent('/news/modifyNewsContent',bady)

    # bady={"newsname": "我是市场评论文章标题","newscontent": "我是市场评论文章内容","Perm":1,"class": 2}
    # New.createNews('/news/createNews',bady)


