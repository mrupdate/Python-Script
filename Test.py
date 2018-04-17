# -*- coding: utf-8 -*-
# @Time    : 2017/5/12 22:08
# @Author  : set3rnal
# @Site    : 
# @File    : Test.py
# @Software: PyCharm
# 扩展欧几里得算法求二元一次方程

# import json
#
# data = [{'a': 1, 'b': 2, 'c': 3}]
# json = json.dum

try:
    fp = open('F://pic/WAV/ES.png', 'wb')
    print 'Ok!'
    fp.close()
except Exception,e:
    print 'No such file'

# code = str[::-2]
# result = ''
# for i in code:
#     ss = ord(i) - 1
#     result += chr(ss)
#
# print result[::-2]

# def ext_euclid(a, b):
#     if (b == 0):
#         return 1, 0, a
#     else:
#         x, y, q = ext_euclid(b, a % b)
#         x, y = y, (x - (a // b) * y)
#         return x, y, q
#
#
# if __name__ == '__main__':
#     print ext_euclid(1749, 0)
