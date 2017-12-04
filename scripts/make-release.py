#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    make-release
    ~~~~~~~~~~~~

    Helper script that performs a release.  Does pretty much everything
    automatically for us.

    :copyright: (c) 2017 by Ma Fei.
"""
import re
import sys
from subprocess import Popen, PIPE


def set_filename_version(filename, version_number, pattern):
    changed = []

    def inject_version(match):
        before, old, after = match.groups()
        changed.append(True)
        return before + version_number + after

    with open(filename) as f:
        contents = re.sub(r"^(\s*%s\s*=\s*')(.+?)(')" % pattern,
                          inject_version, f.read(),
                          flags=re.DOTALL | re.MULTILINE)

    if not changed:
        fail('Could not find %s in %s', pattern, filename)

    with open(filename, 'w') as f:
        f.write(contents)


def set_init_version(version):
    info('Setting __init__.py version to %s', version)
    set_filename_version('proxy/__init__.py', version, '__version__')


def fail(message, *args):
    print >> sys.stderr, 'Error:', message % args
    sys.exit(1)


def info(message, *args):
    print >> sys.stderr, message % args


def main():
    describe = 'git rev-list --count HEAD'
    version = Popen(describe.split(), stdout=PIPE).communicate()[0].strip()
    set_init_version(version)


if __name__ == '__main__':
    main()
