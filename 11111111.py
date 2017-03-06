# coding=utf-8
import readexcel as r
import time
import os
import xlwt
from datetime import datetime

# style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on', num_format_str='#,##0.00')
# style1 = xlwt.easyxf(num_format_str='D-MMM-YY')
#
# wb = xlwt.Workbook()
# ws = wb.add_sheet('A Test Sheet')
#
# ws.write(0, 0, 1234.56, style0)
# ws.write(1, 0, datetime.now(), style1)
# ws.write(2, 0, 1)
# ws.write(2, 1, 1)
# ws.write(2, 2, xlwt.Formula("A3+B3"))
#
# wb.save('example.xls')

_list = r.readexcel()
# _list = list(tuple(_list))
utf8string = _list[4].encode("utf-8")

# print _list[4][0]
a = ["FAX","FBX","FCX","FDX"]
b = ["CN","US",'AA']
c = ["58018","58019","58020",'58021','58022','58023']
d = "FN"
e = "04214T"
f = []
# print list(itertools.combinations([1,2,3,4,5,6,7,8,9,10],3))
for i in a:
    for m in b:
        for n in c:
            # print i+m+d+n+e
            g = i+m+d+n+e
            f.append(g)
print f
print len(f)
