import xlrd
import json
import operator

class Read_Xlsx():
    def read_xlsx(filename='D:/requests_test_public/config/entname.xlsx'):
        # 打开excel文件
        data1 = xlrd.open_workbook(filename)
        # 读取第一个工作表
        table = data1.sheets()[0]
        # 统计行数
        n_rows = table.nrows

        data1 = []
        data=[]
        for v in range(0, n_rows):
            # 每一行数据形成一个列表
            values = table.row_values(v)
            data1.append(values)
        for i in data1:
            for a in i:
                data.append(a)
        print(data)
        return data

if __name__ == '__main__':
    Read_Xlsx.read_xlsx()