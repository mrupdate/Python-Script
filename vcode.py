#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/17 16:30
# @Author  : Set3rnal
# @Site    : 
# @File    : vcode.py
# @Software: PyCharm
import base64

from PIL import Image
import pytesseract

image = Image.open('test.png')
vcode = pytesseract.image_to_string(image)
print vcode
print base64.b64decode('UENURntFYTV5X0RvX05ldF9DcjRjazNyfQ==')

