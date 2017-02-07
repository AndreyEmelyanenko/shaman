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

    # Step 1. Clone repository and build
    git clone https://github.com/Landish145/shaman
    cd shaman
    # Step 2. Install python packages (minimum)
    wget https://bootstrap.pypa.io/get-pip.py
    python get-pip.py
    pip install -r requirements.txt
    # Step 3. Add shaman to a PYTHONPATH
    export PYTHONPATH=<shaman_dir>:$PYTHONPATH

Now you should be able to use shaman command line utility (try ``python bin/daemon.py --help``).


----------------

If the instructions above did not work for you please let us know and
send e-mail to `artemzraev@gmail.com`.

.. vim:ft=rst