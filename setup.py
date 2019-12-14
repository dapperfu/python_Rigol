# -*- coding: utf-8 -*-
from setuptools import setup

setup(name='rigol',
      version='0.1',
      description='High level python module for controlling Rigol devices.',
      url='https://github.com/jed-frey/python_Rigol',
      author='Jed Frey',
      license='MIT',
      packages=['rigol'],
      setup_requires=[
      ],
      tests_require=[
          'pytest',
          'pytest-html',
      ],
      zip_safe=False,
      )
