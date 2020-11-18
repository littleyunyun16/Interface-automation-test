# 这个文件主要来通过get、post、put、delete等方法来进行http请求，并拿到请求响应
import requests
import json
from common.get_sign import get_sign


class RunMain():

    def send_post(self,url,data):
        result=requests.post(url,json=data).json()
        res=json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)
        return res

    def send_get(self,url,data):
        result=requests.get(url,params=data).json()
        res=json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    def run_main(self,method,url=None,data=None):
        result =None
        sign=get_sign(data)
        data["sign"]=sign
        if method=='post':
            result=self.send_post(url,data)
        elif method=='get':
            result=self.send_get(url,data)
        else:
            print("method值错误！！！")
        return result


if __name__ == '__main__':
    para= {"method": "gy.erp.trade.return.status.update","sessionkey": "94ee1ca3c41d44989290d02985105865", "appkey": "116761","code":"RGO12504806369","audit_status": "2",}

    result = RunMain().run_main('post', 'http://api.demo.guanyierp.com/rest/erp_open',para)
    print(result)


