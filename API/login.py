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
            # print(picPath)
            # bese64
            cls.picPath=list(picPath.split(",")[1].split())[0]
    @classmethod
    def login(cls,api):
        url = read_ini(env_Path).data('evn').get('ip') + api
        log = logger()
        # print(bady)
        bese.bese_shift(f'{cls.picPath}')
        cls.picPath=codedemo.ddddddor(r'1.jpg')
        # print(a)

        body = {"username": "admin1", "password": "123456", "captcha": f'{cls.picPath}',
                "CaptchaId": f"{cls.captchaId}"}
        msg=None
        while msg != '登录成功':
            with requests.post(url=url,json=body) as response:
                msg=response.json()['msg']
            # print(response.json()['msg'])
            time.sleep(1)
        else:
            cls.token=response.json()['data']['token']
            # print(token)
        log.info(f'{response.json()["msg"]}')

if __name__ == '__main__':
    #
    Login.getcode('/user/captcha')
    Login.login('/user/login')

