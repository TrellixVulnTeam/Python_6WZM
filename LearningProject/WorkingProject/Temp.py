#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import zipfile, os, shutil, re


# newZip = zipfile.ZipFile('new.zip', 'w')
# newZip.write('zip01.txt', compress_type=zipfile.ZIP_DEFLATED)
# newZip.close()
# # os.unlink(os.path.join(os.getcwd(), 'new.zip'))

# beforeRex = re.compile('fuck', re.VERBOSE)
# folders = os.listdir('D:\\GItHub\\Python\\LearningProject\\WorkingProject\\folder')
# for folder in folders:
#     mo = beforeRex.search(folder)
#     print(folder)

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('width must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2.')


for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        boxPrint(sym, w, h)
    except Exception as err:
        print('An exceptin happend:' + str(err))
