# coding=utf-8
import time
import xlrd
import os

def readexcel():
    new_list = []
    fname = "APIcase222.xlsx"
    bk = xlrd.open_workbook(fname)
    sheet_list = bk.sheets()
    shxrange = range(bk.nsheets)
    try:
        sh = bk.sheet_by_name("real")
    except:
        print "no sheet in %s named Sheet1" % fname
    # 获取行数
    nrows = sh.nrows
    # 获取列数
    ncols = sh.ncols
    # print "nrows %d, ncols %d" % (nrows, ncols)
    # 获取数据
    t_now = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
    for i in range(1, 3):  # 目标起始行所在的前一行到目标结尾行
        try:
            cell_value0 = sh.row_values(i)
            cell_value1 = sh.cell_value(i, 1)
            cell_value2 = sh.cell_value(i, 6)
            cell_value3 = sh.cell_value(i, 2)
            cell_value4 = sh.cell_value(i, 3)
            cell_value5 = sh.cell_value(i, 4)
            cell_value6 = sh.cell_value(i, 5)
            cell_value7 = sh.cell_value(i, 7)
            # filename = cell_value1+cell_value2
            # print filename
            result_dir = 'C:\\Users\\wujingjian\\Desktop\\result\\%s\\%s' % (t_now, cell_value1)
            os.makedirs(result_dir)
            print cell_value0
        except:
            pass
        try:
            output = open(result_dir + '\\%s.txt' % cell_value2, 'w')
            output.write(testsMain())
        except Exception, e:
            output = open(result_dir + '\\%s.txt' % cell_value2, 'w')
            output.write(str(e))
    output.close()
    utf8string = cell_value6.encode("utf-8")
    utf8string_change = eval(utf8string)
    results_fields = utf8string_change
    results_fields_map = dict(results_fields)
    return cell_value1,cell_value2,cell_value3,cell_value4,cell_value5,utf8string_change,cell_value7,results_fields_map
if __name__ == '__main__':
    readexcel()


