#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    proxy
    ~~~~~~~~~~~~

    This module is the main config.

    :copyright: (c) 2017 by Ma Fei.
"""
from logging.config import dictConfig

__version__ = '0.0.1'

LOGGING_CONFIG = dict({
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    'loggers': {
        'shortener': {
            'handlers': ['console'],
            'propagate': False,
            'level': 'INFO',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        },
    },
    'formatters': {
        'console': {
            'format': '%(asctime)s [%(levelname)s] [%(name)s][%(process)d]'
                      ': %(message)s',
        },
    }
})
dictConfig(LOGGING_CONFIG)
