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

def get_config_value(section):
    """Reads config file (if exists) to get config value """
    key = 'path'
    config_filename = 'readme_config.ini'
    config = configparser.ConfigParser()
    real_folder = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(real_folder,config_filename)
    if os.path.exists(config_path):
        config.readfp(open(config_path))
        if config.has_option(section, key):
            value = config.get(section, key)
            if value.startswith('~'):
                value = os.path.expanduser(value)
        else:
            value = None
    else:
        value = None

    if value is None:
        raise ValueError("No config found, or no value in config %s" %section)

    return value

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

def make_symlink(fullfilename, output_folder, new_name=None):
    """Makes symlink for readme file in specified folder in config file
    if @new_name specified - symlink will have other name
    """
    if new_name:
        filename = new_name
    else:
        filename = os.path.basename(fullfilename)

    mkdir_p(output_folder)
    symlink_file = os.path.join(output_folder, filename)
    try:
        os.unlink(symlink_file)
        os.symlink(fullfilename, symlink_file)
        print ("Symlink updated %s" % symlink_file)
    except OSError:
        os.symlink(fullfilename, symlink_file)
        print ("Symlink created %s" % symlink_file)


def get_readme_filename(foldername):
    """return readme full name (file_location) """
    FILENAME = 'README_%s.txt'
    filename = FILENAME % foldername
    file_location = os.path.join(os.path.abspath(os.path.curdir), filename)
    return file_location

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

def make_bin_symlink():
    """Copy symlink to current script to BIN folder from config"""
    bin_folder = get_config_value('BIN_FOLDER')
    make_symlink(__file__, bin_folder, new_name='readme')

def run():
    check_platform()
    keywords = get_keywords()
    timestamp = int(time.time())
    files = get_file_list()
    folder_name = get_cur_folder_name()
    filename =  get_readme_filename(folder_name)
    structure = make_structure_for_dumping(filename, timestamp, keywords, files)
    dump_structure(filename, structure)
    symlink_folder = get_config_value("SYMLINK_FOLDER")
    make_symlink(filename, symlink_folder)

