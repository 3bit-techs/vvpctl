#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='vvpctl',
    version='0.1.0',    
    description='Ververica Platform Cli',
    long_description=long_description,
    long_description_content_type="text/markdown",
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
    python_requires='>=3.6',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',  
        'Programming Language :: Python :: 3',
        "Operating System :: OS Independent",
    ],
)