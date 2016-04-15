#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


__author__ = 'opportunity356'


def heapsort(a):
    n = len(a)
    i = n // 2 - 1
    end_pos = n
    # building a heap
    while i >= 0:
        sift_down(a, i, end_pos)
        i -= 1

    end_pos = n - 1
    while end_pos > 0:
        a[0], a[end_pos] = a[end_pos], a[0]
        sift_down(a, 0, end_pos)
        end_pos -= 1

    return a


def sift_down(a, j, end_pos):
    while 2 * j + 1 < end_pos:
        k = max_child(a, j, end_pos)
        if a[j] < a[k]:
            a[j], a[k] = a[k], a[j]
            j = k
        else:
            break


def max_child(a, j, r):
    left_child = 2 * j + 1
    right_child = left_child + 1
    max_ch = left_child
    if right_child < r and a[right_child] > a[left_child]:
        max_ch = right_child
    return max_ch


def main():
    items = range(0, 25)
    random.shuffle(items)
    print 'shuffled', items
    print 'sorted', heapsort(items)


if __name__ == '__main__':
    main()
