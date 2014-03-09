try:
	from setuptools import setup
except ImportError:
	from distutils.cor import setup

config = {
	'description': 'My Project',
        'author': 'Ivan Kho',
        'url': 'URL to get it at.',
        'download_url': 'Where to download it.',
        'author_email': 'ivankho@berkeley.edi',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['NAME'],
        'scripts': [],
        'name': 'projectname'
}

setup(**config)
