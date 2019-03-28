import pymysql as pymysql

class Connect_mysql:
        def connect_mysql(self,dbvalue,sqlvalue):
                # 连接数据库
                hostvalue = '10.1.1.103'
                uservalue = 'gsuser'
                passwordvalue = 'gsuser'
                portvalue = 3306
                connection = pymysql.connect(host=hostvalue, user=uservalue, password=passwordvalue, db=dbvalue,
                                port=portvalue, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
                # 通过cursor创建游标
                cursor = connection.cursor()
                # 创建sql 语句，并执行

                cursor.execute(sqlvalue)
                #result = cursor.fetchone()  # 查询数据库单条数据
                result = cursor.fetchall() #查询数据库多条数据
                # 提交sql
                connection.commit()
                #connection.close()
                print(result)
                return result
