import unittest
import requests
import hashlib
import urllib3
import json
from w3lib import url
import sys
from configparser import ConfigParser
cp = ConfigParser()
cp.read("D:\\requests_test\\config\\config.ini")
url=cp.get("service","url_test")
uid=cp.get("uk","uid")
key=cp.get("uk","key")


class Gs001(unittest.TestCase):
    def only_entinfo(self,entname,pagenum=1,pagesize=10):

        args = '{"entInfo":"entname"}'
        signstring = "uid=" + uid + "&api=" + "GS001" + "&args=" + args + "&key=" + key
        sign = hashlib.md5(signstring.encode(encoding='UTF-8')).hexdigest()
        param = {"uid": "qqqq",
                 "api": "GS001",
                 "args": '{"entInfo":"%s","pageNum":"%s","pageSize":"%s"}' % (entname,pagenum,pagesize),
                 "sign": sign
                 }
        r = requests.get(url, params=param)
        data1 = r.json()
        #print(r.url)
        #print(r.text)
        #print(data1["code"])
        #print(data1["msg"])
        self.assertEqual(data1["code"], "0000")
        self.assertEqual(data1["msg"], "查询成功")
        return data1

    def test_gs001(self):
        returm_msg=self.only_entinfo("广发证券股份有限公司",2,5)
        first=returm_msg['data']['docs'][1]
        # 判断字段是否存在
        if 'entName' and \
            'regNo' and\
            'isCenter'in first:
            print('y')
        #判断字企业数量是否等于rows的值
        print(returm_msg['data']['docs'][1]['entName'])
        one_page_entnum=len(returm_msg['data']['docs'])
        page_rows=returm_msg['data']['rows']
        print(page_rows)
        self.assertEqual(page_rows,one_page_entnum)#断言搜索到的企业数量等于rows值



if __name__ == "__main__":
    unittest.main()