#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'opportunity356'

import unittest


def fib(n):
    """
    Function computes n-th element of Fibonacci sequence using fast matrix
    exponentiation algorithm. Theoretical complexity is O(n). Practically
    it seems to be worse then O(n), cause of bignum arithmetic.
    """
    if n < 0:
        return (-1) ** (n % 2 + 1) * fib(-n)

    # a, b, c are elements of symmetric matrix P:
    # |a b|      |1 1|
    # |b c|  =>  |1 0|
    #
    # x, y are elements of vector v = (x, y) = (0, 1)
    a = b = y = 1
    c = x = 0

    i = n
    while i:
        if i & 1:  # if the current bit of n's binary representation is 1
            # multiplying vector v and matrix P
            (x, y) = (a * x + b * y,
                      b * x + c * y)
            i -= 1  # setting the current bit to 0
        else:
            # multiplying matrix P by itself
            (a, b, c) = (a * a + b * b,
                         a * b + b * c,
                         b * b + c * c)
            i >>= 1  # getting next bit
    return x


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
