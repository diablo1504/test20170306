# coding=utf-8
import urllib2
import os
import xlrd
from xlutils.copy import copy

excel_result = []
file_list = []
PASS_FINAL = 0
ERROR_FINAL = 0
FAIL_FINAL = 0
pathDir = os.listdir("E:\\test_result\\20170223_160609\\")
# style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',num_format_str='#,##0.00')

#替换文件名作为可解析的HTML格式
# for allDir in pathDir:
#     child = os.path.join('%s%s' % ("E:\\test_result\\20170223_160609\\", allDir))
#     child = child.replace('\\', '/')
#     file_list.append(child)
# print file_list
# #统计测试结果情况
# for i in range(0, len(file_list)):
#     url = "file:///" + file_list[i]
#     content = urllib2.urlopen(url).read()
#     PASS = content.count('pass</a>')
#     PASS_FINAL += PASS
#     ERROR = content.count('error</a>')
#     ERROR_FINAL += ERROR
#     FAIL = content.count('fail</a>')
#     FAIL_FINAL += FAIL
#     if ERROR != 0 or FAIL != 0:
#         os.renames(file_list[i], file_list[i][:-5] + '_fail.html')
#     else:
#         os.renames(file_list[i], file_list[i][:-5] + '_pass.html')
# print PASS_FINAL, ERROR_FINAL, FAIL_FINAL
for i in range(0,len(pathDir)):
    excel_result.append(pathDir[i].split('_')[2][0:4])
print excel_result
rb = xlrd.open_workbook("APIcase222.xls")
rs = rb.sheet_by_index(0)
nrows = rs.nrows
print nrows
wb = copy(rb)
ws = wb.get_sheet(0)
for m in range(1,nrows):
    print m
    ws.write(m, 8, excel_result[m-1])
    if m == nrows:
        ws.write(m+1,8,excel_result[m])
wb.save('APIcase222.xls')
# fname = "APIcase222.xlsx"
# bk = xlrd.open_workbook(fname)
# sheet_list = bk.sheets()
# shxrange = range(bk.nsheets)
# print shxrange
# try:
#     sh = bk.sheet_by_name("real")
# except:
#     print "no sheet in %s named real" % fname
# nrows = sh.nrows
# for m in range(1,nrows-1):
#     # print m
#     sh.put_cell(m,8,1,excel_result[m],0)
    # sh.write(m, 8, excel_result[m], set_style('Times New Roman', 220, True))
# file = xlwt.Workbook()
# table = file.add_sheet('sheet name',cell_overwrite_ok=True)
# table.write(1,8,'pass')
# file.save('test20170227.xlsx')
