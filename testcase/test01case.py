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

    # def checkResult(self):  # 断言
    #     """
    #     check test result
    #     :return:
    #     """
    # data1 = eval(self.params)
    # info = RunMain().run_main(self.method, self.url, data1)  # 根据Excel中的method调用run_main来进行requests请求，并拿到响应
    # ss = json.loads(info)  # 将响应转换为字典格式
    # self.assertTrue(ss['success'])
    # if self.case_name == 'login':  # 如果case_name是login，说明合法，返回的code应该为200
    #     self.assertEqual(ss['code'], 200)
    # if self.case_name == 'login_error':  # 同上
    #     self.assertEqual(ss['code'], -1)
    # if self.case_name == 'login_null':  # 同上
    #     self.assertEqual(ss['code'], 10001)


if __name__ == '__main__':
    unittest.main()
