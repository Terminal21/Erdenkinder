import os

from setuptools import find_packages
from setuptools import setup

version = '0.1'
project = 'erdenkinder'

install_requires=[
        'Kotti',
    ],

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

setup(name=project,
      version=version,
      description="AddOn for Kotti",
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "License :: Repoze Public License",
        ],
      keywords='kotti addon',
      author='Stefan@Terminal.21',
      author_email='stefan@terminal21.de',
      url='http://pypi.python.org/pypi/',
      license='bsd',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      tests_require=[],
      entry_points={
        'fanstatic.libraries': [
          'erdenkinder = erdenkinder.fanstatic:library',
        ],
      },
      )
