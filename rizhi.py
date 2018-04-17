#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/3 11:58
# @Author  : Set3rnal
# @Site    : 
# @File    : rizhi.py
# @Software: PyCharm

import urllib
import re

sql_pattern = re.compile(r"\[(.*?)\].*GET /backend.php?user=admin' (.*?) HTTP/1.1")
comment_pattern = re.compile(r"/\*.*?\*/")
with open("sqlmap.txt") as f:
    log_data = f.read()
    log_data = urllib.unquote(log_data)
log_data = comment_pattern.sub('', log_data)
log_data = sql_pattern.findall(log_data)
data = []
for line in log_data:
    if 'flag' in line[1]:
        data.append(line)
tmp = ''
flag = ''
for index, f_line in enumerate(data):
    try:
        s_line = data[index + 1]
        if f_line[0] == s_line[0]:
            tmp += '0'
        else:
            tmp += '1'
        if (index + 1) % 7 == 0:
            tmp += '0'
            tmp = tmp[::-1]
            print tmp
            flag += chr(int(tmp, 2))
            tmp = ''
    except IndexError:
        break
print flag
