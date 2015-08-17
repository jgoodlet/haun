#!/usr/bin/env python

import re
import ast
from setuptools import setup, find_packages


with open('README.md') as f:
    long_description = f.read()

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('haun/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))


setup(
    name='haun',
    version=version,
    description='Simple CLI for the Email Hunter API.',
    long_description=long_description,
    author='Joshua Goodlett',
    author_email='joshuagoodlett@gmail.com',
    url='https://github.com/jgoodlet/haun',
    license='MIT',
    packages=find_packages(),
    tests_require=['pytest'],
    install_requires=['click'],
    entry_points={
        'console_scripts': [
            'haun=haun.cli:main'
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'
    ]
)