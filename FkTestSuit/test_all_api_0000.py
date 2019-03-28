import unittest
import requests
import hashlib
from w3lib import url
import datetime
from configparser import ConfigParser

cp = ConfigParser()#public
cp.read("D:\\requests_test\\config\\config.ini")
url = cp.get("service", "url_test")
uid = cp.get("uk", "uid")
key = cp.get("uk", "key")


class All_api_0000(unittest.TestCase):
    def only_entinfo(self, entname, api):
        args = '{"entInfo":"entname"}'
        signstring = "uid=" + uid + "&api=" + api + "&args=" + args + "&key=" + key
        sign = hashlib.md5(signstring.encode(encoding='UTF-8')).hexdigest()
        param = {"uid": "qqqq",
                 "api": api,
                 "args": '{"entInfo":"%s"}' % entname,
                 "sign": sign
                 }
        r = requests.get(url, params=param)
        data1 = r.json()
        print(r.url)
        # print(r.text)
        print(data1["code"])
        print(data1["msg"])
        self.assertEqual(data1["code"], "0000")
        code = data1["code"]
        return data1

    def entname_and_type(self, entname, type,api):
        args = '{"entInfo":"entname"}'
        signstring = "uid=" + uid + "&api=" + "DI005" + "&args=" + args + "&key=" + key
        sign = hashlib.md5(signstring.encode(encoding='UTF-8')).hexdigest()
        param = {"uid": "qqqq",
                 "api": api,
                 "args": '{"entInfo":"%s","type":"%s"}' % (entname, type),
                 "sign": sign
                 }
        r = requests.get(url, params=param)
        data1 = r.json()
        print(r.url)
        # print(r.text)
        print(data1["code"])
        print(data1["msg"])
        self.assertEqual(data1["code"], "0000")
        code = data1["code"]
        return code

    def only_id(self, id, api):
        args = '{"entInfo":"entname"}'
        signstring = "uid=" + uid + "&api=" + api + "&args=" + args + "&key=" + key
        sign = hashlib.md5(signstring.encode(encoding='UTF-8')).hexdigest()
        param = {"uid": "qqqq",
                 "api": api,
                 "args": '{"id":"%s"}' % id,
                 "sign": sign
                 }
        r = requests.get(url, params=param)
        data1 = r.json()
        print(r.url)
        # print(r.text)
        print(data1["code"])
        print(data1["msg"])
        self.assertEqual(data1["code"], "0000")
        self.assertEqual(data1["msg"], "查询成功")
        code = data1["code"]
        return code

    def only_entname(self, entname, api):
        args = '{"entName":"entname"}'
        signstring = "uid=" + uid + "&api=" + api + "&args=" + args + "&key=" + key
        sign = hashlib.md5(signstring.encode(encoding='UTF-8')).hexdigest()
        param = {"uid": "qqqq",
                 "api": api,
                 "args": '{"entName":"%s"}' % entname,
                 "sign": sign
                 }
        r = requests.get(url, params=param)
        data1 = r.json()
        print(r.url)
        # print(r.text)
        print(data1["code"])
        print(data1["msg"])
        self.assertEqual(data1["code"], "0000")
        self.assertEqual(data1["msg"], "查询成功")
        code = data1["code"]
        return data1

    def entname_and_page(self, api, entname, pagesize=10, pagenum=1):
        args = '{"entname":"entname","pagesize":"pagesize","pagenum":"pagenum"}'
        signstring = "uid=" + uid + "&api=" + api + "&args=" + args + "&key=" + key
        sign = hashlib.md5(signstring.encode(encoding='UTF-8')).hexdigest()
        param = {"uid": "qqqq",
                 "api": api,
                 "args": '{"entInfo":"%s","pageSize":"%s","pageNum":"%s"}' % (entname, pagesize, pagenum),
                 "sign": sign
                 }
        r = requests.get(url, params=param)
        data1 = r.json()
        print(r.url)
        # print(r.text)
        print(data1["code"])
        print(data1["msg"])
        self.assertEqual(data1["code"], "0000")
        self.assertEqual(data1["msg"], "查询成功")
        code = data1["code"]
        return code

    def gs011(self, entname, year):
        args = '{"entInfo":"entname"}'
        signstring = "uid=" + uid + "&api=" + "GS011" + "&args=" + args + "&key=" + key
        sign = hashlib.md5(signstring.encode(encoding='UTF-8')).hexdigest()
        param = {"uid": "qqqq",
                 "api": "GS011",
                 "args": '{"entInfo":"%s","year":"%s"}' % (entname, year),
                 "sign": sign
                 }
        r = requests.get(url, params=param)
        data1 = r.json()
        print(r.url)
        # print(r.text)
        print(data1["code"])
        print(data1["msg"])
        self.assertEqual(data1["code"], "0000")
        self.assertEqual(data1["msg"], "查询成功")
        code = data1["code"]
        return code

    def yq001(self, entname, eventlist):
        nowdate1 = datetime.datetime.now()
        befor_30_dayes = (nowdate1 + datetime.timedelta(days=-30)).strftime('%Y-%m-%d')
        nowdate = nowdate1.strftime('%Y-%m-%d')
        args = '{"entname":"entname","pagesize":"pagesize","pagenum":"pagenum"}'
        signstring = "uid=" + uid + "&api=" + "YQ001" + "&args=" + args + "&key=" + key
        sign = hashlib.md5(signstring.encode(encoding='UTF-8')).hexdigest()
        param = {"uid": "qqqq",
                 "api": "YQ001",
                 "args": '{"entName":"%s","startDate":"%s","endDate":"%s","eventlist":"%s",}' % (
                     entname, befor_30_dayes, nowdate, eventlist),
                 "sign": sign
                 }
        r = requests.get(url, params=param)
        data1 = r.json()
        print(r.url)
        # print(r.text)
        print(data1["code"])
        print(data1["msg"])
        self.assertEqual(data1["code"], "0000")
        self.assertEqual(data1["msg"], "查询成功")
        code = data1["code"]
        return code

    def yq002(self, entname, isimportant="true"):
        nowdate1 = datetime.datetime.now()
        befor_30_dayes = (nowdate1 + datetime.timedelta(days=-30)).strftime('%Y-%m-%d')
        nowdate = nowdate1.strftime('%Y-%m-%d')
        args = '{"entname":"entname","pagesize":"pagesize","pagenum":"pagenum"}'
        signstring = "uid=" + uid + "&api=" + "YQ002" + "&args=" + args + "&key=" + key
        sign = hashlib.md5(signstring.encode(encoding='UTF-8')).hexdigest()
        param = {"uid": "qqqq",
                 "api": "YQ002",
                 "args": '{"entName":"%s","startDate":"%s","endDate":"%s","isimportant":"%s"}' % (
                     entname, befor_30_dayes, nowdate, isimportant),
                 "sign": sign
                 }
        r = requests.get(url, params=param)
        data1 = r.json()
        print(r.url)
        # print(r.text)
        print(data1["code"])
        print(data1["msg"])
        self.assertEqual(data1["code"], "0000")
        self.assertEqual(data1["msg"], "查询成功")
        code = data1["code"]
        return code

    def gs024_jqtygm(self, industry, province):
        args = '{"entInfo":"entname"}'
        signstring = "uid=" + uid + "&api=" + "GS024" + "&args=" + args + "&key=" + key
        sign = hashlib.md5(signstring.encode(encoding='UTF-8')).hexdigest()
        param = {"uid": "qqqq",
                 "api": "GS024",
                 "args": '{"industry":"%s","province":"%s"}' % (industry, province),
                 "sign": sign
                 }
        r = requests.get(url, params=param)
        data1 = r.json()
        print(r.url)
        # print(r.text)
        print(data1["code"])
        print(data1["msg"])
        self.assertEqual(data1["code"], "0000")
        self.assertEqual(data1["msg"], "查询成功")
        code = data1["code"]
        return code

    def entinfo_and_id(self, entname, id, api):
        args = '{"entInfo":"entname"}'
        signstring = "uid=" + uid + "&api=" + api + "&args=" + args + "&key=" + key
        sign = hashlib.md5(signstring.encode(encoding='UTF-8')).hexdigest()
        param = {"uid": "qqqq",
                 "api": api,
                 "args": '{"entInfo":"%s","id":"%s"}' % (entname, id),
                 "sign": sign
                 }
        r = requests.get(url, params=param)
        data1 = r.json()
        print(r.url)
        # print(r.text)
        print(data1["code"])
        print(data1["msg"])
        self.assertEqual(data1["code"], "0000")
        self.assertEqual(data1["msg"], "查询成功")
        code = data1["code"]
        return code

    def name_and_pid(self, name, pid, eid, api):
        args = '{"entInfo":"name"}'
        signstring = "uid=" + uid + "&api=" + api + "&args=" + args + "&key=" + key
        sign = hashlib.md5(signstring.encode(encoding='UTF-8')).hexdigest()
        param = {"uid": "qqqq",
                 "api": api,
                 "args": '{"pid":"%s","name":"%s","eid":"%s"}' % (pid, name, eid),
                 "sign": sign
                 }
        r = requests.get(url, params=param)
        data1 = r.json()
        print(r.url)
        # print(r.text)
        print(data1["code"])
        print(data1["msg"])
        self.assertEqual(data1["code"], "0000")
        self.assertEqual(data1["msg"], "查询成功")
        code = data1["code"]
        return code

    def only_city(self, city, api):
        args = '{"entInfo":"entname"}'
        signstring = "uid=" + uid + "&api=" + api + "&args=" + args + "&key=" + key
        sign = hashlib.md5(signstring.encode(encoding='UTF-8')).hexdigest()
        param = {"uid": "qqqq",
                 "api": api,
                 "args": '{"city":"%s"}' % city,
                 "sign": sign
                 }
        r = requests.get(url, params=param)
        data1 = r.json()
        print(r.url)
        # print(r.text)
        print(data1["code"])
        print(data1["msg"])
        self.assertEqual(data1["code"], "0000")
        self.assertEqual(data1["msg"], "查询成功")
        code = data1["code"]
        return code

    def fx105_cpwsfx(self, entname, reson, type, status, pagesize=10, pagenum=1, ):
        args = '{"entInfo":"entname"}'
        signstring = "uid=" + uid + "&api=" + "FX105" + "&args=" + args + "&key=" + key
        sign = hashlib.md5(signstring.encode(encoding='UTF-8')).hexdigest()
        param = {"uid": "qqqq",
                 "api": "FX105",
                 "args": '{"entInfo":"%s","pageSize":"%s","pageNum":"%s","reson":["%s"],"type":["%s"],"status":["%s"],"sort":{"amount":"desc","trialDate":"asc"}}' % (
                     entname, pagesize, pagenum, reson, type, status),
                 "sign": sign
                 }
        r = requests.get(url, params=param)
        data1 = r.json()
        print(r.url)
        # print(r.text)
        print(data1["code"])
        print(data1["msg"])
        self.assertEqual(data1["code"], "0000")
        self.assertEqual(data1["msg"], "查询成功")
        code = data1["code"]
        return code

    def td002_tdjylb(self, entname, type, pagesize=10, pagenum=1):
        args = '{"entname":"entname","pagesize":"pagesize","pagenum":"pagenum"}'
        signstring = "uid=" + uid + "&api=" + "TD002" + "&args=" + args + "&key=" + key
        sign = hashlib.md5(signstring.encode(encoding='UTF-8')).hexdigest()
        param = {"uid": "qqqq",
                 "api": "TD002",
                 "args": '{"entInfo":"%s","type":"%s","pageSize":"%s","pageNum":"%s"}' % (
                     entname, type, pagesize, pagenum),
                 "sign": sign
                 }
        r = requests.get(url, params=param)
        data1 = r.json()
        print(r.url)
        # print(r.text)
        print(data1["code"])
        print(data1["msg"])
        self.assertEqual(data1["code"], "0000")
        self.assertEqual(data1["msg"], "查询成功")
        code = data1["code"]
        return code

    def sf002_sfpmlb(self, entname, subjectType, auctionStatus, pagesize=10, pagenum=1):
        args = '{"entname":"entname","pagesize":"pagesize","pagenum":"pagenum"}'
        signstring = "uid=" + uid + "&api=" + "SF002" + "&args=" + args + "&key=" + key
        sign = hashlib.md5(signstring.encode(encoding='UTF-8')).hexdigest()
        param = {"uid": "qqqq",
                 "api": "SF002",
                 "args": '{"entInfo":"%s","subjectType":"%s","auctionStatus":"%s","pageSize":"%s","pageNum":"%s"}' % (
                     entname, subjectType, auctionStatus, pagesize, pagenum),
                 "sign": sign
                 }
        r = requests.get(url, params=param)
        data1 = r.json()
        print(r.url)
        # print(r.text)
        print(data1["code"])
        print(data1["msg"])
        self.assertEqual(data1["code"], "0000")
        self.assertEqual(data1["msg"], "查询成功")
        code = data1["code"]
        return code

    def entinfo_and_stocktype(self, entname, stocktype, api):
        args = '{"entname":"entname","stocktype":"stockType"}'
        signstring = "uid=" + uid + "&api=" + api + "&args=" + args + "&key=" + key
        sign = hashlib.md5(signstring.encode(encoding='UTF-8')).hexdigest()
        param = {"uid": "qqqq",
                 "api": api,
                 "args": '{"entInfo":"%s","stockType":"%s"}' % (entname, stocktype),
                 "sign": sign
                 }
        r = requests.get(url, params=param)
        data1 = r.json()
        print(r.url)
        # print(r.text)
        # print(data1["code"])
        # print(data1["msg"])
        self.assertEqual(data1["code"], "0000")
        self.assertEqual(data1["msg"], "查询成功")
        code = data1["code"]
        return code

    def gs028_ssnbxq(self, entname, table, stocktype, pagesize=5, pagenum=1):
        args = '{"entname":"entname","table":"table","stocktype":"stockType","pagesize":"pagesize","pagenum":"pagenum"}'
        signstring = "uid=" + uid + "&api=" + "GS028" + "&args=" + args + "&key=" + key
        sign = hashlib.md5(signstring.encode(encoding='UTF-8')).hexdigest()
        param = {"uid": "qqqq",
                 "api": "GS028",
                 "args": '{"entInfo":"%s","table":"%s","stockType":"%s","pageSize":"%s","pageNum":"%s"}' % (
                     entname, table, stocktype, pagesize, pagenum),
                 "sign": sign
                 }
        r = requests.get(url, params=param)
        data1 = r.json()
        print(r.url)
        # print(r.text)
        # print(data1["code"])
        # print(data1["msg"])
        self.assertEqual(data1["code"], "0000")
        self.assertEqual(data1["msg"], "查询成功")
        code = data1["code"]
        return code

    def id_and_libtype(self, id, libtype, api):
        args = '{"id":"id","libtype":"libtype"}'
        signstring = "uid=" + uid + "&api=" + api + "&args=" + args + "&key=" + key
        sign = hashlib.md5(signstring.encode(encoding='UTF-8')).hexdigest()
        param = {"uid": "qqqq",
                 "api": api,
                 "args": '{"id":"%s","libtype":"%s"}' % (id, libtype),
                 "sign": sign
                 }
        r = requests.get(url, params=param)
        data1 = r.json()
        print(r.url)
        # print(r.text)
        # print(data1["code"])
        # print(data1["msg"])
        self.assertEqual(data1["code"], "0000")
        self.assertEqual(data1["msg"], "查询成功")
        code = data1["code"]
        return code

    def parentId(self, parentId, api):
        args = '{"parentId":"parentId"}'
        signstring = "uid=" + uid + "&api=" + api + "&args=" + args + "&key=" + key
        sign = hashlib.md5(signstring.encode(encoding='UTF-8')).hexdigest()
        param = {"uid": "qqqq",
                 "api": api,
                 "args": '{"parentId":"%s"}' % (parentId),
                 "sign": sign
                 }
        r = requests.get(url, params=param)
        data1 = r.json()
        print(r.url)
        #print(r.text)

        print(data1["code"])
        print(data1["msg"])
        self.assertEqual(data1["code"], "0000")
        self.assertEqual(data1["msg"], "查询成功")
        code = data1["code"]
        return code

    def entname_and_name(self, entname, name,api):
        args = '{"entInfo":"entname"}'
        signstring = "uid=" + uid + "&api=" + api + "&args=" + args + "&key=" + key
        sign = hashlib.md5(signstring.encode(encoding='UTF-8')).hexdigest()
        param = {"uid": "qqqq",
                 "api": api,
                 "args": '{"entInfo":"%s","name":"%s"}' % (entname, name),
                 "sign": sign
                 }
        r = requests.get(url, params=param)
        data1 = r.json()
        print(r.url)
        # print(r.text)
        print(data1["code"])
        print(data1["msg"])
        self.assertEqual(data1["code"], "0000")
        code = data1["code"]
        return code

    def test_yq001(self):  # 舆情分析事件统计接口
        self.yq001("青岛银行股份有限公司", "骗贷套贷")

    def test_yq002(self):  # 舆情分析列表接口
        self.yq002("青岛银行股份有限公司")

    def test_jj001(self):  # 基金列表接口
        self.only_entname("平安道远投资管理（上海）有限公司", "JJ001")

    def test_jj002(self):  # 基金详情接口
        self.only_entname("平安道远投资管理（上海）有限公司", "JJ002")

    def test_td002(self):  # 土地交易列表接口
        self.td002_tdjylb("小米科技有限责任公司", "all", 10, 1)

    def test_td003(self):  # 土地供应信息详情
        self.only_id("e_26c9b793849b31ebd8b1424a2e5510b3", "TD003")

    def test_td004(self):  # 土地抵押信息详情

        self.only_id("e_30f70e30e7833b6b16b37f2a1cc99eba", "TD004")

    def test_td005(self):  # 土地转让信息详情
        self.only_id("e_b4cf344f8f1c12e6f08a2981a7d7f53d", "TD005")

    def test_di005_copyright(self):  # 知识产权接口：列表
        self.entname_and_type("广发证券股份有限公司", "copyright","DI005")

    def test_gs001(self):  # 模糊搜索
        self.only_entinfo("广发证券股份有限公司", "GS001")

    def test_gs002(self):  # 股东标签接口
        self.only_entinfo("小米科技有限责任公司", "GS002")

    def test_gs003(self):  # 任职接口
        self.only_entinfo("小米科技有限责任公司", "GS003")

    def test_gs004(self):  # 照面信息接口
        self.only_entinfo("新湖中宝股份有限公司", "GS004")

    def test_gs005(self):  # 对外投资统计接口
        self.only_entinfo("广发证券股份有限公司", "GS005")

    def test_gs006(self):  # 企业股东接口
        self.only_entinfo("小米科技有限责任公司", "GS006")

    def test_gs007(self):  # 受益所有人接口
        self.only_entinfo("小米科技有限责任公司", "GS007")

    def test_gs011(self):  # 年报详情接口
        self.gs011("乐视网信息技术（北京）股份有限公司", "2017")

    def test_gs012(self):  # 动产抵押列表接口
        self.only_entinfo("小米科技有限责任公司", "GS012")

    def test_gs013(self):  # 股权出质列表接口
        self.only_entinfo("小米科技有限责任公司", "GS013")

    def test_gs014(self):  # 股权冻结列表接口
        self.only_entinfo("q7aabbdc6786848fe835e9a7a401bf654", "GS014")

    def test_gs015(self):  # 股权冻结详情接口
        self.parentId("ff80808165d19fd80165d5a56976558c", "GS015")

    def test_gs016(self):  # 变更分析统计接口
        self.only_entinfo("广发证券股份有限公司", "GS016")

    def test_gs017(self):  # 变更详情列表接口
        self.only_entinfo("广发证券股份有限公司", "GS017")

    def test_gs019(self):  # 关联分析接口
        self.entname_and_name("小米科技有限责任公司",'', "GS019")

    def test_gs020(self):  # 对外投资图谱接口
        self.only_entinfo("广发证券股份有限公司", "GS020")

    def test_gs021(self):  # 对外投资列表接口
        self.only_entinfo("广发证券股份有限公司", "GS021")

    def test_gs022(self):  # 上市公司股权质押列表接口#selfPledge  holdPledge  pledgee
        self.entname_and_type("qd102d44f2c284b774c3d7ee2f6aec122", "selfPledge", "GS022")

    def test_gs023(self):  # 上市公司并购重组列表接口
        self.only_entinfo("广发证券股份有限公司", "GS023")

    def test_gs024(self):  # 近期同业规模接口
        self.gs024_jqtygm("零售业", "北京")

    def test_gs025(self):  # 上市公司股权质押详情接口
        self.only_id("e_1f328b0874485e8b43a9df3d8b9742e2", "GS025")

    def test_gs026(self):  # 上市公司基础信息
        self.entinfo_and_stocktype('青岛银行股份有限公司', 'A股 002948', "GS026")

    def test_gs027(self):
        self.only_entinfo('qc67ff91aad074b0ba3292e7b40c8ad19', 'GS027')

    def test_gs028(self):  # 上市公司年报详情接口
        self.gs028_ssnbxq("青岛银行股份有限公司", 'zcfz', 'A股 002948')

    def test_gs032(self):  # 上市公司前十大股东
        self.entinfo_and_stocktype('青岛银行股份有限公司', 'A股 002948', "GS032")

    def test_gs033(self):  # 许可证列表接口
        self.only_entinfo('华泰财产保险有限公司', 'GS033')

    def test_gs034_00(self):  # 许可证详情接口
        self.id_and_libtype('qa7cf2825694344bebdd02502829930ae', '食品经营许可', 'GS034')

    def test_gs034_01(self):
        self.id_and_libtype('e_5b560f4ae762588320996274921c19fe', '食品生产许可', 'GS034')

    def test_gs034_02(self):
        self.id_and_libtype('e_421d18d64c45180a0f6caaac412e0fdc', '保健食品许可', 'GS034')

    def test_gs034_03(self):
        self.id_and_libtype('e_a2e3f1af9f21623e307c10294237a3f9', '药品经营许可', 'GS034')

    def test_gs034_04(self):
        self.id_and_libtype('e_6058fd40070ec16c91517ca94e46b91c', '互联网药品信息服务资格证', 'GS034')

    def test_gs034_05(self):
        self.id_and_libtype('q3dd0a43c8d9807dd9ca310d0744b09f6', '互联网药品交易服务', 'GS034')

    def test_gs034_06(self):
        self.id_and_libtype('e_ec1de868f5760fe15a6ca1872db7e985', '医疗器械经营企业', 'GS034')

    def test_gs034_07(self):
        self.id_and_libtype('e_d66b4ac8a401cb1458dba55c7faa2113', '药品GSP认证', 'GS034')

    def test_gs034_08(self):
        self.id_and_libtype('e_007bdcac96c13d9e9e338bf4d6417314', '网上药店', 'GS034')

    def test_gs035(self):  # 工商行政许可接口
        self.entname_and_page('GS035', 'q6a0ac6a809881aecf3b8167c07f033cb')

    def test_gs036(self):  # 信用中国行政许可接口
        self.entname_and_page('GS036', '小米科技有限责任公司')

    def test_gs037(self):  # 医院慈善机构照面信息
        self.only_entinfo('h_a837bc774385730d86c205f4fd139052', 'GS037')

    def test_gs038(self):  # 自然人投资任职接口
        self.name_and_pid('陈喆', '0006687', '', 'GS038')

    def test_zp001(self):  # 人才分析接口
        self.only_entinfo("广发证券股份有限公司", "ZP001")

    def test_di001(self):  # 知识产权接口：统计
        self.only_entinfo("广发证券股份有限公司", "DI001")

    def test_di002(self):  # 知识产权接口：专利类别前十
        self.only_entinfo("广发证券股份有限公司", "DI002")

    def test_di003(self):  # 知识产权接口：IPC类别前十
        self.only_entinfo("广发证券股份有限公司", "DI003")

    def test_di004(self):  # 知识产权接口：商标类别前十
        self.only_entinfo("广发证券股份有限公司", "DI004")

    def test_td001(self):  # 土地交易统计接口
        self.only_entinfo("广发证券股份有限公司", "TD001")

    def test_sf001(self):  # 司法拍卖统计接口
        self.only_entinfo("九鼎房地产有限公司", "SF001")

    def test_sf002(self):  # 司法拍卖列表接口
        self.sf002_sfpmlb("朝阳天富物业管理有限责任公司", '', '')

    def test_sf003(self):  # 司法拍卖详情查询
        self.entinfo_and_id("盘锦龙驿房地产开发有限责任公司", "744f0ff2b924cd147ff6787e7ce4d6ed", "SF003")

    def test_fx001(self):  # 风险传导企业列表接口
        self.only_entinfo("q20a22b453196756629588f0d6df2df98", "FX001")

    def test_fx002(self):  # 风险信号查询接口
        self.only_entinfo("q7aabbdc6786848fe835e9a7a401bf654", "FX002")

    def test_fx003(self):  # 关联风险信号查询接口
        self.only_entinfo("q7aabbdc6786848fe835e9a7a401bf654", "FX003")

    def test_fx003_01(self):  # 关联风险信号查询接口
        self.only_entinfo("小米科技有限责任公司", "FX003")

    def test_fx004(self):  # 区域司法风险接口
        self.only_city("杭州市", "FX004")

    def test_fx006(self):  # 全量风险统计接口
        self.only_entinfo("小米科技有限责任公司", "FX006")

    def test_fx101(self):  # 全量风险司法时间统计
        self.only_entinfo("广发证券股份有限公司", "FX101")

    def test_fx102(self):  # 全量风险开庭公告分析
        self.only_entinfo("广发证券股份有限公司", "FX102")

    def test_fx103(self):  # 全量风险裁判文书分析
        self.only_entinfo("小米科技有限责任公司", "FX103")

    def test_fx104(self):  # 开庭公告列表分页查询
        self.entname_and_page("FX104", "小米科技有限责任公司")

    def test_fx105(self):  # 裁判文书列表分页查询
        self.fx105_cpwsfx("小米科技有限责任公司", "合同纠纷", "民事案件", "应诉方")

    def test_fx106(self):  # 裁判文书详情查询
        self.entinfo_and_id("小米科技有限责任公司", "e_72c4806b31d413dee524df79f3c11b5e036dc1cf79de147019229331b238eeec", "FX106")

    def test_fx107(self):  # 被执行人列表分页查询
        # 加一个isRecent=Y 时查询近期数据
        self.entname_and_page("FX107", "小米科技有限责任公司")

    def test_fx108(self):  # 失信被执行人列表分页查询
        # 加一个isRecent=Y 时查询近期数据
        self.entname_and_page("FX108", "小米科技有限责任公司", 10, 1)

    def test_fx109(self):  # 曝光台列表分页查询
        self.entname_and_page("FX109", "小米科技有限责任公司", 10, 1)

    def test_fx110(self):  # 法院公告列表分页查询
        self.entname_and_page("FX110", "乐视网信息技术（北京）股份有限公司", 10, 2)

    def test_fx201(self):  # 抽查检查分页查询
        self.entname_and_page("FX201", "邵阳市大祥区百乐饮料厂", 10, 1)

    def test_fx202(self):  # 经营异常分页查询
        self.entname_and_page("FX202", "q672fc489a2d8ae11e11474ad5de6d88a", 10, 1)

    def test_fx203(self):  # 海关失信分页查询
        self.entname_and_page("FX203", "福州甩酷动漫科技有限公司", 10, 1)

    def test_fx204(self):  # 破产清算分页查询
        self.entname_and_page("FX204", "qee8d6339d22a05b745ba45e68cc890dd", 10, 1)

    def test_fx205(self):  # 破产案件分页查询
        self.entname_and_page("FX205", "四川九峰投资有限公司", 10, 2)

    def test_fx206(self):  # 严重违法失信分页查询
        self.entname_and_page("FX206", "q38a70ae77b1549eb976b60b37249be99", 10, 1)

    def test_fx301(self):  # 税收违法分页查询
        self.entname_and_page("FX301", "万载县郝梦箱包制造厂", 10, 1)

    def test_fx302(self):  # 税务非正常户分页查询
        self.entname_and_page("FX302", "广西鸿海投资集团有限公司", 10, 1)

    def test_fx303(self):  # 欠税记录查询
        self.only_entinfo("万科企业股份有限公司", "FX303")

    def test_fx401(self):  # 行政处罚列表
        self.entname_and_page("FX401", "乐视网信息技术（北京）股份有限公司", 10, 2)

    def test_fx402(self):  # 信用中国行政处罚列表
        self.entname_and_page("FX402", "乐视网信息技术（北京）股份有限公司", 10, 2)

    def test_fx501(self):  # 风险信号-司法协助详情
        self.only_entinfo("q04a91c5d1c9fb2b0f3b23505f1a080ae", "FX501")

    def test_fx502(self):  # 风险信号-股权质押列表
        self.entname_and_page("FX502", "q73b2159efe0d73ab1561250119ba4c9e")

    def test_fx503(self):  # 风险信号-动产抵押列表接口
        self.entname_and_page("FX503", "qb380388edb35b6efb1d8706d8e04639b")

    def test_fx504(self):  # 风险信号-土地抵押信息
        self.entname_and_page("FX504", "霍州市中镇五交化机电有限责任公司")

    def test_fx505(self):  # 风险信号-动产抵押详情接口
        self.only_id("142000006979752925", "FX505")

    def test_fx506(self):  # 风险信号-行政处罚详情接口
        self.only_id("142000006975376817", "FX506")

    def test_zp001(self):  # 人才分析接口
        self.only_entinfo("万科企业股份有限公司", "ZP001")


if __name__ == "__main__":
    unittest.main()
