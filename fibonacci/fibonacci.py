#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'opportunity356'

import unittest


def fib(n):
    """
    |1 1|
    |1 0|
    :param n:
    :return:
    """
    if n < 0:
        return (-1)**(n % 2 + 1) * fib(-n)
    a = b = y = 1
    c = x = 0

    i = n
    while i:
        if i & 1:
            (x, y) = (a * x + b * y,
                      b * x + c * y)

        (a, b, c) = (a * a + b * b,
                     a * b + b * c,
                     b * b + c * c)
        i >>= 1
    return x


class FibonacciTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(3), 1)
        # self.assertEqual(fib(), 1)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
