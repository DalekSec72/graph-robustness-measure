# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='GraphRobustnessMeasure',
    version='0.1.0',
    description='2020 hyu cse project',
    long_description=readme,
    author='Taehun Kim',
    author_email=':th6424@gmail.com',
    url='https://github.com/DalekSec72/GraphRobustnessMeasure',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)