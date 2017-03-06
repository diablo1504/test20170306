# coding=utf-8
import time
import urllib,urllib2
import json
import util as u


KEY_TIME = "_time"
KEY_AK = "_ak"
PARAMS_SEP = "&"
ACCESS_KEY = "superlvr"
SECRET_KEY = "fa034ce350e72d8a3960ba560150cd62"
# time = time.time()

def testsMain():
    # _list = r.readexcel()
    header = eval(cell_value5)
    model = header["buildID"][:3]
    area = header["buildID"][3:5]
    eui = header["buildID"][7:12]
    data = None
    values = cell_value6
    url = cell_value3
    par = eval(cell_value4)
    my_string = par
    method = cell_value7
    method = method.lower()
    if method == "get":
        if "<" and ">" in url:
            for i in par.keys():
                n_p_k = "<" + str(i) + ">"
                if n_p_k in url:
                    url = url.replace(n_p_k, str(par[i]))
                    par.pop(i)
        elif "{" and "}" in url:
            for i in par.keys():
                n_p_k = "{" + str(i) + "}"
                if n_p_k in url:
                    url = url.replace(n_p_k, str(par[i]))
                    par.pop(i)
        return_items = u.getSignature(ACCESS_KEY, SECRET_KEY, par, time)
        _sign = return_items[0]
        strpar = return_items[1]
        my_string = strpar + "&_sign=" + _sign
        url2 = url + '?' + my_string
        print "url2 as: " + url2
        req = urllib2.Request(url2, data, header)
        res_data = urllib2.urlopen(req)
        apicontent = res_data.read()
        j_a_c = json.loads(apicontent)
        result = json.dumps(j_a_c, indent=4)
        file_object = open('E:\\test_result\\pro.txt', 'w')
        file_object.write(result)
        file_object.close()
        try:
            print "actual result:\n" + result.decode("unicode_escape")
        except:
            pass
    elif method == "post":
        if "<" and ">" in url:
            for i in par.keys():
                n_p_k = "<" + str(i) + ">"
                if n_p_k in url:
                    url = url.replace(n_p_k, str(par[i]))
                    par.pop(i)
        return_items = u.getSignature(ACCESS_KEY, SECRET_KEY, par, time)
        _sign = return_items[0]
        strpar = return_items[1]
        my_string = strpar + "&_sign=" + _sign
        url2 = url + '?' + my_string
        print "url2 as: " + url2
        # #my_string = strpar
        # url2 = url + '?' + my_string
        # print "url2 as: " + url2
        # data = urllib.urlencode(values)
        # req = urllib2.Request(url2,data,header)
        req = urllib2.Request(url, my_string,header)
        res_data = urllib2.urlopen(req)
        apicontent = res_data.read()
        j_a_c = json.loads(apicontent)
        result = json.dumps(j_a_c, indent=4)
        file_object = open('E:\\test_result\\pro.txt', 'w')
        file_object.write(result)
        file_object.close()
        try:
            print "actual result:\n" + result.decode("unicode_escape")
        except:
            pass
    elif method == "put":
        if "<" and ">" in url:
            for i in par.keys():
                n_p_k = "<" + str(i) + ">"
                if n_p_k in url:
                    url = url.replace(n_p_k, str(par[i]))
                    par.pop(i)
        return_items = u.getSignature(ACCESS_KEY, SECRET_KEY, par, time)
        _sign = return_items[0]
        strpar = return_items[1]
        my_string = strpar + "&_sign=" + _sign
        url2 = url + '?' + my_string
        print "url2 as: " + url2
        req = urllib2.Request(url2, data, header)
        req.get_method = lambda: 'PUT'
        res_data = urllib2.urlopen(req)
        apicontent = res_data.read()
        j_a_c = json.loads(apicontent)
        result = json.dumps(j_a_c, indent=4)
        file_object = open('E:\\test_result\\pro.txt', 'w')
        file_object.write(result)
        file_object.close()
        try:
            print "actual result:\n" + result.decode("unicode_escape")
        except:
            pass
    elif method == "delete":
        if "<" and ">" in url:
            for i in par.keys():
                n_p_k = "<" + str(i) + ">"
                if n_p_k in url:
                    url = url.replace(n_p_k, str(par[i]))
                    par.pop(i)
        return_items = u.getSignature(ACCESS_KEY, SECRET_KEY, par, time)
        _sign = return_items[0]
        strpar = return_items[1]
        my_string = strpar + "&_sign=" + _sign
        url2 = url + '?' + my_string
        print "url2 as: " + url2
        req = urllib2.Request(url2, data, header)
        req.get_method = lambda: 'DELETE'
        res_data = urllib2.urlopen(req)
        apicontent = res_data.read()
        j_a_c = json.loads(apicontent)
        result = json.dumps(j_a_c, indent=4)
        file_object = open('E:\\test_result\\pro.txt', 'w')
        file_object.write(result)
        file_object.close()
        try:
            print "actual result:\n" + result.decode("unicode_escape")
        except:
            pass
    else:
        print "\t... hehe ..."
    return result

if __name__ == '__main__':
    testsMain()






