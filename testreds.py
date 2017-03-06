# coding=utf-8
import redis
# import string
# import sys
# import os
import string

letter = string.digits
list_result = []
result_str = []
result_final = ""
model_default = "LEVR_share_ota_zset_pro_policy_model_"
group_default = "LEVR_share_ota_zset_pro_policy_group_"
eui_default ="LEVR_share_ota_zset_pro_policy_eui_"
model = "FCX"
eui = "58518"
group = "18"
eui_final = eui_default + eui
model_final = model_default + model
group_final = group_default + group

f = open("1.txt", "r")
lines = f.readlines()
config = []
for line in lines:
    line = line.strip('\n')
    config.append(line.split('=')[1])
f.close()
# pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
# pool = redis.ConnectionPool(host='%s'%(conf ig[0]), port='%d'%(int(config[1])))
pool = redis.ConnectionPool(host=config[0], port=int(config[1]))
r = redis.Redis(connection_pool=pool)
list_result = r.keys("*ota*")
# print list_result
if eui_final in list_result:
    result_str.append(eui_final)
if model_final in list_result:
    result_str.append(model_final)
if group_final in list_result:
    result_str.append(group_final)
print result_str
# result_str_change = ','.join(result_str)
# for m in result_str:
#     result_final += m
# print result_final
# print int(r.zrange('LEVR_share_ota_zset_pro_policy_model_FCX',0,-1,False,True)[1][1])
r.zinterstore("test",result_str,aggregate="MAX")
a = r.zrange("test",0,-1,False,True)
print a
list1 = []
for i in range (0,len(a)):
    list1.append(int(a[i][1]))
print max(list1)