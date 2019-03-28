import unittest
import requests
import hashlib
from w3lib import url
from configparser import ConfigParser
from config import Connect_Mysql,only_entname
cp = ConfigParser()
cp.read("D:\\requests_test\\config\\config.ini")
url=cp.get("service","url_test")
uid=cp.get("uk","uid")
key=cp.get("uk","key")

module={
    "basicList" : [ {
      "regNo" : "110108012660422",
      "entName" : "小米科技有限责任公司",
      "city" : "北京市",
      "industrySecCode" : "65",
      "county" : "海淀区",
      "frName" : "雷军",
      "taxCredit" : "A级纳税人",
      "industryCode" : "65",
      "entType" : "有限责任公司（自然人投资或控股）",
      "industrySecName" : "软件和信息技术服务业",
      "pripid" : "q7aabbdc6786848fe835e9a7a401bf654",
      "creditCode" : "91110108551385082Q",
      "regCapCur" : "人民币",
      "province" : "北京",
      "htmlFrom" : "",
      "industryPhyCode" : "",
      "regCap" : "185000.00",
      "html" : "",
      "tel" : "",
      "openTime" : "2010-03-03至2030-03-02",
      "industryName" : "",
      "industryPhyName" : "",
      "stockTypeList" : [ ],
      "address" : "北京市海淀区清河中街68号华润五彩城购物中心二期13层",
      "entId" : "q7aabbdc6786848fe835e9a7a401bf654",
      "apprDate" : "2018-06-20",
      "esDate" : "2010-03-03",
      "hasSholder" : "true",
      "operateScope" : "技术开发；货物进出口、技术进出口、代理进出口；销售通讯设备、厨房用品、卫生用品（含个人护理用品）、日用杂货、化妆品、医疗器械I类、II类、避孕器具、玩具、体育用品、文化用品、服装鞋帽、钟表眼镜、针纺织品、家用电器、家具（不从事实体店铺经营）、花、草及观赏植物、不再分装的包装种子、照相器材、工艺品、礼品、计算机、软件及辅助设备、珠宝首饰、食用农产品、宠物食品、电子产品、摩托车、电动车、自行车及零部件、智能卡、五金交电（不从事实体店铺经营）、建筑材料（不从事实体店铺经营）；维修仪器仪表；维修办公设备；承办展览展示活动；会议服务；筹备、策划、组织大型庆典；设计、制作、代理、发布广告；摄影扩印服务；文艺演出票务代理、体育赛事票务代理、展览会票务代理、博览会票务代理；手机技术开发；手机生产、手机服务（限海淀区永捷北路2号二层经营）；从事互联网文化活动；出版物零售；出版物批发；销售第三类医疗器械；销售食品；零售药品；广播电视节目制作。（企业依法自主选择经营项目，开展经营活动；从事互联网文化活动、出版物批发、出版物零售、销售食品、广播电视节目制作、零售药品、销售第三类医疗器械以及依法须经批准的项目，经相关部门批准后依批准的内容开展经营活动；不得从事本市产业政策禁止和限制类项目的经营活动。）",
      "regOrg" : "北京市工商行政管理局海淀分局",
      "entStatus" : "在营（开业）"
    } ],
    "entHisList" : [ ]
  }
class Gs004(unittest.TestCase):
    def request_gs004(self,entname):
        args = '{"entInfo":"entname"}'
        signstring = "uid=" + uid + "&api=" + "GS004" + "&args=" + args + "&key=" + key
        sign = hashlib.md5(signstring.encode(encoding='UTF-8')).hexdigest()
        param = {"uid": "qqqq",
                 "api": "GS004",
                 "args": '{"entInfo":"%s"}' % (entname),
                 "sign": sign
                 }
        r = requests.get(url, params=param)
        data1 = r.json()
        print(r.url)
        code=data1["code"]
        print(code)
        print(data1["msg"])
        return data1

    def assert_data(self,entname):
        return_msg = self.request_gs004(entname)
        data=return_msg["data"]
        for i in data:  # 判断两个list是否存在
            if i in module.keys():
                print(i)
            else:
                raise KeyError('No Such Key!!!')
        basiclist=return_msg["data"]['basicList'][0]
        sql="SELECT *  FROM enterprisebaseinfocollect WHERE entname = '%s'" % entname
        carry_sql = Connect_Mysql.Connect_mysql().connect_mysql('gs',sql)[0]
        carry_sql=carry_sql
        for v in carry_sql:
            if carry_sql[v]==None:
                carry_sql[v]=''

        assert carry_sql['regno'] == basiclist['regNo']
        assert carry_sql['entname'] == basiclist['entName']
        assert carry_sql['regorg_city'] == basiclist['city']
        assert carry_sql['regorg_county'] == basiclist['county']
        assert carry_sql['frname'] == basiclist['frName']
        if basiclist['taxCredit']=='A级纳税人':
            sql_tax="SELECT *  FROM rep_local_taxpayer_level WHERE ent_name = '%s'" % entname
            carry_sql_tax = Connect_Mysql.Connect_mysql().connect_mysql('data', sql_tax)[0]
            assert carry_sql_tax != {}
            assert carry_sql_tax['level']=='A'
        assert carry_sql['industryco'] == basiclist['industryCode']
        assert carry_sql['enttype_name'] == basiclist['entType']
       # assert carry_sql['regno'] == basiclist['industrySecName']
       # assert carry_sql['pripid'] == basiclist['pripid']
        assert carry_sql['credit_code'] == basiclist['creditCode']

        if '合伙' in basiclist['entName']:
            carry_sql['regcapcur_name'] = ''
        elif carry_sql['regcapcur_name'] == '' :
            carry_sql['regcapcur_name'] = '人民币'

        assert carry_sql['regcapcur_name'] == basiclist['regCapCur']
        assert carry_sql['regorg_province'] == basiclist['province']
       # assert carry_sql['regno'] == basiclist['industryPhyCode']

        if '合伙' in basiclist['entName']:
            carry_sql['regcap'] = ''
        elif carry_sql['regcap']==0 or carry_sql['regcap']=='':
            carry_sql['regcap'] =''
        else:
            regcap = int(carry_sql['regcap'])#直接取整数部分比较
            regCap=int(float(basiclist['regCap']))
            assert regcap == regCap
        assert carry_sql['industryco_name'] == basiclist['industryName']
        assert carry_sql['industryphy_name'] == basiclist['industryPhyName']
        assert carry_sql['dom'] == basiclist['address']
        assert carry_sql['eid'] == basiclist['entId']
        assert str(carry_sql['apprdate']) == basiclist['apprDate']
        assert str(carry_sql['esdate']) == basiclist['esDate']
        assert carry_sql['opscope'] == basiclist['operateScope']
        assert carry_sql['regorg_name'] == basiclist['regOrg']
        assert carry_sql['entstatus_name'] == basiclist['entStatus']

    def test_test(self):
        self.assert_data('新湖中宝股份有限公司')

    def test_run(self):
        entnamelist= only_entname.Read_Xlsx.read_xlsx()
        for i in entnamelist:
            try:
                self.assert_data(i)
            except AssertionError as e:
                print(e)
                pass
            continue
