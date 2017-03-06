# coding=utf-8
import unittest
import time
import HTMLTestRunner
import json
import result as ret
import xlrd

class TestDictValueFormatFunctions(unittest.TestCase):
    def setUp(self):
        file_object = open('E:\\test_result\\pro.txt', 'rb')
        list_of_all_the_lines = file_object.read()
        ccc = json.loads(list_of_all_the_lines)
        ddd = json.dumps(ccc, indent=4)
        eee = eval(ddd)
        fff = []
        ggg = []
        ggg.append(eee)
        fff.append(eee["data"])
        self.results_first = ggg
        self.results = fff

    def test_format(self):
        self.assertTrue(isinstance(self.results, list),
                        "self.results's type must be dict but got {0}".format(type(self.results)))
        for r in self.results:
            for f in results_fields_map:
                value = r.get(f, None)
                self.assertTrue(isinstance(value,results_fields_map[f]),
                                u"{0}'s type must be {1} but got {2}".format(value,results_fields_map[f], type(value)))
                # self.assertTrue(isinstance(value, results_fields_map[f]))

    def test_value(self):
        for i in self.results_first:
            self.assertEqual(i["errno"], 10000)
        for r in self.results:
            self.assertEqual(r["versionCode"], "16113002")
            self.assertEqual(r["sysVersionCode"], "16061320")

    # def tearDown(self):


if __name__ == '__main__':
    print "+++++++++++++++++++++++++"
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
            cell_value1 = sh.cell_value(i, 1)
            print "++++++++++++++++++++++"
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

        except:
            pass
        try:
            output = open(result_dir + '\\%s.txt' % cell_value2, 'w')
            output.write(ret.testsMain())
        except Exception, e:
            output = open(result_dir + '\\%s.txt' % cell_value2, 'w')
            output.write(str(e))
    output.close()
    utf8string = cell_value6.encode("utf-8")
    utf8string_change = eval(utf8string)
    results_fields = utf8string_change
    results_fields_map = dict(results_fields)
    ret.testsMain()
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestDictValueFormatFunctions)
    suite = unittest.TestSuite(suite2)
    # 获取当前时间，这样便于下面的使用。
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    # 打开一个文件，将result写入此file中
    fp = open("E:\\test_result\\result" + now + ".html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='test result', description=u'result:')
    runner.run(suite)
    fp.close()



