from setuptools import setup, find_packages

import sys
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

if sys.version_info.major != 3:
    print('This Package is only compatible with Python 3, but you are running '
          'Python {}. The installation will likelyfail.'.format(sys.version_info.major))
          


setup(name='yamdai',
      version='0.1.1',
      description='Creates anki decks from markdown',
      author='M. Fatih Bostanci',
      author_email='fatih.bostanci@hotmail.de',
      license='MIT',
      packages= find_packages(),
      install_requires=[
        'genanki',
        'setuptools',
        'misaka',
        'pygments'
        ],
      entry_points={
        "console_scripts": [
            "yamdai=yamdai.yamdai:main"
        ]
      },
      package_data = {'yamdai': ['code_highlight.css']},
      zip_safe=False)