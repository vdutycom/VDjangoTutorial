#/usr/bin/env python
import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
setup(
    name='VDjangoTutorial',
    version='1.0.0.dev1',
    keywords='django REST python',
    #packages=find_packages(),
    #packages=['tutorial','snippets','snippets.myviews'],
    packages=find_packages('tutorial'),
    include_package_data=True,
    package_dir={'': 'tutorial'},
    description='a django example and django REST API example,contain permission example',
    url='https://github.com/vdutycom/djangoVtutorial',
    author='LUX.YE',
    author_email='97536218@qq.com',
    license='MIT',
 	long_description=README,
    install_requires=[
		'asgiref==3.2.3',
		'Django==3.0',
		'djangorestframework==3.10.3',
		'djangorestframework-jwt==1.11.0',
		'mysql-connector==2.2.9',
		'mysqlclient==1.4.6',
		'Pygments==2.5.2',
		'PyJWT==1.7.1',
		'PyMySQL==0.9.3',
		'pytz==2019.3',
		'sqlparse==0.3.0',
		'uWSGI==2.0.18',   ],
    scripts=[
        'tutorial/manage.py',
        'tutorial/tutorial/wsgi.py',
    ],
    entry_points={
        'console_scripts': [
            'tutorial_manage = manage:main',
        ]
    },
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
