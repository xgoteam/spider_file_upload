#!/usr/bin/env python
# coding: utf-8
from setuptools import (
    find_packages,
    setup,
)

setup(
    name='oss_bucket_methods',  # 模块名称
    version='1.0',
    description='Oss云存储 上传方法',  # 描述
    packages=find_packages(),
    author='guo_jd',
    url='#',
    install_requires=['oss2','pymongo'],
)
