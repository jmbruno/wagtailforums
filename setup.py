#!/usr/bin/env python

import sys

from wagtailforums import __version__

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


# Hack to prevent stupid TypeError: 'NoneType' object is not callable error on
# exit of python setup.py test # in multiprocessing/util.py _exit_function when
# running python setup.py test (see
# http://www.eby-sarna.com/pipermail/peak/2010-May/003357.html)
try:
    import multiprocessing
except ImportError:
    pass


setup(
    name='wagtailforums',
    version=__version__,
    description='A simple forum system for Wagtail CMS',
    author='Karl Hobley', 'Jean Marc BRUNO',
    author_email='karlhobley10@gmail.com',
    url='https://github.com/jmbruno/wagtailforums',
    packages=['wagtailforums'],
    include_package_data=True,
    license='BSD',
    long_description=open('README.md').read(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Framework :: Django',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ],
    install_requires=[
        'Django>=3.0',
        'wagtail>=2.9,
    ],
    zip_safe=False,
)
