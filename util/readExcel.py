# -*- coding:utf-8 -*-
__author__ = "lizhouquan"

import xlrd


# 读取excel中每一行的数据，并保存为一个列表

def read_xlsx(path):
    # book = xlrd.open_workbook(path)   # 打开excel表
    with xlrd.open_workbook(path, 'rb') as book:
        table = book.sheet_by_index(0)  # 找到sheet页

        # 获取总行数总列数
        row_num = table.nrows
        col_num = table.ncols

        xlsx_list = []
        key = table.row_values(0)  # 这是第一行数据,返回一个列表，作为字典的key值
        if row_num <= 1:
            print('excel为空')
        else:
            j = 1  # 从第二行开始获取值
            for i in range(row_num - 1):  # 有多少行，读多少次
                xlsx_dict = {}
                values = table.row_values(j)
                for x in range(col_num):  # 有多少列，赋值多少次
                    # 把key值对应的value赋值给key，每行循环一次
                    xlsx_dict[key[x]] = values[x]
                j = j + 1
                # 把字典添加到列表中
                xlsx_list.append(xlsx_dict)
            return xlsx_list


if __name__ == '__main__':
    data = read_xlsx('../data/user_lizhouquan.xlsx')
    print(data)
    print(data[0].get('phonenumber'))