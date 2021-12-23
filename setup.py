#!/usr/bin/env python

from setuptools import setup

setup(name='photoalbum',
      version='1.1',
      description='Photo Album Generator',
      author='David Coss, PhD',
      author_email='david@davecoss.com',
      license='GPL v3',
      packages=['photoalbum'],
      scripts=["scripts/generate_webpage", "scripts/generate_index"],
      )
