#!/usr/bin/env python
#coding:utf-8

try:
    import readme
    readme.make_bin_symlink()
except ImportError:
    print ("Please first install readme using 'python setup.py install' command")
