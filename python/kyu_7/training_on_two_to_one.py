# https://www.codewars.com/kata/5656b6906de340bd1b0000ac/train/python


def longest(s1, s2):
    return ''.join(sorted(list(set(s1) | set(s2))))
