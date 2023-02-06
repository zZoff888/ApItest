import unittest
from ddt import *
from Config.config import bady_Path
from Untils.public.ReadExcel import ReadExcel
from pages.test import Login

@ddt()
class TestDemo(unittest.TestCase):
    interexcle = None
    url=None
    bady=None
    interexcle = ReadExcel.readExcel(bady_Path, "签名true")
    getLoginMessagedata=[]
    for i in interexcle:
        # print(i,type(i))
        url = i["url"]
        a = '/sign/getLoginMessage'
        if url == a:
            bady = i["请求参数"]
            getLoginMessagedata.append(bady)
    # print(getLoginMessagedata,type(getLoginMessagedata))
    authLoginSign=[]
    for i in interexcle:
        # print(i,type(i))
        url = i["url"]
        a = '/sign/authLoginSign'
        if url == a:
            bady = i["请求参数"]
            authLoginSign.append(bady)
    # print(authLoginSign)
    @data(*getLoginMessagedata)
    # @unpack
    def test_05_list(self, bady1):
        a=json.loads(bady1)
        Login.set()
        value=Login.getLoginMessage(a)
        self.assertIn("成功", value)
    @data(*authLoginSign)
    def test_07_list(self, bady1):
        b={"address":"0x089c71Ee576b4F2F4D1DaD99d8901CaAa32eF6cb"}
        a = json.loads(bady1)
        Login.set()
        Login.getLoginMessage(b)
        Login.authLoginSign(a)
        # print(bady1)



if __name__ == '__main__':
    unittest.main(verbosity=2)
