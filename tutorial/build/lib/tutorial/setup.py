#!/usr/bin/env python
import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
setup(
    name='vduty_django_tutorial',
    version='1.0.0.dev1',
    keywords='django REST python',
    packages=find_packages('tutorial'),
    include_package_data=True,
    #package_dir={'': 'tutorial'},
    description='a django example and django REST API example,contain permission example',
    url='https://github.com/vdutycom/djangoVtutorial',
    author='LUX.YE',
    author_email='97536218@qq.com',
    license='MIT',
 	long_description=README,
    classifiers=[
       'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: X.Y',  # replace "X.Y" as appropriate
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',        
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',  
        ],
   )
