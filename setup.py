### -*- coding: utf-8 -*-
###
### © 2012 Krux Digital, Inc.
### Author: Paul Lathrop <paul@krux.com>
###

from setuptools import setup, find_packages

setup(name='pysecurity-groups',
      version="1.0.0",
      description='Library for working with EC2 security groups in bulk.',
      author='Paul Lathrop',
      author_email='paul@krux.com',
      url='https://github.com/krux/pysecurity-groups',
      packages=find_packages(),
      install_requires=['boto', 'argparse', 'IPy'],
      entry_points={'console_scripts':
                    ['security-groups = pysecurity_groups.cli:main'] },
      )
