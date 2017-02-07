.. shaman documentation master file, created by
   sphinx-quickstart on Thu Feb  2 17:54:32 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. _contents:


Welcome to shaman's documentation!
==================================

Shaman is a python framework for combining and running one after another small
(or not) processors (called "stages"). For instance, you can create a project with a lot of
different functions:
   1) web scraping<br>
   2) clean text extracting<br>
   3) clean text lemmatizing<br>
   4) top words (tfidf) counting<br>
   5) saving the result to a database<br>

There are three parts in the shaman library:<br>
1) stages (actual processors, which do represent some functionality)<br>
2) consumer (worker, that run them all in a particular order)<br>
3) daemon (run as many as needed workers. Also used as a CLI unstrument.)<br>

.. raw:: html

   <a href="https://github.com/Landish145/shaman"><img style="position: absolute; top: 0; right: 0; border: 0;" src="https://camo.githubusercontent.com/38ef81f8aca64bb9a64448d0d70f1308ef5341ab/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f6769746875622f726962626f6e732f666f726b6d655f72696768745f6461726b626c75655f3132313632312e706e67" alt="Fork me on GitHub" data-canonical-src="https://s3.amazonaws.com/github/ribbons/forkme_right_darkblue_121621.png"></a>


Shaman Documentation
--------------------
.. toctree::
   :maxdepth: 1

   intro
   download
   installation/index
   tutorials/index
