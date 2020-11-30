# 读取usercase.xlsx中的用例，用unittest来进行断言校验


import testfile.readExcel as readexcel
# import paramunittest
import unittest
import json
import urllib.parse
from common.configHttp import RunMain
from ddt import  ddt,data,unpack,file_data

return_xls = readexcel.readExcel().get_xls('ReturnOrder.xlsx', 'Sheet1')  # 由文件readExcel来获取用例


@ddt
class testUserLogin(unittest.TestCase):
    def setParameters(self, module, ID, UserCase, method, params):

        self.module = module
        self.ID = ID
        self.UserCase = UserCase
        self.method = method
        self.params = params

    def setUp(self):
        print(self.UserCase+ "测试开始前准备")

    def tearDown(self):
        print("测试结束，输出log完结\n\n")
    @data(*return_xls)
    def test01case(self):
        params = eval(self.params)
        info = RunMain().run_main(self.method, url, params)
        ss = json.loads(info)



if __name__ == '__main__':
    unittest.main()
