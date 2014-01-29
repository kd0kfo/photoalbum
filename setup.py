#!/usr/bin/env python

from setuptools import setup

setup(name='photoablum',
      version='1.0.b',
      description='Photo Album Generator',
      author='David Coss, PhD',
      author_email='david@davecoss.com',
      license='GPL v3',
      packages=['photoalbum'],
      scripts=["scripts/generate_webpage", "scripts/generate_index"],
      )
