# -*- coding: utf-8 -*-
# @Time    : 2017/5/12 22:08
# @Author  : set3rnal
# @Site    :
# @File    : Test.py
# @Software: PyCharm

a = """
ABCDEFG
ABCDEFG
ABCDEFG
ABCDEFG
"""

b = "BCAG"
c = "2,3,1,4"
a = a.splitlines()
a.pop(0)
s = ''
t = []

c = c.split(',')
for i in range(0, len(c)):
    index = a[int(c[i]) - 1].index(b[i])
    print
    tt = a[int(c[i]) - 1][index:] + a[int(c[i]) - 1][:index]  # 从index开始，在index结束
    print tt
    t.append(tt)

# for y in range(len(t[0])):
#     for x in range(0, len(t)):
#         s += t[x][y]
#
#     print '第' + str(y) + '列', ''.join(s)
#
#     s = ''
