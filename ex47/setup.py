try:
    from setuptools import setup

except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Assignment',
    'author': 'Asgard',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'LPTHW'
}

setup(**config)
