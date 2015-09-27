#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'opportunity356'


def fib(n):
    """
    Function computes n-th element of Fibonacci sequence using fast matrix
    exponentiation algorithm. Function accepts both positive and negative
    numbers.
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
