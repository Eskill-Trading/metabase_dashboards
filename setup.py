# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in metabase_dashboards/__init__.py
from metabase_dashboards import __version__ as version

setup(
	name='metabase_dashboards',
	version=version,
	description='All dashboards from metabase.',
	author='Eskill Trading',
	author_email='eskilladmin@eskilltrading.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
