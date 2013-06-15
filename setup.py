#!/usr/bin/env python

from setuptools import setup
import os.path

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setupconf = dict(
    name = 'readme',
    version = '0.0.1',
    url = 'https://github.com/pymen/readmehorton',
    author = 'Anton Sedov',
    author_email = 'sedovanton@gmail.com',
    description = 'Generation of reame files with content of current and sub folders',
    keywords = 'generation readme',
    packages = ['readme'],
    package_data = {'': ['*.ini', '*.MD']},
    data_files=[("/usr/local/bin", "readme/readme")],
    classifiers = [
        'Intended Audience :: Developers',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        ],
    )

if __name__ == '__main__':
    setup(**setupconf)

