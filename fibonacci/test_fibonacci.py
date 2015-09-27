#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'opportunity356'

from fibonacci import fib

import unittest


class FibonacciTest(unittest.TestCase):
    def test_initial(self):
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)

    def test_positive(self):
        self.assertEqual(fib(3), 2)
        self.assertEqual(fib(8), 21)

    def test_negative(self):
        self.assertEqual(fib(-6), -8)
        self.assertEqual(fib(-9), 34)

    def test_big_positive(self):
        self.assertEqual(fib(332),
                         1082459262056433063877940200966638133809015267665311237542082678938909)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
