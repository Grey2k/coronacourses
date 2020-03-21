#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name="coronacourses_api",
      version="0.1",
      description="API backend for CoronaCourses",
      url="https://github.com/jjegg01/coronacourses",
      packages=find_packages("coronacourses_api"),
      install_requires=["django>=3.0<4"]
)
