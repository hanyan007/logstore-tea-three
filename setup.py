#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : setup.py.py
# @Author: hanyan_news
# @Desc  :


from distutils.core import setup
from setuptools import find_packages

with open("README.rst", "r") as f:
  long_description = f.read()


setup(name='logstore-tea-three',  # 包名
      version='1.0.0',  # 版本号
      description='a small package just example for logstores',
      long_description=long_description,
      author='hanyan_news',
      author_email='hanyan0572@gmail.com',
      url='https://github.com/hanyan007/logstore-tea-three.git',
      install_requires=["package-tea-hanyan==1.0.3", "restful-dnspod-log==1.0.1", "dnspod-domain-log==1.0.4", "logstore-tea-one==1.0.0", "logstore-tea-two==1.0.0", "logstore-tea-four==1.0.0", "package-tea-nine==1.0.0", "package-tea-eight==1.0.0", "package-tea-one==1.0.0", "package-tea-seven==1.0.0"],
      project_urls={  # Optional
        "Source": 'https://github.com/hanyan007/logstore-tea-three.git',
      },
      license='BSD License',
      packages=find_packages(),
      platforms=["all"],
      classifiers=[
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Natural Language :: Chinese (Simplified)',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Topic :: Software Development :: Libraries'
      ],
      )
