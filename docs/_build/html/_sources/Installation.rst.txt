.. default-role:: code

Installation
============

Install ``proxy`` for the first time::

    $ pip install proxy


Upgrade
-------

If you have installed ``proxy`` before and want to upgrade to the latest version, you can use the ``-U`` option.

This option works on each installation method described above. ::

    $ pip install -U proxy

Check Installation
------------------

When proxy is installed, a **proxy** command should be available in your shell (if you're not using
virtualenv—which you should—make sure your python script directory is on your path).

To see ``proxy`` version: ::

    $ proxy -v
    A Terminal Tools For proxy
    Version: 0.0.1

To see available options, run::

    $ proxy --help
    A Terminal Tools For proxy
    Usage: proxy [OPTIONS]

    Options:
        -v, --version           show the version of this tool
        --help                  Show this message and exit.


Supported Python Versions
-------------------------

proxy supports Python 2.7.

``proxy`` has been tested on ``macOS`` platforms.

