# 读取usercase.xlsx中的用例，用unittest来进行断言校验


import testfile.readExcel as readexcel
import paramunittest
import unittest
import json
import urllib.parse
from common.configHttp import RunMain

url = 'http://api.demo.guanyierp.com/rest/erp_open'
return_xls = readexcel.readExcel().get_xls('ReturnOrder.xlsx', 'Sheet1')  # 由文件readExcel来获取用例


@paramunittest.parametrized(*return_xls)
class testUserLogin(unittest.TestCase):
    def setParameters(self, module, ID, UserCase, method, params):

        self.module = module
        self.ID = ID
        self.UserCase = UserCase
        self.method = method
        self.params = params

    def description(self):
        """
        test report description
        :return:
        """
        self.module
        self.UserCase

    def setUp(self):
        print(self.UserCase+ "测试开始前准备")

    def tearDown(self):
        print("测试结束，输出log完结\n\n")

    def test01case(self):
        self.checkResult()

    def checkResult(self):
        params=eval(self.params)
        info = RunMain().run_main(self.method, url, params)
        ss = json.loads(info)
        if self.UserCase == '审核':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertTrue('success')
            print(ss['code'])

        if self.UserCase == '已审核':  # 同上
            self.assertFalse('success')
        if self.UserCase == 'null':  # 同上
            self.assertFalse('success')


if __name__ == '__main__':
    unittest.main()
