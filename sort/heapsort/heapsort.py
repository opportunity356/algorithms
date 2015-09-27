#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


__author__ = 'opportunity356'


def heapsort(a):
    n = len(a)
    i = n // 2 - 1
    r = n
    # building a heap
    while i >= 0:
        push_down(a, i, r)
        i -= 1

    r = n - 1
    while r > 0:
        a[0], a[r] = a[r], a[0]
        push_down(a, 0, r)
        r -= 1

    return a


def push_down(a, j, r):
    while 2 * j + 1 < r:
        k = max_child(a, j, r)
        if a[j] < a[k]:
            a[j], a[k] = a[k], a[j]
            j = k
        else:
            break


def max_child(a, j, r):
    if 2 * j + 2 < r:
        if a[2 * j + 2] > a[2 * j + 1]:
            return 2 * j + 2
    return 2 * j + 1


def main():
    items = range(0, 25)
    random.shuffle(items)
    print 'shuffled', items
    print 'sorted', heapsort(items)


if __name__ == '__main__':
    main()
