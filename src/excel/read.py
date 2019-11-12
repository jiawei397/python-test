import xlrd
import xlsxwriter
from datetime import date,datetime

file = '集团财务报表编制表.xlsx'

def read_excel():

    wb = xlrd.open_workbook(filename=file)#打开文件
    # print(wb.sheet_names())#获取所有表格名字

    sheet1 = wb.sheet_by_index(2)#通过索引获取表格
    # sheet2 = wb.sheet_by_name('1.货币资金')#通过名字获取表格
    # print(sheet1,sheet2)
    # print(sheet1.name,sheet1.nrows,sheet1.ncols)

    rows = sheet1.row_values(3)#获取行内容
    # cols = sheet1.col_values(3)#获取列内容
    print(rows)
    # print(cols)
    #
    print(sheet1.cell(3,3).value)#获取表格里的内容，三种方式
    # print(sheet1.cell_value(1,0))
    # print(sheet1.row(1)[0].value)

    val = sheet1.cell(3,3).value


    row = 3

    col = 3

    # 类型 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
    ctype = 2
    value = 33

    xf = 0  # 扩展的格式化

    sheet1.put_cell(row, col, ctype, value, xf)

    print(sheet1.cell(3, 3).value)  # 获取表格里的内容，三种方式


read_excel()
