# 读取usercase.xlsx中的用例，用unittest来进行断言校验


import testfile.readExcel as readexcel
import paramunittest
import unittest
import json
import urllib.parse
from common.configHttp import RunMain

return_xls = readexcel.readExcel().get_xls('ReturnOrder.xlsx', 'Sheet1')  # 由文件readExcel来获取用例


@paramunittest.parametrized(*return_xls)
class testReturnOrder(unittest.TestCase):
    def setParameters(self, id, case_name, url, method, params, expect, response, result, passed):
        self.id = id
        self.case_name = case_name
        self.url = url
        self.method = method
        self.params = params
        self.expect = expect
        self.response = response
        self.result = result
        self.passed = passed

    def setUp(self):
        print(self.id + "测试开始前准备")

    def tearDown(self):
        print("测试结束，输出log完结\n\n")

    def test01case(self):
        params = eval(self.params)
        info = RunMain().run_main(self.method, self.url, params)
        ss = json.loads(info)
        self.assertTrue(ss['success'])




if __name__ == '__main__':
    unittest.main()
