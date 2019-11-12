# -*- coding: utf-8 -*-
import xlrd
import shutil
import os


def read_excel():
    # 打开文件
    shutil.copy(r'.\集团财务报表编制表.xlsx', r'D:\java')
    # workbook = xlrd.open_workbook(r'集团财务报表编制表.xlsx')
    # 获取所有sheet
    # print(workbook.sheet_names())  # [u'sheet1', u'sheet2']
    # # 获取sheet
    # sheet = workbook.sheet_names()[0]
    # sheet_data = workbook.sheet_by_name(sheet)
    # # print(sheet_data)
    # # sheet的名称，行数，列数
    # # print(sheet_data.name, sheet_data.nrows, sheet_data.ncols)
    # rows = sheet_data.row_values(0)  # 获取第四行内容
    # cols = sheet_data.col_values(2)  # 获取第三列内容
    # # print(rows)
    # for i, j in enumerate(rows):
    #     print(i, ':', j)
    #     for i in range(sheet_data.nrows):
    #         strr = sheet_data.row_values(i)[5][:5]
    #         if (strr == 'AXIAL'):
    #             dicom_path = sheet_data.row_values(i)[15]
    #             row_path = sheet_data.row_values(i)[16]
    #             print(row_path)
    #             roww = row_path.split('\\', 3)[3]
    #             # print(roww)
    #             # row_path='C:\Users\xxx\Desktop\xxx'
    #             path_now = roww
    #             # path_now = os.path.join('jw', roww)
    #             # print(path_now)
    #             shutil.copytree(path_now, r'D:\java')
    #             # shutil.copytree(row_path,r'C:\Users\xxx\Desktop')
    #             break

if __name__ == '__main__':
    read_excel()
