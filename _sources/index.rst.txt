.. kuvat-api documentation master file, created by
   sphinx-quickstart on Mon Jun 29 03:10:56 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Kuvat-api
=====================================

Release v\ |release|.

**Kuvat-api** is a Python library for site `kuvat.fi <https://kuvat.fi>`_.

Installation
------------

To install kuvat-api::

   $ pip install git+https://github.com/Nikotiin/kuvat-api@v0.2

Usage
-----

Example::

   from kuvat_api import Client

   # Initialize client
   client = Client("https://example.kuvat.fi")

   # Get all directories
   directories = client.get_directories()

   # Get list of images
   directory = directories[0]
   images = directory.get_files()

   # Save images
   for image in images:
      image.save("pictures/" + image.name)

Authentication::

   directories = client.get_directories()

   for directory in directories:
      if not directory.authenticated:
         directory.authenticate("password")

.. note::
   Authentication may reveal new directories. You should run :meth:`Client.get_directories`
   again after authentication.


Table of contents
-----------------

.. toctree::
   :maxdepth: 2

   reference
   genindex

