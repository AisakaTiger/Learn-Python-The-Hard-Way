try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Komeiji Sai',
    'url': 'https://github.com/AisakaTiger/Learn-Python-The-Hard-Way',
    'download_url': 'https://github.com/AisakaTiger/Learn-Python-The-Hard-Way',
    'author_email': 'fujibarasai@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
