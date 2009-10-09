#!/usr/bin/env python

from distutils.core import setup

setup(name='repoman',
    version='1.0',
    description='RESTful repository management and buildbot for debian packages',
    author='Jeremy Grosser',
    author_email='synack@digg.com',
    scripts=['scripts/repoman'],
    packages=['repoman'],
)