#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/5 15:55
# @Author  : Set3rnal
# @Site    : 
# @File    : DownloadPic.py
# @Software: PyCharm


import requests
import re

head = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36'}
for x in xrange(1314,1320):
    url="https://www.unodc.org/cld/case-law-doc/traffickingpersonscrimetype/usa/case_"+str(x)+".html?lng=en&tmpl=htms"
    print "Now testing"+url
    rec = requests.get(url, headers=head)
    if rec.status_code == requests.codes.ok:
        print url
        html = rec.text
        # print text
        text = re.findall('<div class="factSummary">([\s\S]*)<div class="clear"></div></div></div><div class="col-md-6 col-lg-6 col-xs-12 case-law-detail">', html)
        
        print text
        # fp = open('aaa.txt', 'wb')
        # fp.write(text[0].encode('utf-8'))
