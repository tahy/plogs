from setuptools import setup, find_packages
from os.path import join, dirname

setup(name='LogAnalyser',
	install_requires=[
		'pytest'
	],
	version='1.0',
	packages=find_packages(),
	long_description=open(join(dirname(__file__), 'README.TXT')).read(),
 )
