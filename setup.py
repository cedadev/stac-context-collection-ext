# encoding: utf-8
"""

"""
__author__ = 'Richard Smith'
__date__ = '05 Aug 2021'
__copyright__ = 'Copyright 2018 United Kingdom Research and Innovation'
__license__ = 'BSD - see LICENSE file in top-level package directory'
__contact__ = 'richard.d.smith@stfc.ac.uk'

from setuptools import find_namespace_packages, setup

with open("README.md") as readme_file:
    _long_description = readme_file.read()

setup(
    name='stac_fastapi_context_collections',
    description='Extension to the STAC context extension. '
                'Adds the collections applicable for the current'
                'search context for use with filter extension.'
                'Developed for use with the stac-fastapi framework',
    author='Richard Smith',
    url='https://github.com/cedadev/stac-context-collection-ext',
    long_description=_long_description,
    long_description_content_type='text/markdown',
    license='BSD - See LICENSE file for details',
    packages=find_namespace_packages(),
    python_requires='>=3.5',
    install_requires=[
        'attr',
        'fastapi',
        'pydantic',
        'stac-fastapi.types',
    ],
    extras_require={
        'dev': [
            'pre-commit'
        ]
    }
)
