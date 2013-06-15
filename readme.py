#!/usr/bin/env python
#coding:utf-8
# Author: Anton Sedov
# Purpose: Odesk Task
# Created: 14.06.2013

import sys
import os

try:
    import ConfigParser as configparser #python 2.x
except ImportError:
    import configparser #python 3.x

import yaml
import time
import datetime
import fnmatch
import errno
from collections import OrderedDict

def check_platform():
    """Checks that it is not windows platform"""
    if sys.platform.startswith('win'):
        raise WindowsError("This script can be run only on Unix systems")

def mkdir_p(path):
    """ Mkdir if not exists """
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST:
            pass
        else: raise

def get_symlink_folder():
    """Reads config file (if exists) to get config value of symlink_folder"""
    section, key = "SYMLINK_FOLDER", 'path'
    config = configparser.ConfigParser()
    if os.path.exists('readme_config.ini'):
        config.readfp(open('readme_config.ini'))
        if config.has_option(section, key):
            symlink_folder = config.get(section, key)
        else:
            symlink_folder = None
    else:
        symlink_folder = None
    return symlink_folder

def get_keywords():
    """Gets command line args, using sys argv instead of argparse"""
    keywords = ",".join(sys.argv[1:])
    if not keywords:
        raise ValueError("No Keywords was supplied")
    return keywords

def find_files(directory, pattern):
    """Find all file in this folder and sub-folders"""
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                yield filename

def get_cur_folder_name():
    """return  cur folder name"""
    return  os.path.split(os.path.abspath(os.path.curdir))[1]

def get_file_list():
    """return generator list of file"""
    return [filename for filename in find_files('.', '*')]

def make_symlink(source):
    """Makes symlink for readme file in specified folder in config file"""
    symlink_folder = get_symlink_folder()
    mkdir_p(symlink_folder)
    if symlink_folder:
        os.symlink(source, symlink_folder)
    else:
        print "No config found, or no value in config"

def get_readme_filenames(foldername):
    """return readme short name (filename) and full name (file_location) """
    FILENAME = 'README_%s.txt'
    filename = FILENAME % foldername
    file_location = os.path.join(os.path.abspath(os.path.curdir), filename)
    return filename, file_location

def make_structure_for_dumping(location, timestamp, keywords, files):
    """Prepares dump structure"""
    #dump_structure = OrderedDict()
    dump_structure = {}
    dump_structure['Location'] = location
    dump_structure['Timestamp'] = timestamp
    dump_structure['Keywords'] = keywords
    dump_structure['files'] = files
    return dump_structure

def dump_structure(file_name, dump_structure):
    with open(file_name, 'w') as stream:
        yaml.dump(dump_structure, stream, default_flow_style=False ,  line_break=None)
        print ("Succesfully prepared readme file: %s" % (file_name, ))

def main():
    check_platform()
    keywords = get_keywords()
    timestamp = int(time.time())
    files = get_file_list()
    folder_name = get_cur_folder_name()
    filename, location =  get_readme_filenames(folder_name)
    structure = make_structure_for_dumping(location, timestamp, keywords, files)
    dump_structure(filename, structure)
    make_symlink(filename)

if __name__=='__main__':
    main()