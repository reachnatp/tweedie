#!/usr/bin/env python
from setuptools import setup, find_packages

import versioneer


def read(filename):
    with open(filename, 'r') as f:
        return f.read()


setup(name='tweedie',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      description='Tweedie distribution',
      url='https://github.com/thequackdaddy/tweedie',
      author='',
      author_email='',
      license='BSD',
      keywords='',
      packages=find_packages(),
      # install_requires=install_requires(),
      # extras_require=extras_require(),
      long_description=read('README.rst'),
      zip_safe=False,
      )
