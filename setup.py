try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'sniffer HD',
    'author': 'Jacques Troussard',
    'url': 'https://github.com/jtroussard/snifferHD',
    'download_url': 'https://github.com/jtroussard/snifferHD/archive/master.zip',
    'author_email': 'jacques.troussard@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['snifferHD'],
    'scripts': [],
    'name': 'HD Hound'
}

setup(**config)
