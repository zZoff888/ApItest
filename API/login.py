import time

import requests
from Untils.public.read_ini import read_ini
from Config.config import env_Path
from Untils.public.log import logger
from Untils.public.CodeDemo_ddddocr import codedemo
from Untils.public.bese64 import bese
class Login():
    picPath=None
    captchaId=None
    token=None
    @classmethod
    def getcode(cls,api):
        url=read_ini(env_Path).data('evn').get('ip')+api
        # print(read_ini(env_Path).data('evn'))
        log = logger()
        # print(bady)
        with requests.get(url=url) as response:
            log.info(f'{response.json()["msg"]}')
            # print(response.json())
            cls.captchaId=response.json()['data']['captchaId']
            picPath=response.json()['data']['picPath']+','
            # print(response.json())
            # picPath=response.json()['data']['picPath']+','

            # print(picPath)
            # bese64
            cls.picPath=list(picPath.split(",")[1].split())[-1]
            bese.bese_shift(f'{cls.picPath}')
        # print(cls.picPath)
    @classmethod
    def login(cls,api):
        while True:
            url = read_ini(env_Path).data('evn').get('ip') + api
            log = logger()
            # print(bady)
            cls.picPath = codedemo.ddddddor(r'1.jpg')
            # print(a)

            body = {"username": "admin1", "password": "123456", "captcha": f'{cls.picPath}',
                    "CaptchaId": f"{cls.captchaId}"}


            with requests.post(url=url,json=body) as response:
                msg=response.json()['msg']
                if msg == '登录成功':
                    cls.token = response.json()['data']['token']
                    print(cls.token)
                    break
            Login.getcode('/user/captcha')

if __name__ == '__main__':
    #
    Login.getcode('/user/captcha')
    Login.login('/user/login')

