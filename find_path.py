# 将目录中的所有文件加入列表，从列表中通过正则表达式匹配 barcode 找出绝对路径。
import logging
import csv
import os
import glob
import re

results = list()

paths = []
t = ''

location = '/opt/home/lanchunyuan/fujian/2018/'
for parent,dirnames,filenames in os.walk(location):
    for filename in filenames:
        paths.append(os.path.join(parent,filename))
for path in paths:
#   print(path)
    p_barcode_path = re.compile(r'.*\/R3502037800002016120020\/3\.bmp')
    try:
        tmp = p_barcode_path.search(path)
        t = tmp.group()
        print(t)
    except BaseException as e:
#       logging.exception(e)
#       print(e)
        pass
print(t)
#p_paths = {}
#a_paths = {}
#
#with open('lt_fujian_results.csv') as f_obj:
#   for line in f_obj:
#       line=line.strip('\n')
#       results.append(line.split(','))
#
#for result in results:
##  print(result)
#   p_barcode = result[0]
#   p_finger = result[1]
#   c_barcode = result[2]
#   c_finger = result[3]
#   p_paths[f'{p_barcode}-{p_finger}'] = \
#   glob.glob(f'{location}/**/{p_barcode}',recursive=True)
#   print(p_paths)