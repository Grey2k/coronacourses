#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name="coronacourses_api",
      version="0.1",
      description="API backend for CoronaCourses",
      url="https://github.com/jjegg01/coronacourses",
      packages=find_packages("coronacourses_api"),
      install_requires=["django>=3.0<4",
                        "djangorestframework>=3.11.0<4",
                        "markdown>=3.2.1<4", # Support for doc
                        "coreapi>=2.3.3<4",
                        "Pygments>=2.6.1<3"
      ]
)
