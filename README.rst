..  -*- coding: utf-8 -*-

=============
oecdjson task
=============

version: 0.1.0

oecdjson task collects OECD statistics in JSON format.


Installation
------------

To install oecdjson task, run the following pyloco command. ::

    >>> pyloco install oecdjson
    >>> pyloco oecdjson --version
    oecdjson 0.1.0

If pyloco is not available on your computer, please run the following
command to install pyloco, and try again above task installation. ::

    >>> pip install pyloco --user
    >>> pyloco --version
    pyloco 0.0.109

.. note::

    - 'pip' is a Python package manager.
    - Remove '--user' option to run pyloco on a virtual environment.
    - Add '-U' option to 'pip' command to upgrade pyloco.
    - We recommend to use pyloco version 0.0.109 or higher.

Command-line syntax
-------------------

usage: pyloco oecdjson [-h] [-d dataset] [-f filter] [-a agency]
                          [-p params] [-o outfile] [--general-arguments]
                          

optional arguments:
  -h, --help            show this help message and exit
  -d dataset, --dataset dataset
                        Dataset code (default='QNA')
  -f filter, --filter filter
                        Query
                        filter(default='USA+KOR+CHN.GDP+B1_GE.CUR+VOBARSA.Q')
  -a agency, --agency agency
                        Agency code. (default='all')
  -p params, --params params
                        Additional parameters
  -o outfile, --outfile outfile
                        Save OECD data in a file
  --general-arguments   Task-common arguments. Use --verbose to see a list of
                        general arguments

forward output variables:
   data                 OECD stats in JSON format

 
Example(s)
----------

Following command collect OECD stats of dataset='QNA',
filter='USA+KOR+CHN.GDP+B1_GE.CUR+VOBARSA.Q',
agency='all', and save the collected data to 'oecd.json'.

>>> pyloco oecejson -o oecd.json

