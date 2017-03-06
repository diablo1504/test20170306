# -*- coding: UTF-8 -*-

'''
1、读取指定目录下的所有文件
2、读取指定文件，输出文件内容
3、创建一个文件并保存到指定目录
'''
import os
import urllib2


file_list = []
pathDir = os.listdir("E:\\test_result")
for allDir in pathDir:
    child = os.path.join('%s%s' %("E:\\test_result\\", allDir))
    child = child.replace('\\','/')
    file_list.append(child)
    # print child.decode('gbk')  # .decode('gbk')是解决中文显示乱码问题
# filePathI = "D:\\FileDemo\\Python\\pt.py"
# filePathC = "C:\\"
PASS = 0
ERROR = 0
FAIL = 0
for i in range(0,len(file_list)):
    url = "file:///" + file_list[i]
    print url
    content = urllib2.urlopen(url).read()
    PASS += content.count('pass</a>')
    ERROR += content.count('error</a>')
    FAIL += content.count('fail</a>')
    # for m in content:
    # if "pass</a>" in content:
    #     PASS += 1
    # if "error</a>" in content:
    #     ERROR += 1
    # if "fail</a>" in content:
    #     FAIL += 1
    print PASS, ERROR, FAIL
    # readFile(filePath)
# writeFile(filePathI)