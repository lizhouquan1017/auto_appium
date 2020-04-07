# -*- coding:utf-8 -*-
__author__ = "lizhouquan"

import os
import zipfile
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

def zipping_file(startdir, targetdir):
    fp = zipfile.ZipFile(targetdir, 'w', zipfile.ZIP_DEFLATED)
    for dirpath, dirnames, filenames in os.walk(startdir):
        for filename in filenames:
            fp.write(os.path.join(dirpath, filename))
    fp.close()


def remove_file(root_dir):
    file_list = os.listdir(root_dir)
    for fp in file_list:
        file_path = os.path.join(root_dir, fp)
        os.remove(file_path)


if __name__ == '__main__':
    remove_file(rootPath+'/appium_log')