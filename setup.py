import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
	readme = readme.read()

with open('requirements.txt') as reqs:
	requirements = reqs.read().splitlines()

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
	name='books-list',
	version='0.0.1',
	install_requires=requirements,
	packages=find_packages(),
	include_package_data=True,
	license='MIT License',
	description='TODO',
	long_description=readme,
	url='TODO',
	author='Afroditi Kita, Orestis Ousoultzoglou',
	author_email='TODO, xlxs4@protonmail.ch',
	classifiers=[
		'Intended Audience :: Everyone',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
	],
)
