try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'First knowledge about Single Linked Lists',
    'author': 'Elena',
    'version': '0.2',
    'name': 'Single_Linked_Lists_Project'
}

setup(**config)