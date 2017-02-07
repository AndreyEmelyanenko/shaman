Introduction
============

.. warning::

   Please note that this is a beta version of the Shaman library
   which is still undergoing final testing before its official release.
   Should you encounter any bugs, lack of functionality or
   other problems with our library, please let us know immediately.
   Your help in this regard is greatly appreciated.

This is the documentation for the Shaman.
Multiprocessing application to combine different singular handlers
against one message.

The initial purpose was to create a tool, that:
    * would make possible to download and analyze a content of an html pages.
    * simple enough to add a new functionality in it.
    * hast to be scalable (multiprocessing).

Actual usage can be different from it. There are some spontaneous ideas:
    1) scanning a mongo collection and parsing documents in parallel
    2) parsing a lot of lines from multiple huge files, saving the results
to any database (depending on the results)

There are three parts in the shaman library:
    1) stages (actual processors, which do represent some functionality)
    2) consumer (worker, that run them all in a particular order)
    3) daemon (run as many as needed workers. Also used as a CLI unstrument.)

All stages are run in a particular order and use the same message object (inside one worker).