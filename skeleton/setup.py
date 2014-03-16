try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Aliens and Minotaurs',
    'author': 'Badrenkov, Alexander; Kho, Ivan; Lin, Ton; Ng, Yvonne',
    'author_email': 'ivankho@berkeley.edu',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)