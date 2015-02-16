#!/usr/bin/env python
# -*- coding : utf-8 -*-
from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Captchasec',
    version='0.0.1',
    description='Captcha difficulty tester',
    long_description=long_description,
    url='https://github.com/mmetince/captchasec',
    author='Mehmet Ince',
    author_email='mehmet@mehmetince.net',
    license='MIT',
    keywords='captcha security cracker',
    packages=['captchasec'],
    entry_points={
        'console_scripts': [
            'captchasec = captchasec:main'
        ],
    },
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Penetration Testers/Web Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Security :: Web',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
)