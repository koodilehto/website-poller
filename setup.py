#!/usr/bin/env python
# -*- coding: utf-8 -*-
import websitepoller
from setuptools import setup

description = "Polls specified websites and alerts using system notifications."
try:
    from pypandoc import convert

    long_description = convert('README.md', 'rst')
except (ImportError, IOError, OSError):
    print 'check that you have installed pandoc properly and that ' + \
        'README.md exists!'
    long_description = description

setup(
    name="website-poller",
    version=websitepoller.__version__,
    url='http://koodilehto.github.com/website-poller',
    license='MIT',
    description=description,
    long_description=long_description,
    author=websitepoller.__author__,
    author_email='info@koodilehto.fi',
    packages=['websitepoller', ],
    package_dir={'websitepoller': 'websitepoller', },
    install_requires=['setuptools', ],
    data_files=[('', ['README.md'])],
    entry_points="""
    [console_scripts]
    websitepoller = websitepoller:run
    """,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: System :: Networking :: Monitoring',
    ],
)
