__author__ = "dperealon"
__date__ = "$10-ene-2016 18:35:19$"
__date__ = "$12-ene-2016 12:45:01$"
from setuptools import setup, find_packages

setup (
       name='taller',
       version='0.1',
       packages=find_packages(),

       # Declare your packages' dependencies here, for eg:
       install_requires=['foo>=3'],

       # Fill in these to make your Egg ready for upload to
       # PyPI
       author='dperealon',
       author_email='',

       summary='Just another Python package for the cheese shop',
       url='',
       license='',
       long_description='Long description of the package',

       # could also include long_description, download_url, classifiers, etc.

  
       )
