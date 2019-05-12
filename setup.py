import setuptools
from distutils.core import setup
from setuptools import setup, find_packages

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'TrackTor',
  packages = ['TrackTor', 'TrackTor.Home', 'TrackTor.Icons', 'TrackTor.Logs_Data', 'TrackTor.Utilities'],
  version = '1.0',
  license='GNU General Public License v3 or later (GPLv3+)',
  description = 'A Monitoring Tool for TOR Network',
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'Dr. Pilli Emmanuel Shubhakar, Harsh Gandhi, Ritu Karela, Parul Agrawal',
  author_email = 'espilli.cse@mnit.ac.in, hrgandhi1@gmail.com, ritukarela1234@gmail.com, parulagrawal1507@gmail.com',
  url = 'https://github.com/iamhrg/TrackTor',
  include_package_data = True,
  keywords = ['TrackTor', 'Tor', 'Deep Web', 'Dark Web', 'Tor Project', 'Security', 'Tracking', 'Monitoring', 'Analysing','Nyx', 'Stem', 'User Friendly', 'UI'],
   entry_points={
        'console_scripts': ['TrackTor = TrackTor.__init__:TrackTor_Main']
    },
  install_requires=[
          'stem',
          'argparse',
          'numpy',
          'pycountry',
          'psutil',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',

    'Intended Audience :: Developers',
    'Intended Audience :: Education',
    'Intended Audience :: Science/Research',
    'Intended Audience :: Other Audience',
    'Topic :: Software Development :: Build Tools',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Education',
    'Topic :: Scientific/Engineering',
    'Topic :: Security',

    'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',

    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)
