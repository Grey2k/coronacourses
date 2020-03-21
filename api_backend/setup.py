#!/usr/bin/env python

from setuptools import setup, find_packages


packages = list(filter(lambda x: x.startswith(
    "coronacourses_api"), find_packages()))


setup(name="coronacourses_api",
      version="0.1",
      description="API backend for CoronaCourses",
      url="https://github.com/jjegg01/coronacourses",
      packages=packages,
      install_requires=["django>=3.0<4",
                        "djangorestframework>=3.11.0<4",
                        "markdown>=3.2.1<4", # Support for doc
                        "coreapi>=2.3.3<4",
                        "Pygments>=2.6.1<3",
                        "channels>=2.4.0<3",
                        "PyYAML>=5.3.1<6",
                        "channels_redis>=2.4.2<3",
                        "django-oauth-toolkit>=1.3.0<2"
      ]
)
