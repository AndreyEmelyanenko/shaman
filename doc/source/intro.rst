Introduction
============

.. warning::

   Please note that this is a beta version of the Shaman library
   which is still undergoing final testing before its official release.
   Should you encounter any bugs, lack of functionality or
   other problems with our library, please let us know immediately.
   Your help in this regard is greatly appreciated.

This is the documentation for the Shaman.
Multiprocessing application to download and analyze a content of an html pages.

As en example scenario, consider the following:
reading url from a kafka topic or stdin, running it through a set of processors (called "stages": extracting title, meta, etc) and
writing results to a mongo db or kafka output topic.