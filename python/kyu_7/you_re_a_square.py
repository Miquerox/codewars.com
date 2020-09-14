# https://www.codewars.com/kata/54c27a33fb7da0db0100040e/python


def is_square(n):
    return True if n >= 0 and (n ** 0.5).is_integer() else False
