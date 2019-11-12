import openpyxl
import os
import re

file = 'demo.xlsx'

# 遍历指定目录，显示目录下的所有文件名
def eachFile(filepath):
    pathDir = os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s/%s' % (filepath, allDir))
        # print(child)  # .decode('gbk')是解决中文显示乱码问题
        read_excel(child)

    # print(list)
    # print(sum(list))




# 读取文件内容并打印
# def readFile(filename):
#     fopen = open(filename, 'r')  # r 代表read
#     for eachLine in fopen:
#         print("读取到得内容如下：", eachLine)



# file = '集团财务报表编制表.xlsx'

# list = []


# def is_number(s):
#     try:
#         float(s)
#         return True
#     except ValueError:
#         pass
#
#     try:
#         import unicodedata
#         unicodedata.numeric(s)
#         return True
#     except (TypeError, ValueError):
#         pass
#
#     return False

pattern = re.compile(r'^[-+]?[-0-9]\d*\.\d*|[-+]?\.?[0-9]\d*$')
map = {}

def is_number(num):
  result = pattern.match(str(num))
  if result:
    return True
  else:
    return False

def get_key(table, row, num):
    return table + '-' + str(row) + '-' + str(num)

def is_key(table, row, num):
    return get_key(table,row, num) in map


def read_excel(file):
    data = openpyxl.load_workbook(file)
    # print(data.get_named_ranges())  # 输出工作页索引范围
    # print(data.get_sheet_names())  # 输出所有工作页的名称
    # 取第一张表
    # sheetnames = data.get_sheet_names()

    # table = data.get_sheet_by_name('A3_01_SBL_PRC') #sheetnames[2]
    # print(data.worksheets)

    for table in data.worksheets:
        if table.title.find('清单') == -1 and table.title.find('填写须知') == -1:
            read_table(table)

    # table = data.worksheets[2]

    # read_table(table)
    # values = ['E', 'X', 'C', 'E', 'L']
    # for value in value:
    #     table.cell(nrows + 1, 1).value = value
    #     nrows = nrows + 1
    # print(table.cell(4, 4).value)
    # table.cell(4, 4).value = 33
    # data.save('excel_test.xlsx')

    # list.append(table.cell(4, 4).value)

def read_table(table):
    # print(table.title)  # 输出表名
    nrows = table.max_row  # 获得行数
    ncolumns = table.max_column  # 获得行数
    # print(ncolumns)

    for row in range(1, nrows):
        for col in range(1, ncolumns):
            val = table.cell(row, col).value
            if val and is_number(val):
                # print('%s/%s/%s' % (row, col, val))
                key = get_key(table.title, row, col)
                map.setdefault(key, [])
                map[key].append(val)

# read_excel(file)
# print(map)

def write_excel(file):
    data = openpyxl.load_workbook(file)
    # table = data.worksheets[2]
    # table.cell(4, 4).value = val
    # data.save('excel_test.xlsx')
    for table in data.worksheets:
        if table.title.find('清单') == -1 and table.title.find('填写须知') == -1:
            nrows = table.max_row  # 获得行数
            ncolumns = table.max_column  # 获得行数

            for row in range(1, nrows):
                for col in range(1, ncolumns):
                    if is_key(table.title, row, col):
                        table.cell(row, col).value = sum(map[get_key(table.title, row, col)])

    data.save('汇总表.xlsx')

eachFile('data')
write_excel(file)
# print(map)
