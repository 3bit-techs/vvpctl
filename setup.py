#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import setuptools

setuptools.setup(
    name='vvpctl',
    version='0.1.0',    
    description='Ververica Platform Cli',
    url='https://github.com/3bit-techs/vvpctl',
    author='Eduardo Goncalves',
    author_email='dudssource@gmail.com',
    packages=setuptools.find_packages(),
    scripts=['vvpctl'],
    install_requires=[
        'requests==2.25.0',
        'DeepDiff==5.0.2',
        'argparse==1.4.0'
    ],

    classifiers=[
        'License :: OSI Approved :: Apache Software License',  
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.7',
    ],
)