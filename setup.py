#!/usr/bin/env python

"""Setup script for Commune."""

from src.commune import __project__, __version__

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
  long_description = f.read()

setup(
  name=__project__,
  version=__version__,
  description='A system to simulate communal interaction in video games.',
  long_description=long_description,
  long_description_content_type='text/markdown',
  url='https://github.com/oAGoulart/commune',
  author='Augusto Goulart',
  author_email='josegoulart.aluno@unipampa.edu.br',
  classifiers=[
    'Development Status :: 1 - Planning',
    'Intended Audience :: Developers',
    'Topic :: Games/Entertainment',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
  ],
  keywords='game commune simulate',
  package_dir={'': 'src'},
  packages=find_packages(where='src'),
  python_requires='>=3.8',
  #install_requires=[''],
  project_urls={
    'Bug Reports': 'https://github.com/oAGoulart/commune/issues',
    'Source': 'https://github.com/oAGoulart/commune',
  },
)
