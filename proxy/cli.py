#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    proxy.cli
    ~~~~~~~~~~~~

    This module is the main of proxy.

    :copyright: (c) 2017 by Ma Fei.
"""
import logging
import os
import signal

import click

import proxy

logger = logging.getLogger(__name__)


def output_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo("Version: {}".format(proxy.__version__))
    ctx.exit()


@click.command()
@click.option(
    '-v',
    '--version',
    is_flag=True,
    is_eager=True,
    callback=output_version,
    expose_value=False,
    help="show the version of this tool")
@click.option(
    '-l',
    '--log',
    default='INFO',
    help='Specify logging level, default is INFO')
def parse_command(log):
    log_level = getattr(logging, log.upper())
    logging.basicConfig(level=log_level)


def signal_handler(signum, frame):
    logger.info("main process(%d) got GracefulExitException" % os.getpid())
    os._exit(0)


def main():
    print("A Terminal Tools For agent Agent")
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    parse_command()


if __name__ == "__main__":
    main()
