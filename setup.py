# coding=utf-8
# @Author: jlumbroso
# @Date:   2018-03-29-18:45
# @Email:  lumbroso@cs.princeton.edu
# @Filename: setup.py
# @Last modified by:   jlumbroso
# @Last modified time: 2018-03-29-19:00

from setuptools import setup, find_packages

setup(
	name = "reluctant_walks",
	packages = find_packages(),
	version = "1.0",
	description = ("Python/Sage package to study and sample reluctant "
                   "random walks in the positive quadrant."),
	author = "Jérémie Lumbroso",
	author_email = "lumbroso@cs.princeton.edu",
	url = "https://github.com/jlumbroso/reluctant_walks",
	keywords = ['combinatorics', 'random walks', 'sampling'],
	license = 'LGPLv3',
	classifiers = [
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
        'Topic :: Scientific/Engineering :: Mathematics',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
		'Operating System :: OS Independent',
		'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Development Status :: 5 - Production/Stable'
		],
)
