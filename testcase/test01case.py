# 读取usercase.xlsx中的用例，用unittest来进行断言校验




import unittest
import json
import ddt
import urllib.parse
from common.configHttp import RunMain
from testfile.readExcel import ReadExcel

return_xls = ReadExcel('ReturnOrder.xlsx', 'Sheet1').read_data() # 由文件readExcel来获取用例


@ddt.ddt
class testReturnOrder(unittest.TestCase):

    def setUp(self):
        print("测试开始前准备")

    def tearDown(self):
        print("测试结束，输出log完结\n\n")

    @ddt.data(*return_xls)
    def test01case(self,data):
        params = eval(data['params'])
        info = RunMain().run_main(data['method'], data['url'], params)
        ss = json.loads(info)
        self.assertTrue(ss['success'])




if __name__ == '__main__':
    unittest.main()
