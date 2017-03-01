Installation for Linux and Mac OS-X users
=========================================


shaman is known to work well on

* Ubuntu 16.04.1
* Ubuntu 14.04.1
* MacOS

To install shaman you should clone it from a repo: https://github.com/Landish145/shaman

Script to install shaman on Ubuntu
-----------------------------------

The following script is tested with Ubuntu 14.04.
Scroll further below for more OS-specific insructinos.

.. code-block:: bash

    # Step 0. Prerequisites
    You might wanna need to run these commands:
    -  (python2.7) sudo pip install -U setuptools pip
    - (python3.4) sudo pip3 install -U setuptools pip
    - sudo apt-get install libcurl4-openssl-dev
    # Step 1. using pip:
    sudo pip install shaman
    # Step 2. check if it is working (run in terminal):
    shaman --help
    # Step 3. copy an example* config file to your home folder:
    - (python2.7) cp /usr/local/lib/python2.7/dist-packages/shaman/etc/crawler.config ~/
    - (python3.4) cp /usr/local/lib/python3.4/dist-packages/shaman/etc/crawler.config ~/
    # Step 4. open this file (~/crawler.config) in your favorite text editor and change a basepath param as follows:
    -  (python2.7) basepath = /usr/local/lib/python2.7/dist-packages/shaman
    -  (python3.4) basepath = /usr/local/lib/python3.4/dist-packages/shaman
    # Step 5. Run it using a config:
    echo "http://yandex.ru" | shaman -c ~/crawler.config -i
        Output should look like this:
        url : http://yandex.ru
        charset: utf-8
    stage shutdown called

*  there are 4 stages in a default config file:
    - stdin_reader_stage - reads from stding
    - download_stage - downloads a web page
    - charsetdetect_stage - defines a charset
    - message_printer - prints results


----------------

If the instructions above did not work for you please let us know and
send e-mail to `artemzraev@gmail.com`.

.. vim:ft=rst
