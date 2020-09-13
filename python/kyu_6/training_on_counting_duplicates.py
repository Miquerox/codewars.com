# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python

import collections


def duplicate_count(text):
    return len(set(filter(lambda x: x[1] if x[1] != 1 else 0,
                          collections.Counter(text.lower()).items())))
