#!/usr/bin/env python
import os
from setuptools import setup

setupconf = dict(
    name = 'readme_script',
    version = '0.0.1',
    url = 'https://github.com/pymen/readmehorton',
    author = 'Anton Sedov',
    author_email = 'sedovanton@gmail.com',
    description = 'Generation of reame files with content of current and sub folders',
    keywords = 'generation readme',
    packages = ['readme_script'],
    package_data = {'': ['*.ini', '*.MD']},
    data_files=[("/usr/local/bin", ["readme"])],
    classifiers = [
        'Intended Audience :: Developers',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        ],
    )

if __name__ == '__main__':
    setup(**setupconf)
    copied_file = os.path.join("/usr/local/bin","readme")
    os.system('sudo bash update_chmod.sh')

