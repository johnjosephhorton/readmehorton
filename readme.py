#!/usr/bin/env python
#coding:utf-8
# Author: Anton Sedov
# Purpose: Odesk Task
# Created: 14.06.2013

import sys
import os
import unittest
import argparse

try:
    #python 2.x
    import ConfigParser as configparser
except ImportError:
    #python 3.x
    import configparser

import yaml
import time
import datetime
import glob
from collections import OrderedDict

FILENAME = 'README_%s.txt'


def main():
    location = ''
    timestamp = int(time.time())
    keywords = ''
    files = ''

    folder_name = 'this_folder_name'
    file_name = FILENAME % folder_name

    dump_structure = OrderedDict()
    dump_structure['location'] = location
    dump_structure['timestamp'] = timestamp
    dump_structure['keywords'] = keywords
    dump_structure['files'] = files

    stream = file(file_name, 'wb')
    yaml.dump(dump_structure, stream)
    print ("Succesfully prepared readme file: %s" % file_name)


if __name__=='__main__':
    #unittest.main()
    main()