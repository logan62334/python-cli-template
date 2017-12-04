#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    proxy.util.host
    ~~~~~~~~~~~~

    This module provide the host tool.

    :copyright: (c) 2017 by Ma Fei.
"""
import socket

from proxy.exc import ProxyException


def ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        _ip = s.getsockname()[0]
    except Exception as e:
        raise ProxyException(e)
    finally:
        s.close()

    return _ip


def name():
    return socket.gethostname()
