#!/usr/bin/env python
from setuptools import setup

setup(
    name='vduty_django_tutorial',
    version='1.0.0.dev1',
    description='a django example and django REST API example,contain permission example',
    url='https://github.com/vdutycom/djangoVtutorial',
    author='LUX.YE',
    author_email='97536218@qq.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='django REST python',
    packages=find_packages(),
    include_package_data=True,
)
