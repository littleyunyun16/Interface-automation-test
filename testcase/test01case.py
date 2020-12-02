# 读取usercase.xlsx中的用例，用unittest来进行断言校验


import testfile.readExcel as readexcel
# import paramunittest
import unittest
import json
import urllib.parse
from common.configHttp import RunMain
import ddt

return_xls = readexcel.readExcel().get_xls('ReturnOrder.xlsx', 'Sheet1')  # 由文件readExcel来获取用例
print(return_xls)


@ddt.ddt
class testUserLogin(unittest.TestCase):
    @ddt.data(*return_xls)
    def setParameters(self,data):

        self.id = data['id']
        self.case_name = data['case_name']
        self.url = data['url']
        self.method = data['method']
        self.params = data['params']
        self.expect=data['expect']
        self.response=data['response']
        self.result=data['result']
        self.passed=data['passed']

    def setUp(self):
        print(self.id+ "测试开始前准备")

    def tearDown(self):
        print("测试结束，输出log完结\n\n")
    def test01case(self):
        params = eval(self.params)
        info = RunMain().run_main(self.method, self.url, params)
        ss = json.loads(info)



if __name__ == '__main__':
    unittest.main()
