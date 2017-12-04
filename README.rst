Installation
============

Install ``qpagent`` for the first time::

    $ pip install qpagent -i http://pypi.dev.elenet.me/eleme/eleme --trusted-host pypi.dev.elenet.me


Upgrade
-------

If you have installed ``qpagent`` before and want to upgrade to the latest version, you can use the ``-U`` option.

This option works on each installation method described above. ::

    $ pip install -U qpagent -i http://pypi.dev.elenet.me/eleme/eleme --trusted-host pypi.dev.elenet.me

Check Installation
------------------

When qpagent is installed, a **qpagent** command should be available in your shell (if you're not using
virtualenv—which you should—make sure your python script directory is on your path).

To see ``qpagent`` version: ::

    $ qpagent -v
    A Terminal Tools For agent Agent
    Version: 239

To see available options, run::

    $ qpagent --help
    A Terminal Tools For agent Agent
    Usage: qpagent [OPTIONS]

    Options:
        -v, --version           show the version of this tool
        -e, --environment TEXT  select a development environment such as
                          alpha|beta|prod
        --help                  Show this message and exit.


Supported Python Versions
-------------------------

qpagent supports Python 2.7.

``qpagent`` has been tested on ``macOS`` platforms.

