import unittest
import requests
import hashlib
from w3lib import url
from configparser import ConfigParser
from config import Connect_Mysql,only_entname
from FkTestSuit import test_all_api_0000
from decimal import Decimal
from datetime import datetime
cp = ConfigParser()
cp.read("D:\\requests_test\\config\\config.ini")
url=cp.get("service","url_test")
uid=cp.get("uk","uid")
key=cp.get("uk","key")

class Gs004(unittest.TestCase):
    def request_gs006(self,entname):
        data=test_all_api_0000.All_api_0000.only_entinfo(self,entname ,'GS006')['data']
        if len(data)!=0:
            pripidsql='SELECT pripid FROM gs.enterprisebaseinfocollect WHERE entname = "%s" '%entname
            pripid_sql=Connect_Mysql.Connect_mysql().connect_mysql('gs',pripidsql)[0]["pripid"]#查询主体表
            invsql="SELECT inv,invtype,conprop,subconam,condate FROM gs.e_inv_investment WHERE pripid = '%s' ORDER BY conprop DESC"%pripid_sql
            inv_sql = Connect_Mysql.Connect_mysql().connect_mysql('gs', invsql)#主体表中的pripid查询inv表

            for i in range(0,len(inv_sql)):
                if inv_sql[i]['conprop'] != None:# 数据库中出资比例不为null
                    inv_sql[i]['conprop']=float(Decimal(inv_sql[i]['conprop']).quantize(Decimal('0.00')))#四舍五入数据库中出资比例转换成float类型
                    fundedRatio=float(Decimal(float(data[i]['fundedRatio'].replace('%',''))).quantize(Decimal('0.00')))#四舍五入接口中出资比例转换成float类型
                    try:
                        if inv_sql[i]['conprop']==fundedRatio or inv_sql[i]['conprop']==fundedRatio+0.01:#比较（因不是真正的四舍五入方法有偏差，加了0.01）
                            pass
                    except:
                        raise
                else:
                    assert data[i]['fundedRatio'] == ""#数据库中出资比例字段为null，断言接口返回为空
                if inv_sql[i]['subconam']!=None:#数据库中出资额度不为null
                    inv_sql[i]['subconam']=str(Decimal(inv_sql[i]['subconam']).quantize(Decimal('0.00')))#四舍五入出资额度
                    try:
                        assert inv_sql[i]['subconam'] == data[i]['subConam']    #比较（可能也有偏差，暂未发现）
                    except:
                        raise
                else:
                    print(data[i]['shareholderName'])
                    assert inv_sql[i]['subconam'] == "" or inv_sql[i]['subconam'] ==None #数据库出资额度为null，断言接口返回为空
                if data[i]['conDate']!='': #数据库中投资日期不为null
                    condate = inv_sql[i]['condate'].strftime('%Y-%m-%d')  # 时间格式转换
                    assert condate == data[i]['conDate'] #断言接口返回相等
                else :
                    try:
                        if inv_sql[i]['condate']==None:#数据库中为null
                            assert data[i]['conDate']==''#断言接口返回为空
                        else:   #数据库不为空，接口返回为空时， 成立日期纠错
                            condate1 = int(inv_sql[i]['condate'].strftime('%Y%m%d'))
                            esdate_sql='SELECT esdate FROM gs.enterprisebaseinfocollect WHERE entname = "%s" '%entname
                            esdate=int(Connect_Mysql.Connect_mysql().connect_mysql('gs', esdate_sql)[0]['esdate'].strftime('%Y%m%d'))
                            assert condate1 < esdate#与查询企业主体表中的成立日期相比较
                    except:
                       raise
            for i in range(0,len(inv_sql)):#直接断言股东名称和股东类型
                assert inv_sql[i]['inv'] == data[i]['shareholderName']
                if inv_sql[i]['invtype']=='' or inv_sql[i]['invtype']==None:
                    assert data[i]['shareholderType']==''
                else:
                    assert inv_sql[i]['invtype'] == data[i]['shareholderType']



        else:
            print('data = null')

    def test_test(self):
        self.request_gs006('国创开元股权投资基金（有限合伙）')

    def test_run(self):
        entnamelist = only_entname.Read_Xlsx.read_xlsx()
        for i in entnamelist:
            try:
                self.request_gs006(i)
            except :

                raise

            continue
