#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "opportunity356"


def gcd(u, v):
    """
    Euclidean algorithm.
    """
    if v > u:
        u, v = v, u

    while v != 0:
        r = u % v
        u = v
        v = r

    return u


def main():
    print gcd(40902, 24140)


if __name__ == "__main__":
    main()