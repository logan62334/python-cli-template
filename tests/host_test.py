#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

import agent.util.host as host


class TestHost(unittest.TestCase):
    def test_ip(self):
        self.assertIsNotNone(host.ip())

    def test_name(self):
        self.assertIsNotNone(host.name())


if __name__ == '__main__':
    unittest.main()
