# coding=utf-8
import md5
import urllib,urllib2
import time

KEY_TIME = "_time"
KEY_AK = "_ak"
PARAMS_SEP = "&"
ACCESS_KEY = "superlvr"
SECRET_KEY = "fa034ce350e72d8a3960ba560150cd62"
timestamp = time.time()

def getSignature(accessKey, secretKey, params, time):
    sin = []
    sin.append(KEY_TIME + "=" + str(int(timestamp))) # May...
    sin.append(KEY_AK + "=" + accessKey)
    if params != None:
        for kk in params:
            params_fm = kk + "=" + urllib.quote(str(params[kk]))
            sin.append(params_fm)
    sin.sort()
    paramstring = joinSep(sin, PARAMS_SEP)
    print "paramstring as: " + paramstring
    strSign = paramstring + secretKey
    print "strSign as: " + strSign
    md = md5.new()
    md.update(strSign)
    strSignature = md.hexdigest()
    #print "strSignature as: " + strSignature
    return strSignature, paramstring

def joinSep(arr_str, sep):
    new_str = ""
    first = True
    for s in arr_str:
        if first:
            first = False
        else:
            new_str = new_str + sep
        new_str = new_str + s
    return new_str


