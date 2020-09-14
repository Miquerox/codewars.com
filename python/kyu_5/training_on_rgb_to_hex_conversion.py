# https://www.codewars.com/kata/513e08acc600c94f01000001/train/python


def rgb(r, g, b):
    r, g, b = [min(max(c, 0), 255) for c in (r, g, b)]
    return ''.join(map(lambda c: hex(c)[2:].zfill(2).upper(), (r, g, b)))
